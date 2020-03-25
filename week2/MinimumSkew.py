from week2.skew import skew

def MinimumSkew(genome):
    diff = skew(genome)
    aux = min(diff)
    positions = []

    for i in range(len(genome)):
        if diff[i+1] == aux:
            positions.append(i+1)
        
    return positions 

if __name__ == "__main__":
    
    file = open("test.txt").readlines()
    genome = file[0]
    vec = MinimumSkew(genome)
    
    for pos in vec:
        print(pos, end = ' ')
    print()
    pass

