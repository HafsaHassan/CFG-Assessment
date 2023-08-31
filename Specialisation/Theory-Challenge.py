# 3.1

# Defining hash function
def basic_hash(input_str, table_size):
    hash_code = hash(input_str)
    index = hash_code % table_size
    return index

# If a collision was to occur, a list could be used to create key-value pairs as the same index
# in the hash table. Each index of the hash tabe will be stored as a list of the key value pairs.

# 3.2

# If a collision was to occur, the basic hash table would map both strings to the same index
# in the hash table. A technique called chaining can be used to handle this. This would enable
# each index in the basic hash table to be associated with a list so multiple key value pairs
# can be held. To avoid the collision, append/add the new key value pair to the list at the correct
# index. For example, if we hash 2 keys into a hash table with a size of 5 and a collision
# was to occure, we could store them in a list at the right index in the hash table.

# 1. Define hash function (using function above)
# 2. Using the hash function, if two different strings are used (with different lengths),
# then there will be no hash collision.

# 3.3

# An example of a hash collision would be two different strings inserted that result in
# in the same hash index. E.g. "Apple" and "elppa".
# As mentioned previously, chaining would be used to elimiate hash collisions.
#
#
#
