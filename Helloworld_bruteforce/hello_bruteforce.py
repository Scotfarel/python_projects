import string
import random
import time
 
target_list = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
brute_list = ['', '', '', '', '', '', '', '', '', '', '', '', '']
 
 
def brute(tlist, blist):
    i = 0
    while i < len(target_list):
        if brute_list[i] != target_list[i]:
            brute_list[i] = random.choice(string.printable)
            print(''.join(brute_list))
        else:
            i += 1
        time.sleep(0.005)
 
brute(target_list, brute_list)
