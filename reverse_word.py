sentense="i love my india"
words=sentense.split()
result=[]
for word in words:
    result.append(word[::-1])
print(" ".join(result))    