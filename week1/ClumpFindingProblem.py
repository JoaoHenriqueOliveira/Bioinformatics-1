from FasterFrequentWords import FasterFrequentWords
from FindingFrequentWordsBySorting import FindingFrequentWordsBySorting

def ClumpFindingProblem(genome, k, L, t): #Output: All distinct k-mers forming (L, t)-clumps in Genome
    N = len(genome)
    res = []

    for i in range(N - L + 1):
        text = genome[i:i+L]
        patterns, frequency = FasterFrequentWords(text, k)
        #patterns, frequency = FindingFrequentWordsBySorting(text, k)
        
        if frequency >= t:
            for word in patterns:
                if not(word in res):
                    res.append(word)
            
    return res


if __name__ == "__main__":
    e_coli = open("data/e_coli.txt", "r") #Runtime is very big for e_coli! Try BetterClumpFinding
    dna = e_coli.readline()
    k = 9
    L = 500
    t = 4
    print(f"Size of DNA: {len(dna)}")
    
    res = ClumpFindingProblem(dna, k, L, t)
    
    for item in res:
        print(item, end = " ")
           
    pass

