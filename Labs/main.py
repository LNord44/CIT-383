# program that accepts string, tests whether its a palindrome

word = input("Enter word to test if palindrome?")

revWord = word[::-1]
#splicing

if word == revWord:
    print("word is palindrome")
else:
    print("not palindrome")