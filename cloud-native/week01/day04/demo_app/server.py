import json
import os
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


BASE_DIR = Path(__file__).resolve().parent
PORT = int(os.environ.get("PORT", "8000"))
APP_NAME = os.environ.get("APP_NAME", "day4-shop")
DATA_FILE = os.environ.get("DATA_FILE", "data/products.json")
REQUIRE_DATA = os.environ.get("REQUIRE_DATA", "true").lower() != "false"


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def data_path():
    path = Path(DATA_FILE)
    if not path.is_absolute():
        path = BASE_DIR / path
    return path


def load_products():
    path = data_path()
    if not path.exists():
        raise FileNotFoundError(f"data file not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def health_status():
    try:
        products = load_products()
        return {
            "status": "ok",
            "app": APP_NAME,
            "product_count": len(products),
            "data_file": DATA_FILE,
            "time": utc_now(),
        }, 200
    except Exception as exc:
        status = {
            "status": "unhealthy" if REQUIRE_DATA else "degraded",
            "app": APP_NAME,
            "reason": str(exc),
            "data_file": DATA_FILE,
            "time": utc_now(),
        }
        return status, 503 if REQUIRE_DATA else 200


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        return

    def send_text(self, status, body, content_type="text/plain; charset=utf-8"):
        encoded = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)
        self.log_request_line(status)

    def send_json(self, status, payload):
        self.send_text(
            status,
            json.dumps(payload, ensure_ascii=False, indent=2),
            "application/json; charset=utf-8",
        )

    def log_request_line(self, status):
        print(
            f"{utc_now()} request method={self.command} "
            f"path={self.path} status={status}"
        )

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/":
            self.handle_index()
        elif path == "/api/products":
            self.handle_products()
        elif path == "/health":
            payload, status = health_status()
            self.send_json(status, payload)
        elif path == "/static/style.css":
            css = (BASE_DIR / "static" / "style.css").read_text(encoding="utf-8")
            self.send_text(200, css, "text/css; charset=utf-8")
        else:
            self.send_json(404, {"error": "not found", "path": path})

    def handle_index(self):
        try:
            products = load_products()
            items = "\n".join(
                f"<li><strong>{item['name']}</strong><span>{item['kind']}</span></li>"
                for item in products
            )
            status_label = "data connected"
        except Exception as exc:
            items = "<li><strong>상품 데이터를 불러오지 못했습니다.</strong><span>서버 로그와 /health를 확인하세요.</span></li>"
            status_label = f"data problem: {exc}"

        html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{APP_NAME}</title>
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>
  <main>
    <p class="eyebrow">Week1 Day4 Demo</p>
    <h1>{APP_NAME}</h1>
    <p>이 화면은 클라이언트가 보는 HTML 응답입니다.</p>
    <section>
      <h2>상품 목록</h2>
      <ul>{items}</ul>
    </section>
    <section class="checks">
      <a href="/api/products">/api/products</a>
      <a href="/health">/health</a>
      <a href="/no-page">/no-page</a>
    </section>
    <p class="status">{status_label}</p>
  </main>
</body>
</html>
"""
        self.send_text(200, html, "text/html; charset=utf-8")

    def handle_products(self):
        try:
            self.send_json(200, load_products())
        except Exception as exc:
            print(f"{utc_now()} error data_load_failed reason={exc}")
            self.send_json(500, {"error": "data load failed", "reason": str(exc)})


def main():
    server = ThreadingHTTPServer(("localhost", PORT), Handler)
    print(f"{APP_NAME} listening on http://localhost:{PORT}")
    print(f"data file: {data_path()}")
    print("stop with Ctrl+C")
    server.serve_forever()


if __name__ == "__main__":
    main()
