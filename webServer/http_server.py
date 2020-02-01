#run in python3
import http.server
import socketserver

HOST = '0.0.0.0'
PORT = 8083
Handler = http.server.SimpleHTTPRequestHandler  #handle with index.html

'''
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
'''

httpd = socketserver.TCPServer((HOST, PORT), Handler)
print("servig at ip:port ", HOST, PORT)
httpd.serve_forever()
