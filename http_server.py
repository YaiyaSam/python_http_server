from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json

from sqlalchemy import null

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        message="no parameters"
        if query!="":
            query_components = dict(qc.split("=") for qc in query.split("&"))
            name = query_components["name"]
            message = "Ayo! are you that bitch called " + name +"?"
      
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "This is the post response"
        self.wfile.write(bytes(message, "utf8"))

    # def do_POST(self):
    #     content_len = int(self.headers.getheader('content-length'))
    #     post_body = self.rfile.read(content_len)
    #     self.send_response(200)
    #     self.end_headers()

    #     data = json.loads(post_body)

    #     message = "Hello, World! Here is a POST response"
    #     self.wfile.write(bytes(message, "utf8"))
    #     return 

with HTTPServer(('', 8080), handler) as server:
    server.serve_forever()