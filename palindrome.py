#Palindrome
word=input('enter a word: ')
reverse=word[::-1]
if word==reverse:
    print('Palindrome')
else:
    print('not palindrome')
