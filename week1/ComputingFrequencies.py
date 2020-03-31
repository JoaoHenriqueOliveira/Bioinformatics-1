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

def ComputingFrequencies(genome, k):
    #Computes the frequency of each possible pattern (length k) in genome
    FrequencyArray = [0 for i in range(4**k)]
    N = len(genome)
    
    for i in range(N - k + 1):
        pattern = genome[i:i+k] #nº na base 4 e comprimento k
        number_4 = Pattern2Number(pattern) #string correspondente ao nº na base 4
        number_10 = base4_to_base10(number_4) #nº na base 10 correspondente ao pattern
        FrequencyArray[number_10] += 1 #incrementa a frequencia do respectivo pattern
    
    return FrequencyArray

if __name__ == "__main__":
    
    number_4 = Pattern2Number("TCCTAAAACAGGCACG")
    number_10 = base4_to_base10(number_4)
    
    print(f"Expected: 3113000010221012 --- Result:{number_4}") 
    print(f"Expected: 3607120454 --------- Result:{number_10}")
    print(f"Expected: TCCTAAAACAGGCACG --- Result:{Number2Pattern(3607120454, 16)}")
    
    pass