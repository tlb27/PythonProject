import re
pattern='黑客|破解|反爬'
s='我想学python，破解一些vip视频，python可以实现无底线反爬吗'
str=re.sub(pattern,'xx',s)
print(str)

s='https://www.bilibili.com/video/BV1ZXRiYyEBk?spm_id_from=333.788.videopod.episodes&p=85'
pattern2='[?|&]'
str2=re.split(pattern2,s)
print(str2)