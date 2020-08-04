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
    
    return hash_value % len(hash_data)

def put(k, v):
    # for a given key, store a value in the hash table
    index = get_index(k)
    
    if hash_data[index] is not None:
        print("COLLISION")
    
    hash_data[index] = v
    
    

def get(k):
    # return the value from given key
    index = get_index(k)
    return hash_data[index]

def delete(k):
    index = get_index(k)
    hash_data[index] = None
    
    print("Item Deleted")
    
    

# inserting
put("bobby", "hello, world")
put("ooops", "chicek")
put("ppppa", "yerp")
put("SpaceX", "SpaceX")
put("obbyb", "overide!!!!!!!!!!!!!")

# print all hash_data list
print(hash_data)
# get value by key
print(get("bobby"))
