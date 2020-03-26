from HammingDistance import HammingDistance

def ApproximatePatternCount(text, pattern, d): #Output: Count_{d}(Text, pattern)
    n = len(text)
    k = len(pattern)
    count = 0
    
    for i in range(n - k + 1):
        if HammingDistance(pattern, text[i:i+k]) <= d:
            count += 1
            
    return count

if __name__ == "__main__":
    pattern = "GATCGATGC"
    text = "CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT"
    d = 3
    
    print(ApproximatePatternCount(text, pattern, d))
    pass