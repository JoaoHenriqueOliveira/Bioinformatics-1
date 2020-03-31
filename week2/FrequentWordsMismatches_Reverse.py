from HammingDistance import HammingDistance
from FrequentWordsWithMismatches import *
from Neighbors import Neighbors

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
    
if __name__ == "__main__":
    dna = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    d = 1
    p1 = FrequentWordsMismatches_Reverse(dna, k, d) #ACAT ATGT
    
    for tmp in p1:
        print(tmp, end = ' ')
    
    print()    
    pass   
    