#create ,write ,read
#open(filename,mode)
#mode -read (r) ,write (w)


f = open("demo.txt","w")

f.write("Greetings studying python")

f.close()



x =open("demo.txt","r")

print(x.read())

x.close()


y = open("demo.txt","a")
y.write(" \n An interesting topic \n")

y.close()

x = open("demo.txt","r")

print(x.read())

x.close()


with open("demo.txt") as f:
    print(f.read())

