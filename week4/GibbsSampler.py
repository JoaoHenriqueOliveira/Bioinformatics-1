from RandomizedMotifSearch import *
from random import choices

def Normalize(distribution):
    aux = 0
    for p in distribution:
        aux += p
        
    distribution = [x / aux for x in distribution]
    
    return distribution

def ProfileRandomGeneratedKmer(text, k, profile):
    n = len(text)
    distribution = []
    states = []
    
    for i in range(n - k + 1):
        states.append(i)
        pattern = text[i:i + k]
        distribution.append(CalculateProbability(pattern, profile))
       
    distribution = Normalize(distribution)
    index = choices(states, distribution)[0]
    k_mer = text[index:index + k]
    
    return k_mer

def GibbsSampler(dna, k, t, N):
    motifs = CreateRdmMotif(dna, k, t)
    best_motifs = motifs
    
    for j in range(N):
        i = randint(0, t-1)
        motifs_ = motifs[:i] + motifs[(i+1):]
        profile = MakeProfile(motifs_)
        motifs[i] = ProfileRandomGeneratedKmer(dna[i], k, profile)
        
        if Score(motifs) < Score(best_motifs):
            best_motifs = motifs
    
    return best_motifs

def Simulate_Gibbs(dna, k, t, N, iter):
    best_motifs = CreateRdmMotif(dna, k, t)
    best_score = int(1e9)
    
    for i in range(iter):
        motifs = GibbsSampler(dna, k, t, N)
        score = Score(motifs)
        if  score < best_score:
            best_motifs = motifs
            best_score = score
    
    return best_motifs

if __name__ == "__main__":
    #distribution = [.1,.2,.3]
    #print(Normalize(distribution))
    
    lines = open("gibbs.txt", "r").readlines()
    k = int(lines[0][0:2])
    t = int(lines[0][3:5])
    N = int(lines[0][6:10])
    print(k, t, N)
    dna = []
    for i in range(t):
        string = lines[i + 1][:-1]
        dna.append(string)
        
    res = Simulate_Gibbs(dna, k, t, N, 100)
    for elem in res:
        print(elem)
    print()
    print(Score(res))
    
    #k = 8
    #t = 5
    #N = 100
    #dna = ["CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA","GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG","TAGTACCGAGACCGAAAGAAGTATACAGGCGT","TAGATCAAGTTTCAGGTGCACGTCGGTGAACC","AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
    
    #print(Simulate_Gibbs(dna, k, t, N, 500))
    
    #solution = ["TCTCGGGG","CCAAGGTG","TACAGGCG","TTCAGGTG","TCCACGTG"]
    #print(Score(solution))
    
    #motif = CreateRdmMotif(dna, k, t)
    #print(motif)
    #profile = MakeProfile(motif)
    
    #print(ProfileRandomGeneratedKmer(dna[0], k, profile))
    
    
    
    pass