s="tata consultancy services limited"
l=len(s)

i=1
count=0
while i<l:
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        count=count+1
    i=i+1
	
print(count)


s="tata consultancy services limited"
i=1
count=0
for i in range(l):
	if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
		count=count+1
print(count)


a=68.3
if a>=90:
	print("Distinct")
elif a>=60 and a<90:
	print("Above average")
elif a>=40 and a<60:
	print("Average")
else:
	print("Fail")