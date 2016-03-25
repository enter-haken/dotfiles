#!/bin/env python
import os

repoPath = os.path.dirname(os.path.abspath(__file__))
configFilePath = os.path.join(repoPath, "configFiles")

filesInRepository = [ f for f in os.listdir(configFilePath) ] 

for f in filesInRepository:
    currentUserHome = os.getenv("HOME")
    dottetFile = '.' + f
    fileCandidate = os.path.join(currentUserHome, dottetFile)

    if os.path.isfile(fileCandidate):
        print("file {} exists in home directory. delete to proceed.".format(dottetFile))
        continue

    os.symlink(os.path.join(configFilePath, f), fileCandidate)
    print("symlink created for {}".format(dottetFile))

