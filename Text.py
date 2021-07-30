def countingwords():
    filename=input("Enter The File Name ")
    numberofwords=0
    file=open(filename,"r")
    for eachline in file:
        word=eachline.split()
        numberofwords=numberofwords+len(word)
    print("Number Of Words Is: ",numberofwords)

countingwords()
