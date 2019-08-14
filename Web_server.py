from http.server import HTTPServer, BaseHTTPRequestHandler
from Operation_watcher import Operation_watcher
import json

class SimpleHTTPServer(HTTPServer):
    operation_watcher: Operation_watcher

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    server: SimpleHTTPServer
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        json_str = json.dumps({
            "last_operate_time": self.server.operation_watcher.last_operate_time,
            "last_operate_name": self.server.operation_watcher.last_operate_name,
            "interval_time": self.server.operation_watcher.interval_time
        })
        try:
            self.wfile.write(json_str.encode("utf8"))
        except:
            pass

    def do_POST(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, *argus):
        pass

class Web_server:

    def start(self, operation_watcher: Operation_watcher):
        ip = '127.0.0.1'
        port = 8182
        httpd = SimpleHTTPServer(('127.0.0.1', 8182), SimpleHTTPRequestHandler)
        httpd.operation_watcher = operation_watcher
        print(f"web server start at {ip}:{port}")
        httpd.serve_forever()