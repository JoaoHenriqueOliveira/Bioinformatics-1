from Neighbors import *

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

def ComputingFrequenciesWithMismatches(text, k, d):
    frequency_array = [0 for i in range(4 ** k)]
    n = len(text)
    
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        neigborhood = Neighbors(pattern, d)
        
        for elem in neigborhood:
            j = base4_to_base10(Pattern2Number(elem))
            frequency_array[j] += 1
         
    return frequency_array

#uuseful for d = 1 or 2 anf k up to 9
def FrequentWordsWithMismatches(text, k, d):
    #Find the most frequent k-mers with mismatches in a string
    #Input: A string text as well as integers k and d
    #Output: All most frequent k-mers with up to d mismatches in text.
    frequency_array = ComputingFrequenciesWithMismatches(text, k, d)
    max_count = max(frequency_array)
    cases = 4 ** k
    res = []
    
    for i in range(cases):
        if frequency_array[i] == max_count:
            res.append(Number2Pattern(i, k))
    
    return res

if __name__ == "__main__":
    
    t = FrequentWordsWithMismatches("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)
    
    for item in t:
        print(item, end = ' ')
        
    print()
    #print(ComputingFrequenciesWithMismatches("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1))
    pass