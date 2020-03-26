from MinimumSkew import MinimumSkew

if __name__ == "__main__":
    lines = open("salmonella.txt", "r").readlines()
    genome = ''
    
    for line in lines:
        genome += line[:-1]
    
    print(MinimumSkew(genome))
    pass