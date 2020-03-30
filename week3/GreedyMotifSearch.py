from Profile import *

def InitializeMotifs(dna, k): #Creates a motif matrix from the first pattern with each string in dna
    motifs = [string[0:k] for string in dna]

    return motifs

def GreedyMotifSearch(k, t, dna): #Find the best motif matrix by greedly constructing the profile matrix
    best_motifs = InitializeMotifs(dna, k)
    n = len(dna[0])
    
    for i in range(n - k + 1):
        candidates = []
        motif = dna[0][i:i + k]
        candidates.append(motif)
        curr_pofile = MakeProfile_Laplace(candidates)
        
        for j in range(1, t): #Greedy search through the next dna's given motif above
            next_motif = ProfileMostProbable(dna[j], k, curr_pofile)
            candidates.append(next_motif)
            #curr_pofile = MakeProfile(candidates)
            curr_pofile = MakeProfile_Laplace(candidates)
        
        if Score(candidates) < Score(best_motifs):
            best_motifs = candidates      
        
    return best_motifs

def test_InitializeMotifs():
    dna = ["GGCGTTCAGGCA","AAGAATCAGTCA","CAAGGAGTTCGC","CACGTCAATCAC","CAATAATATTCG"]
    k = 3
    
    print(InitializeMotifs(dna, k))
    pass

if __name__ == "__main__":
    lines = open("data/test.txt", "r").readlines()
    
    k = int(lines[0][0:2])
    t = int(lines[0][3:5])
    print(f"k = {k}, t = {t}")
    
    dna = [lines[i+1][:-1] for i in range(t)]
    
    output = GreedyMotifSearch(k,t, dna)
    
    print("k-mers in the Greedy Motif Matrix: ")
    
    for elem in output:
        print(elem, end = ' ')
    print()
    
    pass