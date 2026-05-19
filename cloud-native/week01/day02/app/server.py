from datetime import datetime, timezone
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


HOST = "127.0.0.1"
PORT = int(os.environ.get("PORT", "8000"))


class Day2Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.respond_html(200, self.home_page())
        elif self.path == "/health":
            self.respond_json(200, {"status": "ok", "service": "day2-demo"})
        elif self.path == "/api/time":
            self.respond_json(
                200,
                {
                    "time": datetime.now(timezone.utc).isoformat(),
                    "timezone": "UTC",
                },
            )
        else:
            self.respond_json(404, {"error": "not found", "path": self.path})

    def respond_html(self, status, body):
        encoded = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)
        self.print_request_log(status)

    def respond_json(self, status, payload):
        encoded = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)
        self.print_request_log(status)

    def print_request_log(self, status):
        print(f"{self.command} {self.path} -> {status}", flush=True)

    def log_message(self, format, *args):
        return

    def home_page(self):
        return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Day2 Demo App</title>
  <style>
    body {
      font-family: system-ui, sans-serif;
      max-width: 720px;
      margin: 48px auto;
      padding: 0 20px;
      line-height: 1.6;
    }
    code { background: #eef2ff; padding: 2px 6px; border-radius: 4px; }
    .card { border: 1px solid #d0d7de; border-radius: 8px; padding: 16px; }
  </style>
</head>
<body>
  <h1>Day2 Demo App</h1>
  <p>이 페이지는 내 컴퓨터에서 실행 중인 작은 웹 서버가 응답한 화면입니다.</p>
  <div class="card">
    <p>확인할 경로:</p>
    <ul>
      <li><code>/</code> - HTML 화면</li>
      <li><code>/health</code> - 상태 확인 JSON</li>
      <li><code>/api/time</code> - 현재 시간 JSON</li>
      <li><code>/missing</code> - 404 관찰</li>
    </ul>
  </div>
</body>
</html>
"""


def main():
    server = ThreadingHTTPServer((HOST, PORT), Day2Handler)
    print("starting day2 demo server", flush=True)
    print(f"listening on http://localhost:{PORT}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nserver stopped", flush=True)
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
