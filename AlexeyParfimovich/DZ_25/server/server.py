#!/usr/bin/env python3

import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler

# Запуск сервера на порте 1234. 
with socketserver.TCPServer(("", 1234), handler) as httpd:
    # Ожидание запросов от клиента.
    httpd.serve_forever()