from random import randint
dic = {"A": 0, "C": 1, "G": 2, "T": 3}

def get_key(val): #A method for finding the key of "dic" given a suitable value
    
    for key, value in dic.items():
        if val == value:
            return key
    return "key doesn't exits!"

def MakeProfile(motif, laplace = True): #Input: list of motifs -> Output: profile matrix
    if laplace: #uses pseudocount, ie sums a ones matrix and then normalize the probabilities (to avoid 0 or 1 as final values)
        t, k = len(motif), len(motif[0])
        cte = t + 4
        profile = [[1.0 for i in range(k)] for i in range(4)]
    
        for j in range(k):
            for i in range(t):
                base = motif[i][j]
                profile[dic[base]][j] += 1.0
    
        for i in range(4):
            for j in range(k):
                profile[i][j] = profile[i][j] / cte
    
        return profile
    else:    
        t, k = len(motif), len(motif[0])
        profile = [[0 for i in range(k)] for i in range(4)]
    
        for j in range(k):
            for i in range(t):
                base = motif[i][j]
                profile[dic[base]][j] += 1.0 / t
    
        return profile

def Score(motif): #Input: motif matrix -> Output: the score function for the given matrix
    score = 0 
    t, k = len(motif), len(motif[0])
    consensus = FrequentNucleotide(motif)
    
    for j in range(k):
        for i in range(t):
            if motif[i][j] != consensus[j]:
                score += 1
     
    return score

def FrequentNucleotide(motif): #Input: motif matrix -> Output: list of most frequent nuc
    consensus_string = []
    count = [0, 0, 0, 0]
    t, k = len(motif), len(motif[0])
    
    for j in range(k):
        for i in range(t):
            count[dic[motif[i][j]]] += 1
        
        max_count = max(count)
        
        for x in range(4):
            if count[x] == max_count:
                consensus_string.append(get_key(x))
                count[x] = 0
                max_count = -1
            else:
                count[x] = 0
                   
    return consensus_string

def CalculateProbability(pattern, profile): #Output: IP(pattern | profile)
    p = 1
    index = 0

    for base in pattern:
        x = profile[dic[base]][index]
        p *= x
        index += 1
        
    return p

def ProfileMostProbable(text, k, profile): #Find a Profile-most probable k-mer in a string
    #Input: A string Text, an integer k, and a 4 × k matrix Profile
    #Output: A Profile-most probable k-mer in Text
    probability = -1
    n = len(text)
    
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        aux = CalculateProbability(pattern, profile)    
        if aux > probability:
            probability = aux
            k_mer = pattern
    
    return k_mer

def Motifs(profile, k, dna): #finds the best motif that suits the given profile matrix
    motif = []
    
    for string in dna:
        motif.append(ProfileMostProbable(string, k, profile))
        
    return motif

def CreateRdmMotif(dna, k, t): #Creates random motif matrix for the given dna
    motif = []
    n = len(dna[0])
    
    for i in range(t):
        start = randint(0, n - k)
        k_mer = dna[i][start:start + k]
        motif.append(k_mer)
                
    return motif

def RandomizedMotifSearch(dna, k, t): #Iteratively computes the motif and profile matrixs until the Score function is smaller than a random one
    #Converges due to the biased estimation of the most frequent pattern
    #Output: motif matrix (the best set of k-mers the algorithm finds)
    best_motifs = CreateRdmMotif(dna, k, t)  
    motifs = best_motifs
    best_score = Score(best_motifs)
    
    while True:
        profile = MakeProfile(motifs)
        motifs = Motifs(profile, k, dna)
        
        score = Score(motifs)
        
        if score < best_score:
            best_score = score
            best_motifs = motifs
            
        else:
            return best_motifs
        
def Simulate(dna, k, t, iter): #Simulation for the RandomizedMotifSearch(dna, k, t) "iter" times
    best_motif = CreateRdmMotif(dna, k, t)
    best_score = int(1e9)
    
    for i in range(iter):
        motif = RandomizedMotifSearch(dna, k, t)
        score = Score(motif)
        if  score <= best_score:
            best_motif = motif
            best_score = score
    
    return best_motif

def test_create_random_motif():
    dna = ["ATGCT","AAATT", "GCTGA","ATGTG"]
    motif=CreateRdmMotif(dna, 3, 4)
    print(motif)
    print(MakeProfile(motif))
    pass

if __name__ == "__main__":
    lines = open("data/RandomizedMotifSearch.txt", "r").readlines()
    k = int(lines[0][0:2])
    t = int(lines[0][3:5])
    print(f"k = {k}, t = {t}")
    dna = []
    
    for i in range(t):
        string = lines[i + 1][:-1]
        dna.append(string)
        
    res = Simulate(dna, k, t, 1000)
    for elem in res:
        print(elem)
    print()
    
    print(Score(res))
    pass
