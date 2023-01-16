from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "0.0.0.0"
serverPort = 8081

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        f = open("name.txt", "r")
        name = f.read()
        self.wfile.write(bytes("Hello " + name, "utf-8"))

webServer = HTTPServer((hostName, serverPort), MyServer)
print("Server started http://%s:%s" % (hostName, serverPort))

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()