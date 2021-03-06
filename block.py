import time
from crypto_hash import crypto_hash

class Block:

#Block module
    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
         return (
             'Block('
              f'timestamp: {self.timestamp}, '
              f'last_hash: {self.last_hash}, '
              f'hash: {self.hash}, '
              f'data: {self.data})'
         )

    
       
       
    @staticmethod

    def mine_block(last_block, data):
      #mine block based on the last_block and data.
      timestamp = time.time()
      last_hash = last_block.hash
      hash = crypto_hash(timestamp, last_hash, data)
      return Block(timestamp, last_hash, hash, data)


  
  
  
  #generating genesis block.
    @staticmethod
    def genesis():
      return Block(1, 'genesis_last_hash', 'genesis_hash', [])

def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'slurp')
    print(block)


if __name__ == '__main__':
    main()