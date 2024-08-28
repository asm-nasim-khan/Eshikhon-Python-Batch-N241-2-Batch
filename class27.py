def myFunc(msg,index):
    if index < 0:
        return
    print(msg[index])
    myFunc(msg,index-1)

text = "Mango"
myFunc(text,len(text)-1)

