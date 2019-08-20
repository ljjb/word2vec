import math
import os
import re
import subprocess
import sys

MAX_SIZE = 3570000
DIVISIONS = 10
i = 0
idx = 0

def run_command(cmd):
    cmd = cmd.split()
    
    process = subprocess.Popen(cmd,stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if process.poll() is not None and output == '':
            break
        if output:
            print (output.strip())
progre = re.compile("Progress: (.*)%")

while i < MAX_SIZE:
    idx += 1
    i += math.floor(MAX_SIZE / 10)
    # newcorp_cmd = "head -n {} spaced_corpus.txt > chopped.txt".format(i)
    print("GOTHER")
    with open("spaced_corpus.txt", "r") as i_f:
        with open("chopped.txt", "w") as o_f:
            j = 0
            for line in i_f:
                o_f.write(line)
                j += 1
                if j >= i:
                    break
            
    print("MOVED")

    train_cmd = "./word2vec -train chopped.txt -output vectors-{}.bin -cbow 1 -size 300 -window 5 -negative 5 -hs 0 -min-count {} -sample 5e-3 -threads 8 -binary 0 -iter 1".format(idx, idx)
    train_sp = subprocess.Popen(train_cmd.split(), stdout=subprocess.PIPE)
    while True:
        line = train_sp.stdout.readline().rstrip()
        if (not line) and train_sp.poll() is not None:
            break
        else:
            chunks = line.split(b"\r")
            match = progre.match(str(chunks[0]))
            print(match)
            print(str(chunks[0]))
           
    with open("vectors-{}.bin".format(idx), "r") as i_f:
        with open("cvectors-{}.bin".format(idx), "w") as o_f:
            for line in i_f:
                chunks = line.split()
                word = chunks[0]
                if word.startswith("0x"):
                    word = chr(int(word, 16))
                o_f.write(word + " " + " ".join(chunks[1:]) + "\n")
            
    # for line in iter(train_sp.stdout.readline, ''):
    #     sys.stdout.write(line)
    # output, error = train_sp.communicate()
    # print(output)

