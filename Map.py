'''
Implement a map data structure via hash table per https://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html
'''

class HashTable:
    def __init__(self, size=11):
        self.size = size # It's recommended to have a prime number slot/data size
        # Set up two lists that corresponds the locations between the key and value pair
        self.slots = [None] * self.size # hold the key
        self.data = [None] * self.size # hodl the data values

    # Implement a hash function via linear remainder
    def hashFunction(self, key, size):
        return key % size
    
    # Implement rehash via linear probing collision resolution technique
    def rehash(self, hashValue, size):
        return (hashValue + 1) % size

    # put method for map
    def put(self, key, value):
        hashValue = self.hashFunction(key, self.size)
        # if slot is empty, save the key-value pair to the location
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = value
        else:
            # Update value if slot is already populated with the same key
            if self.slots[hashValue] == key:
                self.data[hashValue] = value
            # if slot is preoccupied with other key-value pair, rehash
            else:
                #tmpHash = hashValue
                while self.slots[hashValue] != None:
                    hashValue = self.rehash(hashValue, self.size)
                if self.slots[hashValue] == key:
                    self.data[hashValue] = value
                else:
                    self.slots[hashValue] = key
                    self.data[hashValue] = value

    # The get method calculates the hash value. If the key does not match, rehash
    def get(self, key):
        hashValue = self.hashFunction(key,self.size)
        if key == self.slots[hashValue]:
            return self.data[hashValue]
        else:
            while self.slots[hashValue] != key:
                newHash = self.rehash(hashValue, self.size)
                if newHash == hashValue:
                    return None
                else:
                    hashValue = newHash
            return self.data[hashValue]

    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key,data)

def testMap():
    H=HashTable()
    H[54]="cat"
    #print(H[54])
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print(H.slots)
    print(H.data)

if __name__ == "__main__":
    testMap()
            

    

            
        



