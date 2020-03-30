from RandomizedMotifSearch import *
from random import choices

def Normalize(distribution): #Normalizes a given distribution vector of probabilities
    aux = 0
    for p in distribution:
        aux += p
        
    distribution = [x / aux for x in distribution]
    
    return distribution

def ProfileRandomGeneratedKmer(text, k, profile): #Outputs the most probable k-mer in text given a profile matrix 
    #(by simulating with a distribution derived from profile itself -> the output is biased)
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

def GibbsSampler(dna, k, t, N): #Outputs the motif matrix by updating a random generated profile matrix. -> 
    #-> each line is calculated by the profile generatd by the others and so on. (*)
    motifs = CreateRdmMotif(dna, k, t)
    best_motifs = motifs
    
    for j in range(N):
        i = randint(0, t-1) #Random select one line to updated
        motifs_ = motifs[:i] + motifs[(i+1):]
        profile = MakeProfile(motifs_) #Calculate the corresponding profile for the other lines
        motifs[i] = ProfileRandomGeneratedKmer(dna[i], k, profile) #(*) select the k-mer in the line selected with he distribution of the previous profile
        
        if Score(motifs) < Score(best_motifs):
            best_motifs = motifs
    
    return best_motifs

def Simulate_Gibbs(dna, k, t, N, iter): #Simulates the GibbsSampler iter times. -> Outputs the best result found
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
    
    lines = open("data/gibbs.txt", "r").readlines()
    k = int(lines[0][0:2])
    t = int(lines[0][3:5])
    N = int(lines[0][6:10])
    print(f"k = {k}, t = {t}, N = {N}")
    dna = []
    for i in range(t):
        string = lines[i + 1][:-1]
        dna.append(string)
        
    res = Simulate_Gibbs(dna, k, t, N, 100)
    
    for elem in res:
        print(elem, end = ' ')
    print()
    print(f"The score value for the solution found is: {Score(res)}")
    
    #k, t, N  = 8, 5, 100
    #dna = ["CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA","GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG","TAGTACCGAGACCGAAAGAAGTATACAGGCGT","TAGATCAAGTTTCAGGTGCACGTCGGTGAACC","AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
    #print(Simulate_Gibbs(dna, k, t, N, 500)) 
    
    pass