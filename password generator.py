import random
import string
print("RANDOM PASSWORD GENERATOR")

min_len=12
max_len=20
digits=list(range(0,10))
lower=list(string.ascii_lowercase)
upper=list(string.ascii_uppercase)
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '~', '>','*', '(', ')', '<']
combined_list= digits+lower+upper+symbols
password=random.choices(combined_list, k=12)
print(''.join(map(str,password)),"is the reqd password")