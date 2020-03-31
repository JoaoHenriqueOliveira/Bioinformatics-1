from skew import skew

def MinimumSkew(genome):
    #Find a position in a genome minimizing the skew.
    #Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).
    diff = skew(genome)
    aux = min(diff)
    positions = []

    for i in range(len(genome)):
        if diff[i+1] == aux:
            positions.append(i+1)
        
    return positions 

if __name__ == "__main__":
    file = open("data/test.txt").readlines()
    genome = file[0]
    vec = MinimumSkew(genome)
    
    for pos in vec:
        print(pos, end = ' ')
    print()
    
    pass

