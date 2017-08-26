import xarray as xr
import pandas as pd
import os


def loadRecursive(path, extensions, folderLevel=0):
    path = path.rstrip(os.sep)  # remove trailing slash
    folderName = path.split(os.sep)[-1]  # gets current folder name
    dirs = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    dataFrames = []
    if len(dirs) > 0:
        for d in dirs:
            folder = os.path.join(path, d)
            dataFrames.append(loadRecursive(folder, extensions, folderLevel + 1))
    else:
        for root, dirs, filenames in os.walk(path):
            for f in filenames:
                if f.endswith(extensions):
                    # print f
                    path = os.path.join(root, f)
                    # df = pd.read_csv(path)
                    df = pd.read_table(path, header=20)
                    dataFrames.append(df)
    if (len(dataFrames) > 0):
        da = pd.concat(dataFrames)
        da[('level_' + str(folderLevel))] = folderName
        return da
    return pd.DataFrame()
