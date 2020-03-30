from MotifEnumeration import HammingDistance

def DistanceBetweenPatternAndString(pattern, dna): #Computes d(Pattern, Dna) = ∑t_i=1 d(Pattern, Dnai)
    k = len(pattern)
    n = len(dna[0])
    distance = 0
    
    for string in dna:
        hd = int(1e9)
        
        for i in range(n - k + 1):
            aux = HammingDistance(pattern, string[i:i + k])
            if hd > aux:
                hd = aux
        distance += hd
                
    return distance

if __name__ == "__main__":
    #dna = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]
    #pattern = "AAA"
    f = open("test.txt", "r").readlines()
    pattern = "".join(f[0][:-1])
    print(pattern)
    Dna = []
    tmp = []
    
    print(f[1])
    for base in f[1]:
        tmp.append(base)
        if base == " ":
            Dna.append("".join(tmp[:-1]))
            tmp = []
        
    print(Dna)
    print(DistanceBetweenPatternAndString(pattern, Dna))
    
    pass