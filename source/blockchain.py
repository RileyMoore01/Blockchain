'''
Installs needed to run this

pip install Flask==0.12.2 requests==2.18.4 
'''

import hashlib
import json

from time import time
from uuid import uuid4

# creates an intital empty list (to store our blockchain) and another to store transactions
class Blockchain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []

  # creates a new block and adds it to the chain
  def new_block(self):
    """
      Create a new Block in the Blockchain
      :param proof: <int> The proof given by the Proof of Work algorithm
      :param previous_hash: (Optional) <str> Hash of previous Block
      :return: <dict> New Block
    """
    
    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'proof': proof,
      'previous_hash': previous_hash or self.hash(self.chain[-1]),
    }

  #reset the current list of transactions
  self.current_transactions = []

  self.chain.append(block)
  return block

  # add a new transaction to the list of transactions
  def new_transaction(self):
    """
      Creates a new transaction to go into the next mined Block
      :param sender: <str> Address of the Sender
      :param recipient: <str> Address of the Recipient
      :param amount: <int> Amount
      :return: <int> The index of the Block that will hold this transaction
    """
    
    self.current_transactions.append({
      'sender': sender,
      'recipient': recipient,
      'amount': amount,
    })

    return self.last_block['index'] + 1

  #hashes a block
  @staticmethod
  def hash(self):
      """
      Creates a SHA-256 hash of a Block
      :param block: <dict> Block
      :return: <str>
    """
    
    # we must make sure that the dictionary is ordered, or well have inconsistencies
    block_string = json.dumps(block, sort_keys = True).encode()
    return hashlib.sha256(block_string).hexdigest()

  #returns the last block in the chain
  @property
  def last_block(self):
    return self.chain[-1]



   def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
