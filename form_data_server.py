import mimetypes
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 2500

class Server(BaseHTTPRequestHandler):
    # def do_GET(self):
    #     self.send_response(200)
    #     self.send_header("Content-type", "text/html")
    #     self.end_headers()
        # self.wfile.write(bytes('<html>'
        #                        '<head>'
        #                        '<title>Django Model Form Data</title>'
        #                        '<meta name="viewport" content="width=device-width, initial-scale=1.0>'
        #                        '<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">'
        #                        '</head>', 'utf-8'))
        # self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        # self.wfile.write(bytes("<body>", "utf-8"))
        # self.wfile.write(bytes('<div class ="container"><h1>Hello, world!</h1></div>', "utf-8"))
        # self.wfile.write(bytes("</body></html>", "utf-8"))
        # with open("template.html") as f:
        #     for line in f:
        #         self.wfile.write(bytes(line.rstrip("\n"), "utf-8"))

    def do_GET(self):
        global mimetype
        if self.path == "/":
            self.path = "/index.html"

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
                # Open the static file requested and send it
                f = open(os.getcwd() + self.path, 'rb')
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                print(os.getcwd() + self.path)
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def setModelsData(self,modelHtml):
        pass

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")