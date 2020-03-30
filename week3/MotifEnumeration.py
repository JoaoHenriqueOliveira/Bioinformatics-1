symbols = ["A", "C", "G", "T"]

def HammingDistance(text1, text2):
    #Compute the Hamming distance between two strings.
    n = len(text1)
    if n != len(text2):
        print("Invalid input!")
        return -1
    d = 0
    
    for i in range(n):
        if text1[i] != text2[i]:
            d += 1
            
    return d

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

def ApproximatePatternCount(text, pattern, d): #Output: Count_{d}(Text, pattern)
    n = len(text)
    k = len(pattern)
    count = 0
    
    for i in range(n - k + 1):
        if HammingDistance(pattern, text[i:i+k]) <= d:
            count += 1
            
    return count

def MotifEnumeration(dna, k, d): #Exhaustif Search
    patterns = [] #Output: all (k, d)-motifs in dna
    N = len(dna) #number of strings in dna
    n = len(dna[0])
    
    for i in range(N):
        for l in range(n - k + 1):
            k_mer = dna[i][l:l + k]                
            neighborhood = Neighbors(k_mer, d) #list of k-mers that at at most d units appart from the subsequence of the dna.
            
            for elem in neighborhood:
                aux = True
                for j in range(N):
                    if ApproximatePatternCount(dna[j], elem, d) == 0:
                        aux = False
                if aux:
                    patterns.append(elem)
                    
    patterns = list(set(patterns))
    
    return patterns

def motif_enum(dna, k, d):
    patterns = []
    N = len(dna) #number of strings in dna
    n = len(dna[0])
    
    for i in range(n - k + 1):
        pattern = dna[0][i:i + k]
        nei = Neighbors(pattern, d)
        
        for elem in nei:
            aux = True
            for j in range(1, N):
                if ApproximatePatternCount(dna[j], elem, d) == 0:
                    aux = False
            if aux and len(elem) != 1:
                patterns.append(elem)
                
    patterns = list(set(patterns))
    
    return patterns

if __name__ == "__main__":
    dna = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
    k = 3
    d = 0
    res = MotifEnumeration(dna, k, d)
    res2 = motif_enum(dna, k, d)
    for val in res:
        print(val, end = " ")
    print()
    print(res2)
    pass