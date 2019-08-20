import sys

with open(sys.argv[1], "r") as i_f:
    with open(sys.argv[2], "w") as o_f:
        for line in i_f:
            chunks = line.split()
            word = chunks[0]
            if word.startswith("0x"):
                word = chr(int(word, 16))
            o_f.write(word + " " + " ".join(chunks[1:]) + "\n")
