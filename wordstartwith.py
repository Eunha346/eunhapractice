text=input()
letter=input()
a=[]
tmp=letter
cnt=1
bcnt=1
for i in text[1:]:
    tmp+=i
    cnt+=1
    if i==letter:
        a.append(tmp[:-1])
        tmp=i
        bcnt=cnt
a.append(text[bcnt-1:])
print(*a,sep='\n')
