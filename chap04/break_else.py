data = ['さくら', 'うめ', 'ききょう', 'くちなし', 'ぼたん']
#data = ['さくら', 'うめ', 'x', 'くちなし', 'ぼたん']

for name in data:
    if name == 'x':
        break
    print(name)
else:
    print('正常終了しました。')
