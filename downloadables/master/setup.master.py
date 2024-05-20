# Coordinate
# Author - Yash Pant

# Master node setup

import json
import os
import sys
import pathlib 

VERSION = "0.1.0"
class MasterEnv:
    def __init__(self):
        self.node_name = None
        self.setup_type = "master"
        self.version = VERSION
        # Collects information about the existing env and desired setup.
        self.database = Database_Mongo()
        self.network = Network_Local()
        self.storage = Storage_Local()
        self.webui = WebUI()
        # Executes all details collected by the previous extensions.
        self.runner = Runner_Python()

class Database_Mongo:
    def __init__(self):
        self.ext_name = "Database_Mongo"

        self.db_path = None
        self.sh_path = None

class Network_Local:
    def __init__(self):
        self.ext_name = "Network_Local"

        self.webui_port = None
        self.server_port = None
        self.worker_ips = None

class Storage_Local:
    def __init__(self):
        self.ext_name = "Storage_Local"

        self.path = None

class WebUI:
    def __init__(self):
        self.run_command = "npm run dev"

class Runner_Python:
    def __init__(self):
        self.ext_name = "Runner_Python"

        self.pyVersion = None
        self.venv_path = None
        self.path = None

env = MasterEnv()

SETUP_DIR_PATH = pathlib.Path(__file__).parent.resolve().__str__().replace("\\", "/")

def getNodeName():
    print("Name this node [Commonly the device name]: ")
    env.node_name = input()

def getPythonDetails():
    verifyPVersion()
    getPExecutable()
    getVenvPath()

def verifyPVersion():
    ver = sys.version.split(" ")[0]
    print("Py interpreter version:", ver)
    env.runner.pyVersion = ver

def getPExecutable():
    path = sys.executable
    path = path.replace('\\', "/")
    env.runner.path = path

def getVenvPath():
    print("Python virtual env path: ")
    env.runner.venv_path = input()

def getMongodbDetails():
    getMDbPath()
    getMShellPath()

def getMDbPath():
    print("Mongo db path: ")
    env.database.db_path = input()

def getMShellPath():
    print("Mongo shell path: ")
    env.database.sh_path = input()

def getWebUIDetails():
    print("Web-client start command [blank for default]:")
    x = input()
    if not x == "":
        env.webui.run_command = x

def getNetworkDetails():
    getWebUIPort()
    getServerPort()
    getWorkerIPs()

def getWebUIPort():
    print("Webui port: ")
    env.network.webui_port = input()

def getServerPort():
    print("Server port: ")
    env.network.server_port = input()

def getWorkerIPs():
    print("Worker node IPs: ")
    ips = input().split(',')
    for index, ip in enumerate(ips):
        ips[index] = ip.strip()
    env.network.worker_ips = ips

def getStorageDetails():
    getSPath()

def getSPath():
    print("Storage path: ")
    env.storage.path = input()

def envSetup():
    print("Coordinate Environment Setup")
    getNodeName()
    getPythonDetails()
    getMongodbDetails()
    getWebUIDetails()
    getNetworkDetails()
    getStorageDetails()

def envWrite():
    import jsonpickle
    env_file = f"{env.storage.path}/env.json"
    os.makedirs(os.path.dirname(env_file), exist_ok=True)
    f = open(env_file, "w+")
    env_data = jsonpickle.encode(env, unpicklable=False)
    print("- - - -")
    print("Master Environment file:")
    print(json.dumps(json.loads(env_data), indent=4))
    print("- - - -")
    f.write(env_data)

def preinstall_info():
    print("- - - -")
    print("Ensure you have the following installed already:")
    print("A python version that is compliant with 3.12")
    print("A py virtual environment & requirements(found in requirements.master.txt)")
    print("Mongo DB and shell")
    print("- - - -")

if __name__ == "__main__":
    print(f"Coordinate -v{VERSION}")
    print(f"Master node setup")
    preinstall_info()
    envSetup()
    envWrite()
    # TODO: copyRunToStorage()
    print("Setup completed. Use the run file to start the server.")