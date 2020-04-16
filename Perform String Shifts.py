shift=[[1,1],[1,1],[0,2],[1,3]]
s="abc"
s=list(s)
for i in range(len(shift)):
    d=shift[i][0]
    val=shift[i][1]

    if d==0:
        for j in range(len(s)):
            ele=s[j]
            num1=ord(ele)
            new_num1=num1+val
            s[j]=chr(new_num1)
    elif d==1:
        for j in range(len(s)):
            ele=s[j]
            num1=ord(ele)
            new_num1=num1-val
            s[j]=chr(new_num1)

print(str(s))