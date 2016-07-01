from zapv2 import ZAPv2
import sys
import time
from pprint import pprint

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

# Give some time to spider for getting started :)
time.sleep(4)

while (int(zap.spider.status()) < 100):    
    print 'Spider progress %: ' + zap.spider.status()       
    time.sleep(2)

#####################################################################
print 'Scanning target %s' % input_target

zap.ascan.scan(input_target, apikey = API_Key)
while (int(zap.ascan.status()) < 100):
    print 'Scan progress %: ' + zap.ascan.status()
    time.sleep(5)
#####################################################################

print 'Alerts: '
pprint (zap.core.alerts())