from DistanceBetweenPatternAndString import DistanceBetweenPatternAndString

dic = {"A": "0", "C": "1", "G": "2", "T": "3"}

def get_key(val):
    
    for key, value in dic.items():
        if val == value:
            return key
    return "key doesn't exits!"

def base4_to_base10(nbr): #recebe string, retorna int
    #transforma o nº na base4 p/ o nº na base 10 
    n = len(nbr)
    result = 0
    
    for i in range(n):
        result += (4**i) * int(nbr[n-i-1])
        
    return result

def Pattern2Number(str): #transforma o patterns para o respectivo nº na base 4
    nbr = []
    
    for base in str:
        nbr.append(dic[base])
    
    return "".join(nbr) #return type is a string!

def Number2Pattern(nbr, k): # nbr -> base 10
    # Recebe o nº na base 10 e transforma para o pattern (string com A, C, G, T) de tamanho k 
    # que codifica o nº em analise
    
    nbr = int(nbr) 
    res = []
    
    while nbr != 0:
        base_number = str(nbr%4) #0, 1, 2, 3
        
        res.append(get_key(base_number))
        nbr = int(nbr/4)
    
    while len(res) < k:
        res.append('A')
            
    res.reverse()
    
    return ''.join(res)

def MedianString(dna, k): #Output: String with minimum distance to a given dna
    distance = int(1e10)
    cases = 4 ** k
    
    for i in range(cases):
        pattern = Number2Pattern(i, k)
        tmp = DistanceBetweenPatternAndString(pattern, dna)
        if distance > tmp:
            distance = tmp
            median = pattern
    
    return median

if __name__ == "__main__":
    k = 7
    dna = ["CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC","GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC","GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"]
    
    print(f"Median String: {MedianString(dna, k)}, k = {k}")
    
    pass