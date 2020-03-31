def ComplementaryDNA(text):
    res = []
    pairs = {"A":"T", "C": "G", "T":"A", "G":"C"}

    for char in text:
        res += pairs[char]
    
    res.reverse()

    return "".join(res)

if __name__=="__main__":
    
    text = "GATTACA"
    res = ComplementaryDNA(text)

    print(res)
    pass