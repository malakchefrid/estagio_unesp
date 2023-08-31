######testing list methods

#create a list conaining numbers from 1 to 9
mylist=list(range(1,10))
print(mylist)
#create a list conaining characters from 1 to 9
print(list(map(str, range(1,10) )))
print(len(mylist))
que_legal= 'que tudo'
hislist=['nossa', que_legal]

mylist.append('hello')
print(mylist)
#add a list to another one
mylist.extend(hislist)
print(mylist)
id= mylist.index('nossa')
print(id)
del mylist[1:5]
print(mylist)
new= mylist.copy()
# mixed printing
print(f'new= {new}')

a_list = ['mayssa', 'malak', 'maram', 'nacira', 'abdelhamid' ] 
print(sorted(a_list))
print(a_list)
a_list.sort()
print(a_list)
# tests weather an element is in the list
print('maram' in a_list)

###testing tuple methods
mytuple = ('hello', 'yes', 'unesp', 'brasil')
print(len(mytuple), mytuple.count('brasil'))

estudante = ("João", 21, "História das Relações Internacionais", 10.0)
nome, idade, disciplina, nota = estudante
print(nome)

###### testing set methods
myset = set()
myset = {2,5,9,'1956','republica'}
print(myset)

myset.add('careful')
myset.discard('barbie')
print(myset)
print(myset.pop())
# adds the parameter set to the set who called the method
myset.update({54,'hello'})
print(myset)

# converting a set to a list and vice versa
l = list(myset)
s= set(mylist)
a_set = {'mas', 'posso'}
print(l, s)
print(myset.union(a_set))
inter = myset.intersection(a_set)
diff = myset.difference(a_set)
print(inter, diff)

print('\n')
###### testing dictionary methods
mydict = {'Tunisia': "Tunis", 'Brasil': "brasilia"}
print(mydict.items())
#mydict['Egypt']   returns error if the key does not exist
mydict.get('Egypt')  # fails silently
a_dict = mydict.fromkeys(['Tunisia', 'Brasil', 'Egypt'], {1, 2 ,5})
print(f'a_dict = {a_dict}')
print(f'mydict = {mydict}')
#returns the value of the specified key
print(mydict.setdefault('Tunisia'))
# adds an item to the dictionary
mydict.setdefault('Algeria','alger')
print(mydict.items())

# if the key is not in the dict, it searches for the defaults value, the second one
find = mydict.get('france','Tunisia')
print(find)
new = mydict.update({"Egypt" : "Cairo"}) # the method returns none, we must print the dict
print(f'mydict = {mydict}' , f'a_dict = {a_dict}', f'\n new = {mydict.items()}')