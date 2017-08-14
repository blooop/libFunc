import glob
import time
import os
import cPickle as pickle

def saveToDisk(data,name):
    pickle.dump(data, open(name, "wb"))

def loadFromDisk(name):
    return pickle.load(open(name, "rb"))

def cacheFunc(func,saveName,timeoutInMins =1):
    timeoutFilename = saveName+".cacheTimeout"
    cacheFileName = saveName + ".cache"
    currentTime = time.time()
    # print currentTime
    if os.path.isfile(timeoutFilename):
        lastTime = loadFromDisk(timeoutFilename)
        if currentTime-lastTime > timeoutInMins:
            print "loaded cache"
            return loadFromDisk(cacheFileName)
    print "caching function"
    dat = func()
    saveToDisk(dat,cacheFileName)
    saveToDisk(currentTime,timeoutFilename)
    return dat