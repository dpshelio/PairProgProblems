import random

def create_file(filein, fileout):
    with open(filein, 'r') as fin:
        data = fin.readlines()
    data = [float(d) for d in data]

    fout = open(fileout, 'w')
    while len(data) >= 10:
        if random.random() < 0.3:
            palindromo = data[0:5]+data[::-1][-5:]
            fout.write(",".join("{0:.4f}".format(x) for x in palindromo) + '\n')
        else:
            fout.write(",".join("{0:.4f}".format(data.pop(0)) for x in range(10))+'\n')

    fout.close()

if __name__ == "__main__":
    create_file('DATA.DAT','RAW.dat')

