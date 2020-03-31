from HammingDistance import HammingDistance

#Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string

def ApproximatePatternMatching(pattern, text, d): #Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches
    # Find all approximate occurrences of a pattern in text
    #retorna as posições iniciais de cada padrão mais frequente.
    n = len(text)
    k = len(pattern)
    res = [] #list of index where the distance is <= d
    
    for i in range(n - k + 1):
        if HammingDistance(pattern, text[i:i+k]) <= d:
            res.append(i)
            
    return res 

if __name__ == "__main__":
    res = ApproximatePatternMatching("ATTCTGGA", "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT", d) # 6 7 26 27
    print(res)
        
    pass