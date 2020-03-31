from MinimumSkew import MinimumSkew
from FrequentWordsMismatches_Reverse import FrequentWordsMismatches_Reverse

if __name__ == "__main__":
    lines = open("data/salmonella.txt", "r").readlines()
    genome = ''
    
    for line in lines:
        genome += line[:-1]
    
    locations = MinimumSkew(genome)
    
    print(locations)
    L = 2000
    d = 2
    print(f"L = {L}, d = {d}")
    for index in locations:
        text = genome[index - L:index + L]
        print(FrequentWordsMismatches_Reverse(text, 9, d))
    
    print()
    pass