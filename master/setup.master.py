# Sets up the master node in the given folder.
# Tasks -
# Verify presence of mongo, mongosh
# [X]Build env file
# Create run file
# TODO: Create venv inside another folder.
# Create run file. The file will.

import os
import sys
import pathlib 
import subprocess

class PythonEnv:
    pyVersion = None
    path = None

class Mongo:
    db_path = None
    sh_path = None

class Network:
    port = None

class Storage:
    path = None

class MasterEnv:
    def __init__(self): 
        self.node_name = None
        self.type = "master"
        self.version = "0.1.0"
        self.python = PythonEnv()
        self.mongo = Mongo()
        self.network = Network()
        self.storage = Storage()

env = MasterEnv()
masterDirPath = pathlib.Path(__file__).parent.resolve().__str__().replace("\\", "/")

requirements = """
jsonpickle==3.0.4
"""

def getNodeName():
    print("Enter name of master node: ")
    env.node_name = input()

def getPythonDetails():
    verifyPVersion()
    getPExecutable()

def verifyPVersion():
    ver = sys.version.split(" ")[0]
    print("Py interpreter version:", ver)
    print("Press y if compatible with 3.12.3")
    
    ok = input()
    if (ok != "y"):
        exit()
    env.python.pyVersion = ver

def getPExecutable():
    env.python.path = sys.executable

def getMongodbDetails():
    getMDbPath()
    getMShellPath()

def getMDbPath():
    print("Enter mongo db absolute path: ")
    env.mongo.db_path = input()

def getMShellPath():
    print("Enter mongo shell absolute path: ")
    env.mongo.sh_path = input()

def getNetworkDetails():
    getNPort()

def getNPort():
    print("Enter network port: ")
    env.network.port = input()

def getStorageDetails():
    getSPath()

def getSPath():
    print("Enter storage path relative to master directory: ")
    env.storage.path = input()

def envSetup():
    print("Environment setup")
    getNodeName()
    getPythonDetails()
    getMongodbDetails()
    getNetworkDetails()
    getStorageDetails()

def envWrite():
    print("Writing environment file")

    import jsonpickle
    envFileData = jsonpickle.encode(env)
    envFileLoc = (masterDirPath + "/env.json")
    f = open(envFileLoc, "w")
    f.write(envFileData)
    f.close()

def virtualEnvSetup():
    print("Virtual Env setup")
    try:
        f = open(f"{masterDirPath}/pyvenv.cfg", "x")
    except:
        print("Virtual env already exists. Enter y to reinstall.")
        if (input() != "y"):
            installRequirements()
            return
    writeRequirements()
    os.system(f"python -m venv {masterDirPath}")
    installRequirements()
    

def writeRequirements():
    f = open(f"{masterDirPath}/requirements.txt", "w")
    f.write(requirements)
    f.close()

def installRequirements():
    activate = f"{masterDirPath}/Scripts/activate.bat"
    subprocess.run(activate)
    venvExePath = f"{masterDirPath}/Scripts/python.exe"
    venvCmd = f"{venvExePath} -m pip install -r {masterDirPath}/requirements.txt"
    # FIXME: Does not work on first run.
    subprocess.run(venvCmd)

def inVirtualEnv():
    return sys.prefix != sys.base_prefix

if __name__ == "__main__":
    print("OpenPipelines master node setup")
    if (inVirtualEnv()):
        envSetup()
        envWrite()
        print("Setup finished.")
    else:
        virtualEnvSetup()
        os.system(f"{masterDirPath}/Scripts/python.exe {masterDirPath}/setup.master.py")