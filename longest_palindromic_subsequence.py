def palindrome(s,i,sub,l):
	if i==len(s):
		if len(sub)!=0 and sub==sub[::-1]:
			l.append([len(sub),sub])
	else:
		palindrome(s,i+1,sub,l)
		palindrome(s,i+1,sub+s[i],l)
	return l
 
s=input()
l=[]
palindrome(s,0,"",l)
l.sort(reverse=True)
print(l[0][1])
