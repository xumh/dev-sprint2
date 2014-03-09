import string

def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res = res + rotate_letter(letter, n)
    return res


print rotate_word('cheer', 7)

'''9.1'''
#fin = open('words.txt')
#for line in fin:
#   word = line.strip()
#   if len(word) > 20:
#       print word

'''9.2'''
import string
def has_no_e():
    fin = open('words.txt')
    ct = 0
    for line in fin:
        word = line.strip()
        if ('e' in word) == False:
            ct = ct + 1
            print word
    print (ct/113809.0)*100

#print has_no_e()

'''9.3'''
def avoid(word, letters):
    for char in letters:
        index = word.find(char)
        if index > -1:
            return
        return 'True'

#print avoid('word', 'asf') 

def avoids():
    proa = 'Please type 5 forbidden letters in a row, e.g. bacon'
    a = raw_input(proa)
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
    ''' for char in a:
            index = word.find(char)
            if index > -1:
                return
            return word
'''
        if avoid(word, a) == 'True':
            print word

print avoids()