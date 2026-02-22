s="madam"
result=""
for char in s:
    result=char+result
print(result)
if result==s:
    print("palindrome")
else:
    print("not palindrome") 