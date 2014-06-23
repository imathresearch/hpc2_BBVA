# (C) 2013 iMath Research S.L. - All rights reserved.

""" The tornado-based module for iMathCloud restful connectivity

Authors:

* iMath
"""

import tornado.ioloop
import tornado.web
import multiprocessing
import time

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
def processGarbageCollector():
    while(True):
        hashmap = pids.getDict()
        for idJob in hashmap:
            process = pids.getProcess(idJob)
            if not process.is_alive():
                pids.deleteEntry(idJob)
        
        time.sleep(FREQ_GARBAGE_COLLECTOR)
        
    
# We initialize the dictionary of JobsIds and PIDs
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
