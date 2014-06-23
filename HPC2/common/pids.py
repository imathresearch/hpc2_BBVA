'''
Created on 23/06/2014

This module is a global module used to associate running processes with iMath Cloud Job Ids
PROVISIONAL SOLUTION

@author: iMath
'''
import json

FILE_NAME = "jobs_to_pids.json"

def init():
    listPids = dict();
    saveDict(listPids)
    
def addEntry(jobId, process):
    listPids = getDict()
    listPids[jobId] = process;
    saveDict(listPids);
    
def getProcess(jobId):
    listPids = getDict();
    if jobId in listPids:
        return listPids[jobId];
    return None;

def getDict():
    listPids = json.load(open(FILE_NAME))
    return listPids

def saveDict(listPids):
    json.dump(listPids, open(FILE_NAME, 'wb'))