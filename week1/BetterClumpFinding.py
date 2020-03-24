from ComputingFrequencies import ComputingFrequencies, Pattern2Number, base4_to_base10, Number2Pattern

def BetterClumpFinding(genome, k, L, t):
    N = len(genome)
    cases = 4 ** k
    frequent_patterns = []
    clump = [0 for i in range(cases)]
    
    text = genome[0:L]
    frequency_array = ComputingFrequencies(text, k)
    
    for i in range(cases):
        if frequency_array[i] >= t:
            clump[i] = 1
            
    for i in range(1, N - L + 1):
        first_pattern = genome[i - 1:i - 1 + k]
        index = base4_to_base10(Pattern2Number(first_pattern))
        frequency_array[index] -= 1
        
        last_pattern = genome[i + L - k:i + L]
        index = base4_to_base10(Pattern2Number(last_pattern))
        frequency_array[index] += 1
        
        if frequency_array[index] >= t:
            clump[index] = 1
            
    for i in range(cases):
        if clump[i] == 1:
            pattern = Number2Pattern(i, k)
            frequent_patterns.append(pattern)
            
    return frequent_patterns

if __name__ == "__main__":
    e_coli = open("e_coli.txt", "r")
    
    dna = e_coli.readline()
    k = 9
    L = 500
    t = 3
    print(len(dna))
    
    res = BetterClumpFinding(dna, k, L, t)
    print("********************")
    #print(ClumpFindingProblem(genome, k, L, t))
    test = open("test.txt", "w")
    
    for item in res:
        test.write(item + " ")
        
    test.close()
    e_coli.close()
    print(f"{k}-mers in E. coli genome: {len(res)}")
    print(0)
    pass