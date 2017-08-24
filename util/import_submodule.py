def addProjToSysPath(projName):
    import os
    import sys
    path = os.path.realpath(__file__)
    projectPath = path[:path.find(projName)] + projName
    sys.path.append(projectPath)
