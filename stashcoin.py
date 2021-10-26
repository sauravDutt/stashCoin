# Program to create a Blockchain (General)

# For Timestamp
import datetime

# Calxulatin the hash
# in order to add ditital
# fingerprints to the blocks
import hashlib

# To store data
# in our blockchain
import json

# Flask is for creating the web app
# and jsonify is for displaying the 
# Blockchain
from flask import Flask, jsonify


class Blockchain:

    # This function creates the very
    # First block and set it's hash to "0"
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash='0')
    
    # This function adds further 
    # blocks into the chain
    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp' : str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }

        self.chain.append(block)
        return block
    
    # This function display the previous block
    def print_previous_block(self, ):
        return self.chain[-1]
    
    # This is the function for proof of work 
    # and used to successfully mine the block
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()
            ).hexdigest()

            if hash_operation[:4] == '00000':
                check_proof = True
            else:
                new_proof += 1
        
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()
            ).hexdigest()

            if hash_operation[:4] != '00000':
                return False
            
            previous_block = block
            block_index += 1
        
        return True

# Creating the Web App using flask
app = Flask(__name__)

# Create the object
# of the class blockchain
blockchain = Blockchain()

# Mining a new block
app.route('/mine_block', methods = ['GET'])
def main_block():
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
