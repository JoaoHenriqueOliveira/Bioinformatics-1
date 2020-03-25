from week2.ApproximatePatternCount import *
from week2.HammingDistance import HammingDistance

def ComplementaryDNA(text):
    res = []
    pairs = {"A":"T", "C": "G", "T":"A", "G":"C"}

    for char in text:
        res += pairs[char]
    
    res.reverse()

    return "".join(res)

def FrequentWordsMismatches_Reverse(text, k, d):
    n = len(text)
    res1 = []
    res2 = []
    cases = 4 ** k
    all_cases = [0 for i in range(cases)]
    
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        index = base4_to_base10(Pattern2Number(pattern))
        
        pattern_rc = ComplementaryDNA(pattern)
        count1 = ApproximatePatternCount(text, pattern, d)
        count2 =  ApproximatePatternCount(text, pattern_rc, d)
        all_cases[index] = count1 + count2
        
    max_count = max(all_cases)
    
    for i in range(cases):
        if all_cases[i] == max_count:
            pattern = Number2Pattern(i, k)
            pattern_rc = ComplementaryDNA(pattern)
            res1.append(pattern)
            res2.append(pattern_rc)
    
    return res1, res2

if __name__ == "__main__":
    dna = "CTGCGCGAGCGTGTGCGGTCTGCGCGCGAGTCTGCGGCGGCGGTCTGTGCGTCGAGCCTGCGCTGTCTCGAGCGCGACTGTCGAGCGCCTGTGCGTCGACGAGTGTGTCGAGTGTGTGCCTGTCGACGAGCGGTGCGCTCTGCGGTCGAGCCGAGCGGCCTGCGGCGCGACGAGCCTGTGTGTGCGCGAGCGCTGTCTGCGTGCGGCCT"
    k = 7
    d = 2
    p1 , p2 = FrequentWordsMismatches_Reverse(dna, k, d)
    #print(FrequentWordsMismatches_Reverse(dna, k, d))
    
    for i in range(len(p1)):
        print(p1[i]+" "+p2[i], end = ' ')
        
    print(len(p1))    
    pass   
    