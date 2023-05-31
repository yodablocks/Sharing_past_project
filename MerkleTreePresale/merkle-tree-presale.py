import hashlib
from web3 import Web3

# Generate a Merkle tree from participant addresses and token allocations
def generate_merkle_tree(participants):
    leaves = [hash_address_and_allocation(address, allocation) for address, allocation in participants]
    tree = construct_tree(leaves)
    root_hash = tree[0]
    return root_hash, tree

# Hash the participant's address and allocation
def hash_address_and_allocation(address, allocation):
    hash_input = address + str(allocation)
    return hashlib.sha256(hash_input.encode()).hexdigest()

# Construct the Merkle tree
def construct_tree(leaves):
    if len(leaves) == 1:
        return leaves

    if len(leaves) % 2 != 0:
        leaves.append(leaves[-1])  # Duplicate the last leaf if the number of leaves is odd

    tree = []
    for i in range(0, len(leaves), 2):
        combined_hash = hashlib.sha256((leaves[i] + leaves[i+1]).encode()).hexdigest()
        tree.append(combined_hash)

    return construct_tree(tree)

# Verify a participant's eligibility and allocation
def verify_participant(participant_address, allocation, merkle_proof, root_hash):
    computed_hash = hash_address_and_allocation(participant_address, allocation)
    for proof in merkle_proof:
        if participant_address.lower() < proof[1].lower():
            computed_hash = hashlib.sha256((computed_hash + proof[1]).encode()).hexdigest()
        else:
            computed_hash = hashlib.sha256((proof[1] + computed_hash).encode()).hexdigest()

    return computed_hash.lower() == root_hash.lower()

# Example usage
participants = [
    ('0xaddress1', 100),
    ('0xaddress2', 200),
    ('0xaddress3', 150),
    ('0xaddress4', 75)
]

root_hash, tree = generate_merkle_tree(participants)
print("Root Hash:", root_hash)
print("Tree:", tree)

participant_address = '0xaddress2'
allocation = 200
merkle_proof = [('0xproof1', 'left'), ('0xproof2', 'right')]
is_verified = verify_participant(participant_address, allocation, merkle_proof, root_hash)
print("Participant Verification Result:", is_verified)
