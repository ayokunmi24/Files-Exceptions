infile = open('philosophers.txt', 'r')
def main():
    #open a file named philosophers.txt
    infile = open('philosophers.txt', 'r')


    #read the names of the philosophers from the file
    philosopher1 = infile.readline().strip()
    philosopher2 = infile.readline().strip()
    philosopher3 = infile.readline().strip()


    #print the names of the philosophers
    print('The philosophers are:')
    print(philosopher1)
    print(philosopher2)
    print(philosopher3)


    #close the file
    infile.close()