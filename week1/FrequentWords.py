from PatternCount import PatternCount

def FrequentWords(text, k): # Ouput: all most frequent k-mers in Text
    #O(n² * k)
    frequentPattern = []
    patterns = []
    count = []
    n = len(text)

    for i in range(n - k + 1): #O(n)
        k_mer = text[i:i+k]
        patterns.append(k_mer)
        count.append(PatternCount(text,k_mer)) #O(n)
    #O(n²) time complexity
    
    max_count = max(count)

    for i in range(n - k + 1):
        if count[i] == max_count:
            frequentPattern.append(patterns[i])

    frequentPattern = list(set(frequentPattern)) #remove duplicates
    
    return frequentPattern, max_count

if __name__== "__main__":
    
    lines = open("data/dna2.txt").readlines()
    text, k = lines[0], int(lines[1])

    k_mer, frequency = FrequentWords(text, k)

    print(f"The most frequent k-mers (k = {k}) in genome: {k_mer}, \nFrequency: {frequency}")

    pass