#Author: Cecelia Williams
#Last Revision: 04.30.2017
#Description: Chapter 20 Exercise 3


""" Read a book from filename, and return a list of its words. """
infile = open('alice_in_wonderland.txt', 'r')
""" creating count dictionary """
word_count = {}

for line in infile:
    for word in line.split():
        word = word.lower()
        word = word.replace('_', '').replace('"', '').replace(',', '')
        word = word.replace('.', '').replace('-', '').replace('?', '')
        word = word.replace("'", "").replace('!', '').replace(';', '')
        word = word.replace('(', '').replace(')', '').replace(':', '')
        word = word.replace('[', '').replace(']', '').replace(' ', '')
        word = word.replace('0', '').replace('1', '').replace('2', '')
        word = word.replace('3', '').replace('4', '').replace('5', '')
        word = word.replace('6', '').replace('7', '').replace('8', '')
        word = word.replace('9', '').replace('*', '')
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
            
keys = list(word_count.keys())
keys.sort()
    
outfile = open('alice_words.txt','w')
outfile.write("Word" + "\t\t\t\t" + "Count" + "\n")
outfile.write("-------------------------------\n")
for word in keys:
    outfile.write(word + "\t\t\t\t" + str(word_count[word]))
    outfile.write('\n')

alice_count = word_count['alice']
print("Alice's name appeared " + str(alice_count) + " times in the story")
      
infile.close()
outfile.close()
 



      








