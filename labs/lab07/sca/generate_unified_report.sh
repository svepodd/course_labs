#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="${ROOT_DIR}/sca/unified-report"
mkdir -p "${OUT_DIR}"

echo "[*] Generating unified SAST+SCA report..."

python3 <<'PY'
import json, csv, os
from pathlib import Path

root = Path(__file__).resolve().parent.parent
out = root / "sca" / "unified-report"
out.mkdir(parents=True, exist_ok=True)

# Источники отчётов
sources = {
    "semgrep": root / "sast" / "semgrep-report.json",
    "checkov": root / "sast" / "checkov-report.json" / "results_json.json",
    "dep_maven": root / "sca" / "dependency-check-report" / "dependency-check-report.json",
    "dep_py": root / "sca" / "dependency-check-report-app" / "dependency-check-report.json"
}

records = []
for name, path in sources.items():
    if not path.exists():
        continue
    try:
        data = json.load(open(path))
    except Exception as e:
        print(f"[WARN] can't parse {path}: {e}")
        continue

    # Semgrep
    if name == "semgrep" and "results" in data:
        for r in data["results"]:
            records.append({
                "tool": "Semgrep",
                "file": r.get("path"),
                "id": r.get("check_id"),
                "severity": r.get("extra", {}).get("severity"),
                "message": r.get("extra", {}).get("message"),
                "line": r.get("start", {}).get("line"),
            })

    # Checkov
    elif name == "checkov" and "results" in data:
        failed = data["results"].get("failed_checks", [])
        for r in failed:
            records.append({
                "tool": "Checkov",
                "file": r.get("file_path"),
                "id": r.get("check_id"),
                "severity": r.get("severity"),
                "message": r.get("check_name"),
                "line": r.get("file_line_range", [None])[0],
            })

    # Dependency-Check
    elif "dependencies" in data:
        for dep in data["dependencies"]:
            vulns = dep.get("vulnerabilities") or []
            for v in vulns:
                records.append({
                    "tool": "Dependency-Check",
                    "file": dep.get("fileName"),
                    "id": v.get("name"),
                    "severity": v.get("severity"),
                    "message": v.get("description", "")[:200],
                    "line": None,
                })

json_path = out / "unified-report.json"
csv_path  = out / "unified-report.csv"
html_path = out / "unified-report.html"

# JSON
json.dump(records, open(json_path, "w"), indent=2)

# CSV
with open(csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)

# HTML (простой шаблон)
with open(html_path, "w") as f:
    f.write("<html><head><meta charset='utf-8'><title>Unified SAST+SCA Report</title>")
    f.write("<style>table{border-collapse:collapse;width:100%}td,th{border:1px solid #ccc;padding:4px}</style></head><body>")
    f.write("<h2>Unified SAST+SCA Report</h2><table><tr>")
    for col in records[0].keys():
        f.write(f"<th>{col}</th>")
    f.write("</tr>")
    for r in records:
        f.write("<tr>" + "".join(f"<td>{r.get(c,'')}</td>" for c in records[0].keys()) + "</tr>")
    f.write("</table></body></html>")

print(f"[+] Unified report generated: {out}")
print(f"    - {json_path}")
print(f"    - {csv_path}")
print(f"    - {html_path}")
PY
