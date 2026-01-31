
def main():
    #open a file named philosophers.txt
    outfile = open('philosophers.txt', 'a')


    #append the names of two more philosophers to the file
    #Ifeoluwanimi Adenekan
    outfile.write('Ifeoluwanimi Adenekan\n')
    outfile.write('Georg Hegel\n')


    #close the file
    outfile.close()

main()