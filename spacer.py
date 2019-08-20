with open("corpus.txt", "r") as i_f:
    with open("spaced_corpus.txt", "w") as o_f:
        for line in i_f:
            o_f.write(" ".join([hex(ord(c)) for c in line]) + "\n")
