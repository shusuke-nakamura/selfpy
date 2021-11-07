import re

tags = '<p><strong>WINGS</strong>サイト<a href="index.html"><img src="wings.jpg" /></a></p>'
ptn = re.compile('<.+>')  # 最長
# ptn = re.compile('<.+?>') # 最短

results = ptn.findall(tags)

for result in results:
    print(result)
