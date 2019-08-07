# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.storage = [None]*capacity
        self.capacity = capacity
        self.count = 0


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    val = 5381
    for x in string:
        val = ((val << 5)+val)+ord(x)
    return val % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hashkey = hash(key, hash_table.capacity)
    if hash_table.storage[hashkey] == None:
        hash_table.storage[hashkey] = LinkedPair(key, value)
        hash_table.count += 1
    else:
        tmp = hash_table.storage[hashkey]
        if tmp.key == key:
            hash_table.storage[hashkey].value = value
            return None
        else:
            while tmp.next != None:
                tmp = tmp.next
                if tmp.key == key:
                    tmp.value = value
                    return None
        tmp.next = LinkedPair(key, value)
        hash_table.count += 1

    if hash_table.count >= 0.8 * hash_table.capacity:
        hash_table = hash_table_resize(hash_table)
    return None


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashkey = hash(key, hash_table.capacity)
    if hash_table.storage[hashkey] == None:
        print("WARNING! Deleting a key that does not exist")
        return None
    else:
        tmp = hash_table.storage[hashkey]
        if tmp.next != None:
            while tmp.next != None:
                if tmp.next.key == key:
                    tmp.next = tmp.next.next
                    hash_table.count -= 1
                    if hash_table.count >= 0.8 * hash_table.capacity:
                        hash_table = hash_table_resize(hash_table)
                    break
                tmp = tmp.next
        else:
            if tmp.key == key:
                hash_table.storage[hashkey] = None
                if hash_table.count >= 0.8 * hash_table.capacity:
                    hash_table = hash_table_resize(hash_table)
                return None
    return None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    address = hash(key, hash_table.capacity)
    if hash_table.storage[address] != None:
        tmp = hash_table.storage[address]
        while tmp != None:
            if tmp.key == key:
                return tmp.value
            tmp = tmp.next
    return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    # if hash_table.count <= 0.2*hash_table.capacity:
    #     new_ht = HashTable(hash_table.capacity//2)
    # elif hash_table.count >= 0.7*hash_table.capacity:
    new_ht = HashTable(hash_table.capacity*2)

    # if hash_table.count <= 0.2*hash_table.capacity or hash_table.count >= 0.7*hash_table.capacity:
    for i in range(hash_table.capacity):
        tmp = hash_table.storage[i]
        # if tmp != None:
        while tmp != None:
            hash_table_insert(new_ht, tmp.key, tmp.value)
            tmp = tmp.next
    hash_table = new_ht
    return hash_table


# def hash_table_resize(hash_table):
#     new_table = HashTable(2 * hash_table.capacity)
#     current_pair = None

#     for i in range(hash_table.capacity):
#         current_pair = hash_table.storage[i]
#         while current_pair is not None:
#             hash_table_insert(
#                 new_table, hash_table.storage[i].key, hash_table.storage[i].value)
#             current_pair = current_pair.next
#     hash_table = new_table
#     return hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
