'''Cho một từ điển sau:
inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
Thực hiện các yêu cầu sau:
+ Thêm key 'pocket' vào dictionary trên. Value của 'pocket' là một danh sách
bao gồm các phần tử 'seashell', 'strange berry', và 'lint'.
+ Sắp xếp các phần tử trong 'backpack' key.
+ Loại bỏ biến 'dagger'
+ Thêm giá trị 50 vào 'gold' key.'''
print('-------------------Bài làm------------------')
# Tạo từ điển inventory
inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Thêm key 'pocket' vào dictionary và gán giá trị là một danh sách các phần tử
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# Sắp xếp các phần tử trong key 'backpack'
inventory['backpack'].sort()

# Loại bỏ biến 'dagger' từ key 'backpack'
inventory['backpack'].remove('dagger')

# Thêm giá trị 50 vào key 'gold'
inventory['gold'] += 50

# In ra inventory sau khi thực hiện các thay đổi
print("Inventory sau khi thực hiện các thao tác:")
print(inventory)
