n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
group = 0

for adventure in data:
    group += 1 
    if group >= adventure :
        result += 1
        count=0


print(result)



