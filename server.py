import mimetypes
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 2500

class Server(BaseHTTPRequestHandler):
    modelData = None

    def do_GET(self):
        global mimetype
        if self.path == "/":
            self.path = "/main.html"

        try:

            sendReply = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith(".png"):
                mimetype = 'image/png'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            if self.path.endswith(".svg"):
                mimetype = 'image/svg+xml'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".ttf"):
                mimetype = 'application/x-font-ttf'
                sendReply = True
            if self.path.endswith(".otf"):
                mimetype = 'application/x-font-opentype'
                sendReply = True
            if self.path.endswith(".woff"):
                mimetype = 'application/font-woff'
                sendReply = True

            if sendReply == True:
                f = open(os.getcwd() + self.path, 'rb')
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                print(os.getcwd() + self.path)
            return

        except Exception as e:
            self.send_error(404, 'Error: %s' % e)

def start_server():
    # if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")