#filler file
def main():
    for i in range(0,11):
        print(32/2*5*i)
        print("\n")
    file = open("NewFile.txt","w")
    file.write("Hello there!")
    file.close()
    filer = open("Newfile.txt", "r")  #very convoluted print statement...
    fileContent =filer.read()
    print(fileContent)
    filer.close()
#boilerplate
main()