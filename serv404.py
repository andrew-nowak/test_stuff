#!/usr/bin/env python

import BaseHTTPServer
import sys


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_error(404, 'Custom fourohfour')
        return

    def do_POST(self):
        self.send_error(404, 'Custom fourohfour')
        return

def main():
    port = 8000
    server_address = ('', port)
    httpd = BaseHTTPServer.HTTPServer(server_address, MyHandler)
    print 'serving 404s on port', port
    httpd.serve_forever()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
