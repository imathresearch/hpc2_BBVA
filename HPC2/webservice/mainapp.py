# (C) 2013 iMath Research S.L. - All rights reserved.

""" The tornado-based module for iMathCloud restful connectivity

Authors:

* iMath
"""

import tornado.ioloop
import tornado.web
import multiprocessing
import time
import os
import errno
import psutil

from HPC2.common import pids

from HPC2.webservice.coreHandlers import SubmitHandler
from HPC2.webservice.coreHandlers import PluginHandler
from HPC2.webservice.coreHandlers import PCTHandler
from HPC2.webservice.coreHandlers import StopJobHandler

"""
This method is executed in an independent process to keep cleaning up the list of processes
that have terminated
"""
FREQ_GARBAGE_COLLECTOR = 60 * 15  # 900 seconds; 15 minutes

def pidExists(pidT): 
    pid = int(pidT)
    if pid < 0: return False #NOTE: pid == 0 returns True
    try:
        os.kill(pid, 0)     # Send signal 0 to the process. If exception process does not exists
                            # Warning, only works for LInux 
    except OSError:
        return False
    else:
        return True

def processGarbageCollector():
    while(True):
        hashmap = pids.getDict()
        toDelete = []
        for idJob in hashmap:
            pid = hashmap[idJob]
            if not pidExists(pid):
                toDelete += [idJob]
            else:
                proc = psutil.Process(int(pid))
                print int(pid)
                if (proc.status == psutil.STATUS_ZOMBIE):
                    os.kill(int(pid),9)
                    toDelete += [idJob]
                    
        for idJob in toDelete:
            del hashmap[idJob]
            print "Process cleaned: ", pid
                
        pids.saveDict(hashmap)
        time.sleep(FREQ_GARBAGE_COLLECTOR)
        
# We initialize the dictionary of JobsIds and Processes
pids.init() 

# We start the process garbage collector
t = multiprocessing.Process(target=processGarbageCollector, args=()) 
t.deamon = True
t.start()

# We start the tornado web server
application = tornado.web.Application([
    (r"/core/submit", SubmitHandler),
    (r"/plugin", PluginHandler),
    (r"/getpct", PCTHandler),
    (r"/stopJob", StopJobHandler)
])

if __name__ == "__main__":
    application.listen(8890,address='')
    tornado.ioloop.IOLoop.instance().start()
