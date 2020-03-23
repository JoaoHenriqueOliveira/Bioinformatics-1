def count_var():
    lines = open("dna.txt").readlines()
    f , var = lines[0], lines[1]
    wdw = len(var)
    count = 0

    for i in range(len(f) - wdw + 1):
        if f[i:i+wdw] == var:
            count += 1

    return var, count

print(count_var())
    

    

