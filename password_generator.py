#!/usr/bin/env python

import random

def random_funct():

 char = 'abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOPQRSTUVWZWYZ0123456789!^!\$%&/()=?{[]}+~#-_.:,;<>|\\'
 length_object = raw_input('Choose your length password :')
 length_object = int(length_object)

 for b in range(15):
  password = ''

  for h in range(length_object):
   password += random.choice(char)

  print(password)

def main():

 random_funct()

main()
