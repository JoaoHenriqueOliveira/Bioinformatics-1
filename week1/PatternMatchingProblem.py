def PatternMatchingProblem(pattern, genome): #Output: A collection of space-separated integers specifying all starting positions where Pattern appears as a substring of Genome.
    n, k = len(genome), len(pattern)
    res = []
    
    for i in range(n - k + 1):
        if genome[i:i+k] == pattern:
            res += str(i) + " "

    return "".join(res)

if __name__ == "__main__":
    
    pattern = "CTTGATCAT"
    with open("data/Vibrio_cholerae.txt") as file:
        data = file.read()
    
    result = open("data/pattern_genome.txt", "w")

    result.write(PatternMatchingProblem(pattern, data))
    
    text = "AAACATAGGATCAAC"
    pattern = "AA"
    
    print(PatternMatchingProblem(pattern, text))
    pass