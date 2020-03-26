from HammingDistance import HammingDistance
symbols = ["A", "C", "G", "T"]

def ImmediateNeighbors(pattern): #return list of patterns that are 1HD away from input
    neighbors = []
    n = len(pattern)
    string = list(pattern)
    
    neighbors.append(pattern)
    
    for i in range(n):
        symbol = string[i]
        
        for val in symbols:
            if val != symbol:
                string[i] = val
                neighbors.append("".join(string))
        string[i] = symbol
        
    return neighbors

def Suffix(pattern):
    u = list(pattern)
    
    return "".join(u[1:])

def FirstSymbol(pattern):
    u = list(pattern)
    
    return u[0]

def Neighbors(pattern, d): # return list of patterns that are "d" units away (or less) from the input string
    #the input will be in the returning list
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return symbols
    
    neighborhood = []
    suffix_neighbors =  Neighbors(Suffix(pattern), d)
    
    for elem in suffix_neighbors:
        if HammingDistance(Suffix(pattern), elem) < d:
            for base in symbols: 
               neighborhood.append(base + elem)
        else:
            neighborhood.append(FirstSymbol(pattern) + elem)
    
    return neighborhood
             
if __name__ == "__main__":
    
    #p = "TGTCAGAACGC"
    #print(ImmediateNeighbors(p))
    #print(p)
    #print(Suffix(p))
    p = "AAA"
    tmp = Neighbors(p, 1)
    
    #for elem in tmp:
    #    print(elem, end = ' ')
    print(tmp)
    
    pass