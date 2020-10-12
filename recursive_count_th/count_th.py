'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# a method
# def count_th(word):
#     counter = word.count('th')
#     return counter


# recursive method
def count_th(word):
    # base case - if string is empty
    if len(word) < 2: # if the length of the word is 0, then there is no word
        # print(f'{word}, length is {len(word)}, returning 0')
        return 0
    
    # recursive case
    # look at first 2 indcies: equal to 'th'?
    elif word[0:2] == 'th':
        # if true add a 1 (mimics a counter)
        # print(f'first letters {word[0:2]}, adding 1, and sending {word[1:]} to recurse')
        return 1 + count_th(word[1:])
    # keep the rest of the indices and recurse again
    else:
        # print(f'first letters {word[0:2]}, no addition, and sending {word[1:]} to recurse')
        return count_th(word[1:])







print(count_th('throw'))
