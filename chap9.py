'''9.1'''
#fin = open('words.txt')
#for line in fin:
#	word = line.strip()
#	if len(word) > 20:
#		print word

'''9.2'''
import string
def has_no_e():
C
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
        return True

#print avoid('bewdd', 'asf') 

def avoids():
    proa = 'Please type 5 forbidden letters in a row, e.g. bacon'
    a = raw_input(proa)
    fin = open('word.txt')
    for line in fin:
        word = line.strip()
        for letter in a:
                if letter in word:
                        return
        print word
                        
print avoids()

