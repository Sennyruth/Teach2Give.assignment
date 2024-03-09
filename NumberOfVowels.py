# Write a program that counts the number of vowels in a sentence.

Sentence = input("Enter a sentence: ")
string = Sentence.lower()
# print(string)
count = 0
list1 = ["a","e","i","o","u"]
for char in string:
    if char in list1:
        count = count+1
print("number of vowels is:",count)
