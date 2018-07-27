# n la so canh
n=int(input("Dien so canh (tu 4 tro len): ")) 

# j la khoang cach cac chu
j=1 
if n<5:
    j=1
else:
    j=(n//5)*j

# hien thi chu:
for row in range (n):
    for col in range (n*4+j*3):
        if (col==0 or ((row==0 or row==n-1) and (0<col<n)))   or  ((col==n+j or col==2*n+j-1) and (row!=0 and row!=n-1)) or ((row==0 or row==n-1) and (col>n+j and col<2*n+j-1))    or   ((col==2*n+2*j) or (col==3*n+2*j-1 and (row!=0 and row!=n-1)) or ((row==0 or row==n-1) and (col>2*n+2*j and col<3*n+2*j-1)))   or   (col==3*n+3*j or ((row==0 or row==(n-1)//2 or row==n-1) and col>3*n+3*j)):
            print("*",end="")
        else:
            print(end=" ")
    print()