import random
import string

def pass_gene(length: int = 25):
  #incl letters numbers and symbols
  char = string.ascii_letters + string.digits + string.punctuation
  #new string called password is made from the one of the ascii char, digits and punctuation in the range of the length given
  password = ''.join(random.choice(char) for i in range(length))
  return password

print("Generated Password Is: ", pass_gene())