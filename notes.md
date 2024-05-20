I can go the extremely well engineered route
# Do i need a database?
env - name, location, checksum (needed when uploading envs for others to use), pipelines
pipeline        
sources - intermediate sources distributed throughout the nodes, cant keep it in db?

# build the ui first so that i know what i need? also useful for sketching out everything.
Flow - login - add nodes - nodes will have acceptable name/token pairs that can connect
Sources - add loader fn, some metadata eg stream/batch etc
Function - add fn
Task - Select or create a Pipeline
Pipeline - select sources and fns from accessible ones

1 master orchestrator that has a db, rest of them only have files related to ongoing functions/intermediate sources.
Lets make it so that nothing remains on them after a pipeline is finished. 
If you want to keep it, you should have made a larger pipeline with the work you intended later on. 

# Replicable steps, ideally a single script should setup the whole thing, for each agent / principal.
Setup scripts can be used for this purpose.

# Highly configurable env (P2)
class MasterEnv:
    def __init__(self):
        self.node_name = None
        self.setup_type = "master"
        self.version = "0.1.0"

        # Collects information about the existing env and desired setup.
        self.database = Database_Mongo()
        self.network = Network_Local()
        self.storage = Storage_Local()
        
        # Executes all details collected by the previous extensions.
        self.runner = Runner_Python()
Similar to this above. 


# WebUI to Server comms
server and ui communicate through a new port 
express kinda situation
View-Model-Controller
py works with db and webui instructions