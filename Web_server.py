from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"aaaaa")

    def do_POST(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, *argus):
        pass

class Web_server:
    def start():
        httpd = HTTPServer(('127.0.0.1', 8182), SimpleHTTPRequestHandler)
        print('http server')
        httpd.serve_forever()