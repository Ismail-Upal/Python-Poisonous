num=input()
num1=num[::-1]
f=0
for i,val in enumerate(num1):
    if val=='0' and f==0:
        continue
    else:
        f=1
        print(val, end="")

print()
if num==num1:
    print("YES")
else :
    print("NO")