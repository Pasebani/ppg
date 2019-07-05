import random
import subprocess
import string

################################
many = int(input("How Many Want You :"))
length = int(input("Enter The Length :"))
for i in range(many):
	s = string.ascii_letters + string.digits + "@#$%^"
	rand = random.sample(s,length)
	password = ''.join(rand)
	print("Passworde {0} is :{1}".format(i+1,password))