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

## advanced

db.insert({'country': 'Jamaica', 'country-code': '1-876'})
user = Query()
## we can't use the format db.search(user.country-code == '1-876), it is invalid because of the hyphen in country-code
## we use the following sntax instead
db.search(user['country-code'] =='1-876')

#using where
from tinydb import where
print(db.search(where('type')=='apple'))

# add nested fields
db.insert({
  "log": {
    "1": {
      "date": "2021-12-11",
      "split": "legday",
      "exercises": [
        {
          "name": "squat",
          "sets": [
            { "set no.": 1, "reps": 8, "weight": "70 kg" },
            { "set no.": 2, "reps": 8, "weight": "80 kg" },
            { "set no.": 3, "reps": 5, "weight": "90 kg" },
            { "set no.": 4, "reps": 5, "weight": "90 kg" }
          ]
        },
        {
          "name": "deadlift",
          "sets": [
            { "set no.": 1, "reps": 8, "weight": "70 kg" },
            { "set no.": 2, "reps": 8, "weight": "80 kg" },
            { "set no.": 3, "reps": 5, "weight": "90 kg" },
            { "set no.": 4, "reps": 5, "weight": "90 kg" }
          ]
        }
      ]
    }
  }
})

print(len(db))