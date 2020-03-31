from ComputingFrequencies import ComputingFrequencies, Number2Pattern

def FasterFrequentWords(genome, k): #Calculate the most frequent k-mers in genome
    #Calcula os paterns (words no genoma) mais frequentes de maneira eficiente    
    frequent_patterns = []
    frequency_array = ComputingFrequencies(genome, k)
    
    max_count = max(frequency_array)
    
    for i in range(len(frequency_array)):
        if frequency_array[i] == max_count:
            pattern = Number2Pattern(i, k)
            frequent_patterns.append(pattern)
            
    return frequent_patterns, max_count


if __name__ == "__main__":
    genome = "TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT"
    k = 3
    
    print(FasterFrequentWords(genome, k))    
    
    pass