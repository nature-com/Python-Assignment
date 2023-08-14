file=open("textfile.txt",'w')
file.write("We are developers and developers are great")
file.close()

file=open("textfile.txt")
a=dict()
for text in file:
    words=text.split()
    for word in words:
        if word in a:
            a[word]=a[word]+1
        else:
            a[word]=1
        
print([a])

