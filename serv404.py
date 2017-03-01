#!/usr/bin/env python

import BaseHTTPServer
import sys
import argparse


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_error(code, message)
        return

    def do_POST(self):
        self.send_error(code, message)
        return


def main():
    global code, message
    desc = "Runs a small http server. Returns 404 (or your "\
           "choice of code) on all GET and POST requests."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--port', dest='port', action='store',
            default=8000, type=int,
            help="Run server on this port")
    parser.add_argument('--code', dest='code', action='store',
            default=404, type=int,
            help="Return this code on all requests")
    parser.add_argument('--message', dest='message', action='store',
            default='', type=str,
            help="Send this message on all requests")
    args = parser.parse_args()
    port = args.port
    code = args.code
    message = args.message
    if len(message) < 1:
        message = 'Custom {}'.format(code)
    server_address = ('', port)
    httpd = BaseHTTPServer.HTTPServer(server_address, MyHandler)
    print 'serving {}s on port {}'.format(code, port)
    httpd.serve_forever()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
