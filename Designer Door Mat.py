n,m=map(int,input().split(' '))
width=m
for i in range(0,n-1):
    if(i%2==0):
        print(('.|.'*(i+1)).center(width,"-"))
print("WELCOME".center(width,"-"))
for i in range(0,n-1):
    if(i%2==0):
        print(('.|.'*(n-2-i)).center(width,"-"))