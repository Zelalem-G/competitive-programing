k, n, w = map(int, input().split())

total = k * w * (w + 1) // 2

borrow = total - n

print(borrow if borrow > 0 else 0)
