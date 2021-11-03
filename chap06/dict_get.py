d = {'apple': 'リンゴ', 'orange': 'みかん', 'melon': 'メロン'}
# print(d['pear'])
print(d.get('pear', 'x'))
print(d.pop('melon', '×'))
print(d.popitem())
print(d)
