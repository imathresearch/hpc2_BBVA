'''
Created on 23/06/2014

This module is a global module used to associate running processes with iMath Cloud Job Ids

@author: iMath
'''

def init():
    global listPids
    listPids = dict();
    
def addEntry(jobId, process):
    global listPids
    listPids[jobId] = process;
    
def getProcess(jobId):
    global listPids
    if jobId in listPids:
        return listPids[jobId];
    return None;

def deleteEntry(jobId):
    global listPids
    if jobId in listPids:
        del listPids[jobId];

def getDict():
    global listPids
    return listPids