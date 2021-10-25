''' sequence of words as input and prints the words in
a sequence after sorting them alphabetically. '''

sentence = input("Enter the sentence ")

word = sentence.split()
print(word)

#sort the word in ascending order
word.sort()
print(word)
