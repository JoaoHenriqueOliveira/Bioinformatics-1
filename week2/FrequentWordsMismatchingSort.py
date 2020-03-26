from Neighbors import *
from FrequentWordsWithMismatches import *

def FrequentWordsMismatchingSort(text, k, d):
    frequent_patterns = []
    neighborhood = []
    n = len(text)
    count = []
    index = []
    
    for i in range(n - k + 1):
        neighborhood.append(Neighbors(text[i:i+k], d))
    
    k = len(neighborhood)
    
    for i in range(k):
        pattern = neighborhood[i][0]
        #for elem in pattern:
        index.append(base4_to_base10(Pattern2Number(pattern)))
        count.append(1)
    
    index.sort() 
    
    for i in range(k - 2):
        if index[i] == index[i+1]:
            count[i+1] = count[i] + 1
    
    max_count = max(count)              
    
    for i in range(k - 1):
        if count[i] == max_count:
            pattern = Number2Pattern(index[i], k)
            frequent_patterns.append(pattern)
            
    return frequent_patterns

if __name__ == "__main__":
    #genome = "TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT"
    genome = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    d = 1
    print(FrequentWordsMismatchingSort(genome, k, d))
    pass