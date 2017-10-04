## SUM THE DIGITS OF A NUMBER

# WAY1:

def sum1(x):
    num = str(x)
    l = len(num)
    sum = 0
    for i in range(0,l):
        y = int(num[i])
        sum += y
    print(sum)
    
#WAY2:
    
def sum2(x):
    sum = 0
    while x>0:
        y = x % 10
        sum += y
        x = (x-y)/10
    print(int(sum))


x = int(input("Write a number: "))

sum1(x)
sum2(x)
