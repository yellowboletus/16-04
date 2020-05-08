import http.server
import socketserver

port = 80
handler = http.server.SimpleHTTPRequestHandler # for storing the components, like EventListener in JS

my_web_server = socketserver.TCPServer(("", port), handler)
print("I will start to listen through port " + str(port))

# Start the webserver (by infinit loop)
my_web_server.serve_forever()