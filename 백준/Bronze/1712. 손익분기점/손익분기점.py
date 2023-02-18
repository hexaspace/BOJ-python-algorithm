fixed, change, price = map(int, input().split())
# fixed + change*x < price * x
if(price <= change):
    print('-1')    
else:
    x = fixed // (price - change)
    print(x+1)