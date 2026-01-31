l = int(input())
word = input()

if l < 26:
    print("NO")
else:
    wordLower = word.lower()
    wordSet = set(wordLower)
    
    if len(wordSet) == 26:
        print("YES")
    else:
        print("NO")
        
    
    
