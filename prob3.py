s='abcdezzetfvsidra'
curr=s[0]
long=s[0]

for c in s[1:]:
    if c>=curr[-1]:
        curr+=c

        if len(curr)>len(long):
            long=curr
    else:
        curr=c
print ("Longest substring in alphabetical order is:", long)









    
