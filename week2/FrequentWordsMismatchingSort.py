from Neighbors import *
from FrequentWordsWithMismatches import *

#useful for d = 1 or 2 anf k up to 9
def FrequentWordsMismatchingSort(text, k, d):
    #Output: All most frequent k-mers with up to d mismatches in text
    frequent_patterns = []
    neighborhood = []
    n = len(text)
    count = []
    index = []
    
    for i in range(n - k + 1):
        for elem in Neighbors(text[i:i+k], d):
            neighborhood.append(elem)
        
    for i in range(len(neighborhood)):
        pattern = neighborhood[i]
        index.append(base4_to_base10(Pattern2Number(pattern)))
        count.append(1)
    
    index.sort()
    
    for i in range(1, len(index)):
        if index[i] == index[i - 1]:
            count[i] = count[i - 1] + 1
    
    max_count = max(count)              
    
    for i in range(len(index)):
        if count[i] == max_count:
            pattern = Number2Pattern(index[i], k)
            frequent_patterns.append(pattern)
            
    return frequent_patterns

if __name__ == "__main__":
    genome = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    d = 1
    print(FrequentWordsMismatchingSort(genome, k, d))

    pass