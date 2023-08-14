a=[]
b=[]
n=int(input("Enter the length of the array: "))

for i in range(n):
    num=int(input("Enter the number: "))
    a.append(num)
a.sort()
print(a)

for i in range(n):
    num=int(input("Enter the number: "))
    b.append(num)
b.sort()
print(b)

def equalarray(a,b,n):
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1

    for i in b:
        if i not in d or d[i]==0:
            return False
        else:
            d[i]=d[i]-1

    return True

result=equalarray(a,b,n)
print("Output: ",result)
