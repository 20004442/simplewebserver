from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang=en>
<head>
<title>webserver</title>
</head>
<body>
<h1>MULTIPLICATION TABLES OF 7</h1>
7x0=0<br>
7x1=7<br>
7x2=14<br>
7x3=21<br>
7x4=28<br>
7x5=35<br>
7x6=42<br>
7x7=49<br>
7x8=56<br>
7x9=63<br>
7x10=70<br>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',80)
httpd = HTTPServer(server_address,myhandler)
print("webserver is running")
httpd.serve_forever()