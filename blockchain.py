import hashlib
import datetime as date

#creating the block class
#defining the structure of each block in the blockchain

class Block:
    def __init__(self,index,timestamp,data,previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_string = str(self.index) + str(self.timestamp) +str(self.data)+str(self.previous_hash)
        return hashlib.blake2b(hash_string.encode()).hexdigest()
    

#creating the blockchain class
#list of blocks in theblockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0,date.datetime.now(),"Genesis Block","0")

    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self,new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1,len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.hash:
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
            
        return True
    #testing the blockchain

    #create the block chainblockchain = Blockchain()

    #add blocks to the blockchain
    # Create the blockchain
blockchain = Blockchain()

s = "Nanda"
for i in range(1,len(s)+1):

    # Add blocks to the blockchain
    blockchain.add_block(Block(i, date.datetime.now(), "Transaction Data 1", ""))
    #blockchain.add_block(Block(2, date.datetime.now(), "Transaction Data 2", ""))
    #blockchain.add_block(Block(3, date.datetime.now(), "Transaction Data 3", ""))

    # Print the contents of the blockchain
    for block in blockchain.chain:
        print("Block #" + str(block.index))
        print("Timestamp: " + str(block.timestamp))
        print("Data: " + block.data)
        print("Hash: " + block.hash)
        print("Previous Hash: " + block.previous_hash)
        print("\n")