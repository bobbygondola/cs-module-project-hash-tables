hash_data = [None] * 8

def hash_function(s):
    #take input.. return bytes size
    bytes_list = s.encode()
    
    total = 0
    
    for b in bytes_list:
        total += b
        # optional but correct 
        total &= 0xffffffff # 32 bit ( 8 f's )
    
    return total

def get_index(s):
    hash_value = hash_function(s)
    
    return hash_value % 8

def put(k, v):
    # for a given key, store a value in the hash table
    index = get_index(k)
    hash_data[index] = v

def get(k):
    # return the value from given key
    index = get_index(k)
    return hash_data[index]
    
# inserting
put("bobby", "hello, world")
put("jerk", 90210)


# print all hashdata
print(hash_data)
# get value by key
print(get("bobby"))
print(get("jerk"))
