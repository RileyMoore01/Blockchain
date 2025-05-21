# creates an intital empty list (to store our blockchain) and another to store transactions
class Blockchain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []
