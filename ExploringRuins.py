'''https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/exploring-ruins/'''

s=input()
for i in range(len(s)):
    if i==0 and s[i]=='?':
        if s=='?':
            s='a'
        elif s[i+1] is not 'a':
            s='a'+s[1:]
            
        else:
            s='b'+s[1:]
            
    elif i==(len(s)-1) and s[i]=='?':
        if s[i-1] is not 'a':
            s=s[:len(s)-1]+'a'
            
        else:
            s=s[:len(s)-1]+'b'
            
    elif s[i]=='?':
        if s[i-1] is not 'a' and s[i+1] is not 'a':
            s=s[:i]+'a'+s[i+1:]
            
        else:
            s=s[:i]+'b'+s[i+1:]
            
            
print(s)
