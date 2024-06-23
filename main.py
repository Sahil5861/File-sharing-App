import http.server, png, os
import socket, socketserver, webbrowser, pyqrcode
from pyqrcode import QRCode

PORT = 8010
USER = os.environ['USERPROFILE']

folder = ''
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), folder)

os.chdir(desktop)

handler = http.server.SimpleHTTPRequestHandler
hostname = socket.gethostname()

# finding the IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

IP = "http://" + s.getsockname()[0] + ":"+ str(PORT)
link = IP

# converting the IP addresss into a QR code
url = pyqrcode.create(link)

url.svg("myqr.svg", scale=8)
webbrowser.open('myqr.svg')

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Type this is your browser {IP}")
    print("Or use the QRCode")
    httpd.serve_forever()