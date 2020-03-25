from HammingDistance import HammingDistance

def ApproximatePatternMatching(pattern, text, d):
    n = len(text)
    k = len(pattern)
    res = [] #list of index where the distance is <= d
    
    for i in range(n - k + 1):
        if HammingDistance(pattern, text[i:i+k]) <= d:
            res.append(i)
            
    return res, len(res) #retorna a lista e o nº de aparições dessas approx words

if __name__ == "__main__":
    
    pattern = "CGGAC"
    text = "ACTAGCACAGGTATTCTAACTGAGCCCGGGACCATTATGGGAAGAGATGTACGAAGCTGTTTCTTAACTTTCTTTAAGTATTCACCTCCCGAGTTAGCCACTATCATAAGTTCGGGAATCACGTCCGGTCCGTAATATCCGTTGGTCAGATGCCTATGACCCTCGCTCCGACTTTGTCGGGATATATGGCTGATTATGACGGCTCAATGATTAGATGGAACAAGATTGAGTTCGCCTAAGGAATAGAGAAATCTCCGAACACGCAATAGCACATTCTTGAATCTAGTTTCCCAAATCTCAACCTTACGGACCCAAGCTCTATACAAACCACGGCAGGAGAGGACCTTTCGGCGGAAACGGGACCCTGGACCTCGAAGGACC"
    d = 3
    
    res, tmp = ApproximatePatternMatching(pattern, text, d)
    
    #for val in res:
    #   print(val, end = ' ')
    print(tmp)
    
    
    pass