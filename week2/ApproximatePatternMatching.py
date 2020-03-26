from HammingDistance import HammingDistance

def ApproximatePatternMatching(pattern, text, d):
    # Find all approximate occurrences of a pattern in text
    #retorna as posições iniciais de cada padrão mais frequente.
    n = len(text)
    k = len(pattern)
    res = [] #list of index where the distance is <= d
    
    for i in range(n - k + 1):
        if HammingDistance(pattern, text[i:i+k]) <= d:
            res.append(i)
            
    return res # All starting positions where Pattern appears as a substring of Text with at most d mismatches

if __name__ == "__main__":
    
    pattern = "CGGAC"
    text = "ACTAGCACAGGTATTCTAACTGAGCCCGGGACCATTATGGGAAGAGATGTACGAAGCTGTTTCTTAACTTTCTTTAAGTATTCACCTCCCGAGTTAGCCACTATCATAAGTTCGGGAATCACGTCCGGTCCGTAATATCCGTTGGTCAGATGCCTATGACCCTCGCTCCGACTTTGTCGGGATATATGGCTGATTATGACGGCTCAATGATTAGATGGAACAAGATTGAGTTCGCCTAAGGAATAGAGAAATCTCCGAACACGCAATAGCACATTCTTGAATCTAGTTTCCCAAATCTCAACCTTACGGACCCAAGCTCTATACAAACCACGGCAGGAGAGGACCTTTCGGCGGAAACGGGACCCTGGACCTCGAAGGACC"
    d = 3
    
    res = ApproximatePatternMatching("ATTCTGGA", "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT", d)
    
    #for val in res:
    #   print(val, end = ' ')
    print(res)
        
    pass