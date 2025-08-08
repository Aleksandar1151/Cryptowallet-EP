# Cryptowallet-EP
CorgiCoin is a simple decentralized blockchain network built in Python using Flask.
The project simulates multiple nodes communicating with each other through a REST API. Each node maintains its own blockchain, can add transactions, mine new blocks, and synchronize with other nodes in the network.

## Technologies
The application is written in Python and uses several key libraries:
- Flask for building the API
- Requests for HTTP communication between nodes
- Hashlib for SHA256 hashing
- Cryptography (in extended versions) for digital signatures

## Project structure
The project contains scripts for running three independent nodes:
- corgicoin_node_5001.py
- corgicoin_node_5002.py
- corgicoin_node_5003.py
There is also a config.py file with global settings, and optionally a Keys folder used for storing keys if you are running the version with transaction signing.

## Installation
First, clone the repository:
```
git clone https://github.com/your-username/corgicoin.git
cd corgicoin
```
It is recommended to create a virtual environment:
```
python3 -m venv venv
source venv/bin/activate   # on Linux/Mac
venv\Scripts\activate      # on Windows
```
Then install the dependencies:
```
pip install -r requirements.txt
```
