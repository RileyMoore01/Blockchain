# creates an intital empty list (to store our blockchain) and another to store transactions
class Blockchain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []

  def new_block(self):
    pass # creates a new block and adds it to the chain

  def new_transaction(self):
    pass # add a new transaction to the list of transactions

  @staticmethod
  def hash(self):
    pass #hashes a block
