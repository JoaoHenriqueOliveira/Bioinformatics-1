from FasterFrequentWords import FasterFrequentWords
from FindingFrequentWordsBySorting import FindingFrequentWordsBySorting

def ClumpFindingProblem(genome, k, L, t):
    N = len(genome)
    res = []

    for i in range(N - L + 1):
        text = genome[i:i+L]
        #patterns, frequency = FasterFrequentWords(text, k)
        patterns, frequency = FindingFrequentWordsBySorting(text, k)
        
        if frequency >= t:
            for word in patterns:
                if not(word in res):
                    res.append(word)
            
    return res


if __name__ == "__main__":
    e_coli = open("e_coli.txt", "r")
    
    dna = e_coli.readline()
    k = 9
    L = 500
    t = 4
    print(len(dna))
    
    res = ClumpFindingProblem(dna, k, L, t)
    #print(res)
    print("********************")
    #print(ClumpFindingProblem(genome, k, L, t))
    test = open("test.txt", "w")
    
    for item in res:
        print(item, end = " ")
        
    test.close()
    test.close()
        
    pass

