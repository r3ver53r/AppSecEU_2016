from zapv2 import ZAPv2

# Use the line below if ZAP is not listening on 8080
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:7777', 'https': 'http://127.0.0.1:7777'})

print zap