from ComputingFrequencies import Pattern2Number, base4_to_base10, Number2Pattern

def FindingFrequentWordsBySorting(text, k):
    #Calcula os paterns (words no genoma) mais frequentes de maneira eficiente
    #usa a função sort
    frequent_patterns = []
    n = len(text)
    index = []
    count = []
    
    for i in range(n - k + 1):
        pattern = text[i:i+k]
        nbr = base4_to_base10(Pattern2Number(pattern))
        index.append(nbr)
        count.append(1)
    
    index.sort() #Sort the index array
    
    for i in range(1, n - k + 1):
        if index[i] == index[i-1]:
            count[i] = count[i-1] + 1
        
    max_count = max(count)
    
    for i in range(n - k + 1):
        if count[i] == max_count:
            pattern = Number2Pattern(index[i], k)
            frequent_patterns.append(pattern)
            
    return frequent_patterns, max_count
        
if __name__ == "__main__":
    genome = "TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT"
    k = 3
    
    print(FindingFrequentWordsBySorting(genome, k))   
    pass