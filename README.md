# stashCoin 


### `Cryptocurrency | BLOCKCHAIN | Python`

The objective is to create a cryptocurrency called the stashCoin, with blockchain and flask for web application.

# stashcoin.py
A blockchain is a time-stamped decentralized series of fixed records that contains data of any size is controlled by a large network of computers which are scattered around the globe and not owned by a single organization. Every block is secured and connected with each other using hashing technology which protects it from being tempered by an unauthorized person. 

### `Logic or the process in stashcoin.py`

The data will be stored in JSON format which is very easy to implement and easy to read. The data is stored in a block and the block contains multiple data. Each and every minute multiple block are added and to differentiate one from other we will use fingerprinting.

The fingerprinting is done by using hash and to be particular we will use the SHA256 hashing algorithm. Every block will contain its own hash and also the hash of the previous function so that it cannot get tampered.

This fingerprinting will be used to chain the blocks together. Every block will be attached to the previous block having its hash and to the next block by giving its hash.

The mining of the new block is done by giving the successfully finding the answer to the proof of work. To make mining hard the proof of work must be hard enough to get exploited.

After mining the block successfully the block will then be added to the chain.

After mining several blocks the validity of the chain must be checked in order to prevent any kind of tampering with the blockchain.

Then the web app will be made by using Flask and deployed locally or publicly as per the need of the user.

## [sauravDutt.in](https://sauravdutt.in/)

