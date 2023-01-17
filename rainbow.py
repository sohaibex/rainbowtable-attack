import random
import hashlib
import time
import numpy as np

with open('hash_challenges.txt', 'r') as f:
    my_list = np.array(f.read().splitlines())

def get_random_num():
    while True:
        num = random.randint(1000, 9999)
        if len(set(str(num))) == 4:
            break
    return num

def salt(password):
    salt = str(get_random_num())
    string_buffer = list(password)
    i = 0
    for s in range(4):
        pos = np.random.randint(0, len(string_buffer)+1)
        string_buffer.insert(pos, '&')
    
    for s in salt:
        string_buffer = ''.join(string_buffer).replace('&', s, 1)
    return ''.join(string_buffer)

def hash_md5(input_string):
    m = hashlib.md5()
    m.update(input_string.encode('utf-8'))
    return m.hexdigest()

def main():
    fichierMDP = open('words_ccm_2023.txt')
    lines = np.array(fichierMDP.readlines())
    total_time_start = time.time()

    for line in lines:
        time_start = time.time()
        for i in np.arange(0, 10000000):
            salt_ = ''.join(salt(''.join(line.splitlines())))

            if np.isin(hash_md5(salt_), my_list):
                f = open("rainbow.txt", "a")
                new_line = ''.join(line.splitlines()) + ":" + salt_ + ":" + hash_md5(salt_) + "\n"
                f.write(new_line)
                print(new_line)
                print(f'Total Time: {time.time() - total_time_start} seconds')
                f.close()
                break
    fichierMDP.close()
    print(f'Total Time: {time.time() - total_time_start} seconds')

main()