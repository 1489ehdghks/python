money = 1260
count = 0 

array = [500,100,50,10]

for coin in array:
    count += money //coin 
    money %= coin
print(count)
