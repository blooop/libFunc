import glob
import time
import os
import cPickle as pickle

def saveToDisk(data, name):
    pickle.dump(data, open(name, "wb"))


def loadFromDisk(name):
    return pickle.load(open(name, "rb"))


def cacheFunc(func, saveName, timeoutInMins=1):
    timeoutFilename = saveName + ".cacheTimeout"
    cacheFileName = saveName + ".cache"
    currentTime = time.time()
    # print currentTime
    if os.path.isfile(timeoutFilename):
        lastTime = loadFromDisk(timeoutFilename)
        if currentTime - lastTime > timeoutInMins:
            print "loaded cache"
            return loadFromDisk(cacheFileName)
    print "caching function"
    dat = func()
    saveToDisk(dat, cacheFileName)
    saveToDisk(currentTime, timeoutFilename)
    return dat


def getFilesMatchingExtension(extensions):
    file_paths = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(extensions):
                file_paths.append(os.path.join(root, file))  # Add it to the list.

    return file_paths


def getFileList(basePath, fileStart, numberOfFiles, extension):
    filenumlist = range(fileStart, fileStart + numberOfFiles)
    fileList = []
    for i in filenumlist:
        fileList.append(basePath + str(i) + extension)
    return fileList

def concatFiles(path,filenames,outputPath,readLinebyLine = False):
    with open( os.path.join(path,outputPath), 'w') as outfile:
        for fname in filenames:
            fname = os.path.join(path,fname)
            with open(fname) as infile:
                if readLinebyLine :
                    for line in infile:
                        outfile.write(line)
                else:
                    outfile.write(infile.read())
