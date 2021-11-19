# Smart contracts unit test generator

A small draft of a tool that will automatically generate a lot of cool routine tests for every Ethereum compatible contract.

## Prerequirements

- python3
- node, npm
- ganache-cli

## Installation

- python3 -m venv env 
- source env/bin/activate
- pip install -r requirements.txt
- brownie compile
- python3 contracts/app.py
- localhost:5000/generate