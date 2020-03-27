def HammingDistance(text1, text2):
    #Compute the Hamming distance between two strings.
    n = len(text1)
    if n != len(text2):
        print("Invalid input!")
        return -1
    d = 0
    
    for i in range(n):
        if text1[i] != text2[i]:
            d += 1
            
    return d
    
if __name__ == "__main__":
    
    text1 = "CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA"
    text2 = "CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"
    
    print(HammingDistance(text1, text2))
    pass