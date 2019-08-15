from http.server import HTTPServer, BaseHTTPRequestHandler
from Operation_watcher import Operation_watcher
import json
from mylib.Config_controller.Config_controller import Config_controller
import threading

class SimpleHTTPServer(HTTPServer):
    operation_watcher: Operation_watcher
    lock: threading.RLock

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    server: SimpleHTTPServer
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        json_str = ""
        with self.server.lock:
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

    conf_c: Config_controller
    lock: threading.RLock

    def __init__(self, lock: threading.RLock):
        self.lock = lock
        self.conf_c = Config_controller("setting.ini")
        self.conf_c.cd("web_server")

    def start(self, operation_watcher: Operation_watcher):
        ip = self.conf_c.get("ip")
        port = self.conf_c.get("port")
        httpd = SimpleHTTPServer((ip, int(port)), SimpleHTTPRequestHandler)
        httpd.operation_watcher = operation_watcher
        httpd.lock = self.lock
        print(f"web server start at {ip}:{port}")
        httpd.serve_forever()