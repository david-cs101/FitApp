#!/usr/bin/env python3
import http.server
import json
import os
import socket

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.json')
SERVE_DIR  = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SERVE_DIR, **kwargs)

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path == '/api/load':
            try:
                with open(DATA_FILE, 'r') as f:
                    data = f.read()
            except FileNotFoundError:
                data = '{}'
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self._cors()
            self.end_headers()
            self.wfile.write(data.encode())
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/save':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            with open(DATA_FILE, 'w') as f:
                f.write(body.decode())
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self._cors()
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
        else:
            self.send_response(404)
            self.end_headers()

    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def log_message(self, format, *args):
        pass  # Silenciar logs

if __name__ == '__main__':
    ip = 'desconocida'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
    except Exception:
        pass

    PORT = 8080
    print()
    print("  ╔═══════════════════════════════════════╗")
    print("  ║           FitPlan · Servidor           ║")
    print("  ╚═══════════════════════════════════════╝")
    print()
    print("  Mac y iPhone deben estar en el mismo WiFi.")
    print()
    print("  Abre esto en Safari de tu iPhone:")
    print()
    print(f"  ➜  http://{ip}:{PORT}/index.html")
    print()
    print("  Datos guardados en: data.json (carpeta FitApp)")
    print()
    print("  (Ctrl+C para detener)")
    print()

    with http.server.HTTPServer(('', PORT), Handler) as httpd:
        httpd.serve_forever()
