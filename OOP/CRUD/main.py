from views import CreateMixin, ReadMixin, UpdateMixin, DeleteMixin
import json

class Product(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    def save(self):
        with open('data.json', 'w') as file:
            json.dump(self.objects, file, indent=4)
        return 'Saved!'
    
class Comment(CreateMixin, ReadMixin, DeleteMixin):
    pass


smart_phones = Product()
print(smart_phones.post(title='Redmi Note 10', description = 'The best phone for own price', qty=10, price=250))
print(smart_phones.post(title='Redmi 1', description = 'The worst phone for own price', qty=12, price=700))
print(smart_phones.post(title='Mi 12', description = 'Flagman phone for own price', qty=2, price=334))
print(smart_phones.post(title='Samsung j2', description = 'So so phone for own price', qty=45, price=242))
print(smart_phones.post(title='Iphone 13', description = 'Good phone for own price', qty=14, price=1000))
print()
print()
print(smart_phones.list())
print()
print()
print(smart_phones.detail(4))
print()
print(smart_phones.patch(1, title='Redmi Note 9'))
print()
print(smart_phones.list())
print(smart_phones.detail(1))
print()
print(smart_phones.delete(-1))
print(smart_phones.delete(1))
print(smart_phones.save())



