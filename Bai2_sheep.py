listsheep = [5, 7, 300, 90, 24, 50, 75]
a = '''__________________________________________________
Hello, my name is Bang and these are my ship sizes'''
print (a)
print (listsheep)
print ("__________________________________________________\n"
       'Now my biggest sheep has size', max (listsheep), "let's shear it\n"
        "__________________________________________________")
print ("After shearing, here is my flock")
b =  listsheep.index (max (listsheep))
listsheep [b] = 8
print (listsheep,
        "\n__________________________________________________")


sheep = [5, 7, 8, 90, 24, 50, 75]
c = '''MONTH 1:
One month has passed, now here is my flock'''
print (c)

for i in range (0,len (sheep)):
         sheep[i] += 50
print (sheep,        
"\nNow my biggest sheep has size", max(sheep), "let's shear it\n"
"After shearing, here is my flock")

i =  sheep . index (max (sheep))
sheep[i] = 8
print (sheep,
        "\n__________________________________________________")


print ("Month 2:\n"
'One month has passed, now here is my flock')

for i in range (0, len  (sheep)):
         sheep[i] += 50

print (sheep,
"\nNow my biggest sheep has size", max (sheep), "let's shear it \n"
"After shearing, here is my flock")

d =  sheep.index (max (sheep))
sheep [d] = 8
print (sheep)


for j in range (0, len (sheep)):
         sheep [j] += 50
        
print ("\n__________________________________________________\n"
       "Month 3:\n"
       "One month has passed, now here is my flock\n",
        sheep,
       "\n__________________________________________________")



print ("My flock has size in total: ", end =" ")
tong = 0
for i in range(0,len(sheep)):
     tong += sheep[i]
print(tong,
"\nI would get: ", tong, " * 2$ = ", tong*2, "$")