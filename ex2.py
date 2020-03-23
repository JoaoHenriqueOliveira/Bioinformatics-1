from ex1 import PatternCount

def FrequentWords(text, k):
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
    lines = open("dna2.txt").readlines()
    text, k = lines[0], int(lines[1])

    k_mer, frequency = FrequentWords(text, k)

    print("The most frequent words in genome: ", k_mer, f"\nFrequency: {frequency}")

    pass