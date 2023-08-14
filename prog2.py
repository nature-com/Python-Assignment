a=[]
n=int(input("Enter the length of the array: "))

for i in range(n-1):
    num=int(input("Enter the number: "))
    a.append(num)
print(a)

def missnum(a,n):
    esum=n*(n+1)/2
    asum=sum(a)
    return esum-asum

missingnum=missnum(a,n)
print("The missing number is: ",int(missingnum))