

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.storage = [None]*capacity
        self.capacity = capacity
        self.count = 0


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    val = 5381
    for x in string:
        val = ((val << 5)+val)+ord(x)
    return val % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    hashkey = hash(key, hash_table.capacity)
    if hash_table.storage[hashkey]:
        print("WARNING! Overwriting a key that exists")
        hash_table.storage[hashkey] = Pair(key, value)
    else:
        hash_table.storage[hashkey] = Pair(key, value)
        hash_table.count += 1


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashkey = hash(key, hash_table.capacity)
    if hash_table.storage[hashkey] == None:
        print("WARNING! Deleting a key that does not exist")
        return
    hash_table.storage[hashkey] = None
    hash_table.count -= 1


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    address = hash(key, hash_table.capacity)
    if hash_table.storage[address] == None:
        return None
    else:
        return hash_table.storage[address].value


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
