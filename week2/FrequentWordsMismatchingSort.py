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

#useful for d = 1 or 2 anf k up to 9
def FrequentWordsMismatchingSort(text, k, d):
    ##Output: All most frequent k-mers with up to d mismatches in text
    frequent_patterns = []
    neighborhood = []
    n = len(text)
    count = []
    index = []
    
    for i in range(n - k + 1):
        for elem in Neighbors(text[i:i+k], d):
            neighborhood.append(elem)
    
    #neighborhood = list(set(neighborhood))
    
    
    for i in range(len(neighborhood)):
        pattern = neighborhood[i]
        index.append(base4_to_base10(Pattern2Number(pattern)))
        #print(pattern)
        count.append(1)
    
    index.sort()
    
    for i in range(1, len(index)):
        if index[i] == index[i - 1]:
            count[i] = count[i - 1] + 1
    
    max_count = max(count)              
    
    for i in range(len(index)):
        if count[i] == max_count:
            pattern = Number2Pattern(index[i], k)
            frequent_patterns.append(pattern)
            
    return frequent_patterns

if __name__ == "__main__":
    #genome = "TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT"
    genome = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    d = 1
    print(FrequentWordsMismatchingSort(genome, k, d))

    pass