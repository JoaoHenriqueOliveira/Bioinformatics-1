from Profile import *

def InitializeMotifs(dna, k):
    motifs = []
    
    for string in dna:
        motifs.append(string[0:k])
    
    return motifs

def GreedyMotifSearch(k, t, dna): #Find the best motifs by greedly constructing the profile matrix
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
    #test_InitializeMotifs()
    
    #dna = ["GGCGTTCAGGCA","AAGAATCAGTCA","CAAGGAGTTCGC","CACGTCAATCAC","CAATAATATTCG"]
    lines = open("test.txt", "r").readlines()
    
    k = int(lines[0][0:2])
    t = int(lines[0][3:5])
    print(k,t)
    dna = []
    
    for i in range(t):
        dna.append(lines[i+1][:-1])
    
    output = GreedyMotifSearch(k,t, dna)
    
    for elem in output:
        print(elem, end = ' ')
    print()
    pass