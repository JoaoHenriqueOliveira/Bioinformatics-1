def PatternCount(text, pattern):
    wdw = len(pattern)
    count = 0

    for i in range(len(text) - wdw + 1):
        if text[i:i+wdw] == pattern:
            count += 1

    return count


if __name__ == "__main__":
    
    #lines = open("dna.txt").readlines()
    #text , pattern = lines[0], lines[1]
    pattern = "AAA"
    text = "GACCATCAAAACTGATAAACTACTTAAAAATCAGT"
    print(f"Pattern: {pattern} Frequency:", PatternCount(text, pattern))

    pass
