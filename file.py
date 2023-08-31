# 2 different method to open a file
# the next instruction is executed starting from where th cursor as left after the last instruction

f= open('test.txt')
#print(f.read())
l= f.readlines()
print(l)
f.close()

# opens the file with only one mode, + can be used for read and write

with open('test.txt','a', encoding='UTF-8') as f:
    f.write("\nciao gente")
    f.close()

with open('test.txt','r', encoding='UTF-8') as f:
    print(f.read(2))
    print(f.readline())
    f.close()
    


