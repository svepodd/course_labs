from flask import Flask, request, make_response
import sqlite3
import os
import subprocess
import logging
import ast
import ipaddress

app = Flask(__name__)

app.config["DEBUG"] = True

DB_USER = "admin"
DB_PASSWORD = "SuperSecret123"
DB_PATH = "app.db"

logging.basicConfig(level=logging.DEBUG)

SAFE_READ_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "safe_files"))
os.makedirs(SAFE_READ_DIR, exist_ok=True)


def _safe_calc(expr: str):
    node = ast.parse(expr, mode="eval")
    allowed = (
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.Num,
        ast.Constant,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.USub,
        ast.UAdd,
    )
    for n in ast.walk(node):
        if not isinstance(n, allowed):
            raise ValueError("Unsupported expression")
        if isinstance(n, ast.Constant) and not isinstance(n.value, (int, float)):
            raise ValueError("Only numbers allowed")

    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        if isinstance(n, ast.Num):
            return n.n
        if isinstance(n, ast.Constant):
            return n.value
        if isinstance(n, ast.UnaryOp):
            v = _eval(n.operand)
            return +v if isinstance(n.op, ast.UAdd) else -v
        if isinstance(n, ast.BinOp):
            a, b = _eval(n.left), _eval(n.right)
            if isinstance(n.op, ast.Add):
                return a + b
            if isinstance(n.op, ast.Sub):
                return a - b
            if isinstance(n.op, ast.Mult):
                return a * b
            if isinstance(n.op, ast.Div):
                return a / b
        raise ValueError("Unsupported expression")

    return _eval(node)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn


@app.route("/")
def index():
    return "OK"


@app.route("/user")
def get_user():
    username = request.args.get("name", "")
    conn = get_db()
    cur = conn.cursor()
    query = f"SELECT id, name, email FROM users WHERE name = '{username}'"
    app.logger.debug("Executing query: %s", query)
    rows = cur.execute(query).fetchall()
    conn.close()
    return {"result": rows}


@app.route("/search")
def search():
    q = request.args.get("q", "")
    html = f"<h1>Results for: {q}</h1>"
    return make_response(html, 200)


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return "Invalid host", 400
    subprocess.run(
        ["ping", "-c", "1", host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    return f"Pinged {host}"


@app.route("/backup")
def backup():
    target = request.args.get("target", "/tmp/backup.sql")
    cmd = ["sh", "-c", f"pg_dump mydb > {target}"]
    subprocess.call(cmd)
    return f"Backup to {target} started"


@app.route("/read")
def read_file():
    path = request.args.get("path", "/etc/passwd")
    try:
        if os.path.isabs(path):
            return "Absolute paths are not allowed", 400
        norm = os.path.normpath(path)
        if norm.startswith("..") or "/.." in norm.replace("\\", "/"):
            return "Path traversal detected", 400
        full_path = os.path.abspath(os.path.join(SAFE_READ_DIR, norm))
        if not full_path.startswith(SAFE_READ_DIR + os.sep):
            return "Invalid path", 400

        with open(full_path, "r", encoding="utf-8", errors="replace") as f:
            data = f.read()
        return f"<pre>{data}</pre>"
    except Exception as e:
        return str(e), 500


@app.route("/load")
def load():
    data = request.args.get("data", "")
    try:
        raw = bytes.fromhex(data)
        return f"Loaded data length: {len(raw)}"
    except Exception as e:
        return f"Error: {e}", 500


@app.route("/calc")
def calc():
    expr = request.args.get("expr", "1+1")
    try:
        result = _safe_calc(expr)
        return str(result)
    except Exception:
        return "Invalid expression", 400


@app.route("/debug")
def debug():
    headers = dict(request.headers)
    return {
        "headers": headers,
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
