# Welcome to OpenPipelines
A highly customizable distributed coordination server and client to easily parallelize workloads across your compute nodes.

# Coordination structure
1. Single Principal
2. Many Agents
Each principal stores all the environments, functions & data sources, and distributes tasks to agents.
Each agent stores only the function & sources/intermediary sources of tasks, and returns them to the sink when needed.

