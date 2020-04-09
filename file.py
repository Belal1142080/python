f=open('data','r')
print(f.readline())
f1=open("text",'a')

for data in f:
    f1.write(data)