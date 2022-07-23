# Date: 16.08.2020
import itertools

print('Program that gives you words (greater than 2) from your letters.\n')
# opens dictionary
file = open('dictionary.txt').read().lower() # dictionary for regular words
#file = open('words_alpha.txt').read() # gives more (insane) words

# collects input of letters from user, creates a list to store new words.
letters = input('Enter the letters (as one word): ').lower()
lst = []

# uses a library to find all permutations, uses a loop to select sub-words as new permutation is made
for i in itertools.permutations(letters):
    select = 3 # minumum number of words to find
    word = ''.join(i)

    for i in range(len(word)-1):
        sub_word = word[:select]
        select += 1
        check = ('\n' + sub_word + '\n')

        if (check in file) and (check[1:-1] not in lst): lst.append(check[1:-1])

# prints the list with the new words and sub-words in sorted order
print()
lst.sort()
print(lst)
input('\nPress Enter to exit...')
