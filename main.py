nameList = ["Jason", "Kristian", "Esme", "Keigo", "Sean", "Stella", "Peter", "Spencer", "Leo"]

def maxLength(givenList):
    wordLength = 0
    for item in givenList:
        if len(item) > wordLength:
            wordLength = len(item)
    return wordLength   

def names1():
    for item in nameList:
        print(item)
names1()
def names2():
    for item in nameList:
        print(item[0])
names2()
def names3():
    for i in nameList[0]:
        print(i)
names3()
def names4():
    wordsize = maxLength(nameList)
    print("List Length: ", len(nameList))
    for i in range(wordsize):
        print(i)
        for name in nameList:
            if i >= len(name):
                print("", end='')
            else:
                print(name[i], end='')
        print('')           
names4()
def names5():
    wordsize = maxLength(nameList) 
    for i in range(wordsize): # Names
        spaceIndex = 0
        for letter in nameList[i]: # Letters
            for a in range(spaceIndex):
              print(' ', end='')
            print(letter)
            spaceIndex += 1
names5()                    