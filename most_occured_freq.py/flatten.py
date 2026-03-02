lst=[1,2,1,2,3,4,5,3,4,5,6,7]
def freq(lst):
    freq={}
    for item in lst:
        if item in freq:
           freq[item]+=1
        else:
           freq[item]=1
    return freq       
lst=[1,2,1,2,3,4,5,3,4,5,6,7]      
print(freq(lst))

freq=freq(lst)
most_occured=max(freq,key=freq.get)
print(most_occured)
most_occured_freq=max(freq.values())
print(most_occured_freq)