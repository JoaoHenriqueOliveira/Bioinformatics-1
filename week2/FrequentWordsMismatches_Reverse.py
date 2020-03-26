from HammingDistance import HammingDistance
from ApproximatePatternCount import *
from Neighbors import Neighbors

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

def ComplementaryDNA(text):
    res = []
    pairs = {"A":"T", "C": "G", "T":"A", "G":"C"}

    for char in text:
        res += pairs[char]
    
    res.reverse()

    return "".join(res)

def FrequentWordsMismatches_Reverse(text, k, d):
    n = len(text)
    all_cases = [0 for i in range(4 ** k)]
    res = []
    
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        pattern_rc = ComplementaryDNA(pattern)
        nei_pat = Neighbors(pattern, d)
        nei_pat_rc = Neighbors(pattern_rc, d)
        for elem1 in nei_pat:
            nbr = base4_to_base10(Pattern2Number(elem1))
            all_cases[nbr] += 1
        for elem in nei_pat_rc:
            nbr = base4_to_base10(Pattern2Number(elem))
            all_cases[nbr] += 1
    
    max_count = max(all_cases)
    
    for i in range(4 ** k):
        if all_cases[i] == max_count:
            pattern = Number2Pattern(i, k)
            pattern_rc = ComplementaryDNA(pattern)
            res.append(pattern)
            res.append(pattern_rc)
            i_rc = base4_to_base10(Pattern2Number(pattern_rc))
            
            if i_rc != i and all_cases[i_rc] == max_count:
                all_cases[i_rc] = -1
            
    return res
    
def FrequentWordsMismathComplement(text, k, d):
    n = len(text)
    
    
    pass
if __name__ == "__main__":
    dna = "CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT"
    #dna = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 9
    d = 3
    p1 = FrequentWordsMismatches_Reverse(dna, k, d)
    #print(FrequentWordsMismatches_Reverse(dna, k, d))
    
    for tmp in p1:
        print(tmp, end = ' ')
    
    print()    
    pass   
    