s = input("Enter a string: ")
count = 0
vowels = set("aeiouAEIOU")
for char in s:
    if char in vowels:
        count += 1
print("vowels:", count)
        
