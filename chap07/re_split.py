import re

msg = 'にわに３わうらにわに５１わにわとりがいる'
ptn = re.compile(r'\d{1,}わ')
result = ptn.split(msg)
print(result)
