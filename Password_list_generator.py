import itertools
import string

symbols = string.ascii_letters + string.digits  #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
combinations = itertools.product(symbols, repeat=4) #Generate all combinations

my_file = open("PassGen.csv", "a+")

for i in combinations:
    my_file.write(''.join(i) + '\n') # Combinations to file

my_file.close()
