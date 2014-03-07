#The Encryption python file.



#5 keys that can be used to encrypt messages.

blowtorch = ['%', '5', 'D', '6', 'G', 'h', '^', 'z', '&', 'p', ':', 'S', ' ', 'T', '8', ')', ']', 'P', ';', '4', 'b', ',', 'o', 'd', '7', 'r', 'g', '{', 'E', '`', 'c', 'H', '(', 'Z', '3', 'B', 'M', '+', '|', 'F', 'V', '#', 'J', 'n', '=', '$', 'N', '-', 'X', '@', '0', '"', '[', 'v', 'e', '}', 'q', 'W', 'I', 'a', 'K', 'U', '2', '/', 'Y', 'A', 'y', '~', '?', '<', 'R', 'w', 'm', '_', '9', 'x', 'i', 'O', 'L', 'Q', 's', 'u', 'j', 'C', '*', '>', '!', 'f', 't', "'", 'l', '.', 'k', '1']

clownfish = ['p', 't', '3', 'v', 'K', '/', 'Y', ']', 'g', 'b', 'm', '-', 'r', '`', 's', 'i', ':', '5', 'M', 'a', 'Z', 'o', 'P', '?', '[', 'N', '8', ' ', 'U', '~', 'A', '*', '=', '2', 'O', 'G', ',', 'H', '1', '&', 'x', 'Q', 'n', '#', 'l', 'q', 'h', ';', 'R', 'c', "'", '^', 'E', 'u', '{', '4', '0', '6', '+', '@', ')', '"', '}', '%', 'y', 'e', 'w', '$', '(', 'z', 'S', 'd', 'T', 'W', '>', '7', 'F', 'k', '_', 'J', 'j', 'V', 'X', '|', '.', 'f', '!', 'D', 'C', 'I', 'B', '9', '<', 'L']

legomovie = ['t', 'v', '4', 'K', 'E', ']', ':', 'f', 'D', '&', 'o', '_', '{', '}', 'W', 'L', 's', 'l', 'k', '.', '<', 'u', 'P', 'Q', 'M', '6', ';', '=', '0', 'N', 'I', '%', 'B', '`', 'U', '@', '!', ',', ' ', 'w', '2', 'F', '^', 'p', '|', '~', 'q', 'c', '>', 'g', 'H', '3', 'b', '(', 'a', 'S', 'n', '-', 'R', '*', '9', 'Z', 'C', 'z', 'Y', '1', 'A', ')', 'y', 'x', 'J', '$', 'e', 'O', '8', '?', 'j', 'm', '+', '/', 'h', 'd', 'r', '7', '[', '"', 'V', 'i', 'G', "'", 'T', 'X', '#', '5']

penultimate = ['/', '6', '?', '5', 'o', "'", '|', 'T', ':', 'l', 'm', 'a', 'r', 'O', 'v', '0', 'J', '3', 'F', ';', 'g', 'I', '!', '+', 'A', 'W', ',', 'Y', 'R', '(', 'c', 'e', 'V', 'B', '@', 'h', 'b', '9', '1', 's', 'u', '"', 'H', 'j', 'n', 't', '<', 'P', 'q', 'y', '_', 'D', 'k', '=', '8', ']', '[', 'i', 'X', 'U', 'Z', 'p', 'L', '~', '^', 'G', ')', '*', ' ', 'Q', '-', '4', '`', 'M', '2', '%', 'N', '>', 'S', 'E', '{', '#', 'w', 'C', '&', 'K', 'f', '$', 'z', 'd', '}', '7', 'x', '.']

finale = ['*', 'f', '_', 'h', 'X', 'N', 's', ',', '~', 'B', '4', 'V', '5', '&', '9', '>', 'W', ';', 'E', 'i', 'T', 'e', 'o', 'q', 'K', 'R', '[', '7', '^', '@', ':', 'y', "'", 'd', '%', 'D', 'G', 'p', 'H', 'j', '|', '`', 'L', '"', '?', '#', '/', 'r', 'v', '=', 'a', 'x', 'c', 'A', '.', 'P', 'u', 'g', 't', ')', 'w', '+', 'm', '<', '3', 'Y', 'b', 'n', 'k', '}', '8', '(', 'Q', 'I', '{', 'F', 'M', '1', ']', ' ', 'J', 'Z', 'S', '$', 'z', 'U', '2', '!', '-', 'l', 'C', 'O', '0', '6']

#Displays length of default keys:
def keyStatus():
  print 'blowtorch key has ' + str(len(blowtorch)) + ' characters.'
  print 'clownfish key has ' + str(len(clownfish)) + ' characters.'
  print 'legomovie key has ' + str(len(clownfish)) + ' characters.'
  print 'penultimate key has ' + str(len(penultimate)) + ' characters.'
  print 'finale key has ' + str(len(finale)) + ' characters.'
  print 'There are ' + str(len(list)) + ' supported characters.'
  
#Checks key validity:
def testKey(key):
  if len(key) != len(list):
    print 'INVALID KEY'
    return -1
  for character in list:
    if key.count(character) != 1:
      print 'INVALID KEY'
      return -1
  print 'VALID KEY'
  return 1
#Generates a new key:
import random
def newKey():
  newKey = list
  random.shuffle(newKey)
  return newKey

#List of 94 supported characters and symbols in original order:
list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W','E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '|', ';', ':', '"', "'", ',', '.', '/', '<', '>', '?', '`', '~', ' ']


#Encryptor(s):

def encrypt1(message,key):
  if testKey(key) == -1:
    raise SystemExit(0)
  encrypted_message = ''
  for character in message:
    encrypted_message = encrypted_message + key[list.index(character)]
  return encrypted_message

#Decryptor(s):

def decrypt1(enc_mssg, key):
  if testKey(key) == -1:
    raise SystemExit(0)
  original_message = ''
  for character in enc_mssg:
    original_message = original_message + list[key.index(character)]
  return original_message

