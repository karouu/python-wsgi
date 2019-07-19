#run in python3
import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler # handle with index.html

'''
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
'''

httpd = socketserver.TCPServer(("",PORT), Handler)
print("servig at port", PORT)
httpd.serve_forever()
