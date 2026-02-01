# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phone_book = {}

for _ in range(n):
    name, num = input().split()
    phone_book[name] = num  

while True:
    try:
        query = input().strip()
        if not query: 
            break
            
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
            
    except EOFError:
        break