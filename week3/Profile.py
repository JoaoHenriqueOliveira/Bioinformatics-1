dic = {"A": 0, "C": 1, "G": 2, "T": 3}

def get_key(val):
    
    for key, value in dic.items():
        if val == value:
            return key
    return "key doesn't exits!"

def MakeProfile(motif): #Input: list of motifs -> Output: profile matrix
    t, k = len(motif), len(motif[0])
    profile = [[0 for i in range(k)] for i in range(4)]
    
    for j in range(k):
        for i in range(t):
            base = motif[i][j]
            profile[dic[base]][j] += 1.0 / t
    
    return profile

def MakeProfile_Laplace(motif):
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

def CalculateProbability(pattern, profile): #returns IP(pattern | profile)
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

def test_Laplacce():
    motif = ["ACTG", "ATTC", "CCTT"]    
    print(MakeProfile_Laplace(motif))
    pass

def Test_makeProfile():
    dna = ["CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC","GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC","GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"]
    for elem in MakeProfile(dna):
        print(elem)
    print()    
    pass

def test_frequent_nucleotide():
    motif = ["ACTG", "ATTC", "CCTT"]
    print(FrequentNucleotide(motif)) 
    pass

def test_score():
    motif = ["ACTG", "ATTC", "CCTT"]
    print(Score(motif))
    pass

if __name__ == "__main__":   
    file = open("data/profile.txt", "r").readlines()   
    text, k, profile = "".join(file[0][:-1]), int(file[1][:-1]), []
     
    print(f"text: {text[0:10]}...{text[-5:]}\nk = {k}")
    print("Profile:")
    
    for i in range(4):
        val = []
        x = ''
        for symbol in file[i + 2]:
            if symbol != " " and symbol != "\n":
                x += symbol   
            else:
                val.append(float("".join(x)))  
                x = '' 
        profile.append(val) 
    
    for line in profile:
        print(line)
    
    pattern = ProfileMostProbable(text, k, profile)
    print(f"Pattern Most Probable: {pattern}\n")
    print(f"Probability for this patterns given the profile: {CalculateProbability(pattern, profile)}")
    
    pass