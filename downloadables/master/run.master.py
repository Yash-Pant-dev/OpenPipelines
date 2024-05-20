# Coordinate
# Author: Yash Pant

# TODO: Start the webui, network, connect to workers, transmit sanity check data.
# connect to mongo and create log
# transfer files b/w nodes

import json

env = None
def load_env():
    global env
    env = json.load("env.json")

if __name__ == "__main__":
    VERSION = "0.1.0"
    print(f"Coordinate -v{VERSION}")
    print("Master node")
    print("----")

    load_env()