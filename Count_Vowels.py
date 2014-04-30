#!usr/bin/python
#Count Vowels - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.
print "This program counts the number of vowels in a text and reports the number of each vowel found."
print "Note that 'y' is not considered a vowel."
string = raw_input("Enter a string: ")
#vowels = ['a', 'e', 'i', 'o', 'u']
s = string.lower()
a = s.count('a')
e = s.count('e')
i = s.count('i')
o = s.count('o')
u = s.count('u')
print "There are " + str(a+e+i+o+u) + " vowels."
print str(a) + " of them are a's."
print str(e) + " of them are e's."
print str(i) + " of them are i's."
print str(o) + " of them are o's."
print str(u) + " of them are u's."