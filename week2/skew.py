def skew(genoma, i = 0):
    #Difference between numbers of G and C in genoma (until position i, if i != 0. Otherwise will consider the whole genoma.
    c, g = 0, 0
    
    if i == 0:
        n = len(genoma)
        res = [ 0 for j in range(n+1)]
        c, g = 0, 0

        for j in range(n):
            if genoma[j] == "C":
                c += 1
            elif genoma[j] == "G":
                g += 1
            res[j+1] = g - c
        
        return res
    
    else:
        for j in range(i):
            if genoma[j] == "C":
                c += 1
            elif genoma[j] == "G":
                g += 1
    
        return g - c

if __name__ == "__main__":
    dna = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
    s = skew(dna)
    
    for elem in s:
        print(elem, end = " ")
    print()
    pass