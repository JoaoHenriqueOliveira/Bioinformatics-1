def PatternMatchingProblem(pattern, genome):
    n, k = len(genome), len(pattern)
    res = []
    
    for i in range(n - k + 1):
        if genome[i:i+k] == pattern:
            res += str(i) + " "

    return "".join(res)

if __name__ == "__main__":
    
    pattern = "CTTGATCAT"

    with open("Vibrio_cholerae.txt") as file:
        data = file.read()
    
    result = open("pattern_genome.txt", "w")

    result.write(PatternMatchingProblem(pattern, data))
    pass