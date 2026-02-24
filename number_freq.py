lst=[1,2,3,4,5,6,7,8,1,2,3,4,5,6]
freq={}
for item in lst:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1
print(freq)            


s="ramanareddy"
freq={}
for item in s:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1

sorted_freq=dict(sorted(freq.items()))        
print(sorted_freq)            