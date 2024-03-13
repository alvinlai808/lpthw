class ShittyDB:
    def __init__(self):
        self.data = {}

    def create(self, key, value):
        if key in self.data:
            raise Exception("Key already exists")
        self.data[key] = value

    def read(self, key):
        if key not in self.data:
            raise Exception("Key does not exist")
        return self.data[key]

    def update(self, key, value):
        if key not in self.data:
            raise Exception("Key does not exist")
        self.data[key] = value
    
    def delete(self, key):
        if key not in self.data:
            raise Exception("Key does not exist")
        self.data.pop(key)

db = ShittyDB()
print(db)

key = "first_name"
value = "alvin"
try: 
    db.read(key)
except Exception as e:
    print(e)

db.create(key, value)
print(db.read(key))
db.update(key, 'penis')
print(db.read(key))
db.delete(key)
try: 
    db.read(key)
except Exception as e:
    print(e)