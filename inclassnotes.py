hash_table = [None] * 8

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
    
    return hash_value % len(hash_table)

def put(k, v):
    # for a given key, store a value in the hash table
    index = get_index(k)
    
    if hash_table[index] is not None:
        print("COLLISION")
    
    hash_table[index] = v

def get(k):
    # return the value from given key
    index = get_index(k)
    return hash_table[index]

def delete(k):
    index = get_index(k)
    hash_table[index] = None
    
    print("Item Deleted") 
    
    

# inserting
put("bobby", "hello, world")
put("ooops", "im a v")
put("ppppa", "more")
put("SpaceX", "SpaceX")
put("obbyb", "overide!!!!!!!!!!!!!")

# print all hash_data list
print(hash_table)
# get value by key
test = hash_function("papapa") # return the .encoded numbers
print(test)
          
