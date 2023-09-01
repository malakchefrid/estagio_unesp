from tinydb import TinyDB, Query
db = TinyDB('db.json')

#db.insert({'type': 'apple', 'count': 7})
#db.insert({'type': 'peach', 'count': 3})
db.insert({'type': 'ananas','count': 12})
print(db.all())

for item in db:
    print(item)

Fruit = Query()
print(db.search(Fruit.count==7))
print(db.search(Fruit.type=='peach'))
print(db.search(Fruit.type=='banana')) #doesn't exist

# change the count of the apple type
db.update({'count' : 10}, Fruit.type=='apple')
# if the field exists it gets changed, otherwise it is added
db.update({'size': 15}, Fruit.type=='peach')

# removes all instances
#db.remove(Fruit.type=='ananas')
db.search(Fruit.type=='ananas')



##### if you need to delete everything
##### db.truncate()