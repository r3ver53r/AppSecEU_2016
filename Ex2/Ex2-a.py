from zapv2 import ZAPv2
import sys
import time

#Check script format. python script.py <Target> 
if len(sys.argv) < 2:
    print "Please enter the inputs in proper format"
    print "python zap.py <Target>"
    exit()
else:
    input_target    = sys.argv[1]

API_Key = 'id7cogi61fk9ef5a25bi76b6s7'

# Use the line below if ZAP is not listening on 8080
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:7777', 'https': 'http://127.0.0.1:7777'})

zap.spider.scan(input_target, apikey = API_Key)