Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re

fname = input()
m = int(input())
with open("data/"+fname, 'r', encoding='utf-8') as f:
	L = re.split('\W+', f.read()) # L은 단어들로 구성된 리스트

word_count = []

for x in range(0,len(L)):
        temp = L.count(L[x]) #각 단어의 개수를 저장
        if temp >= m:
                word_count.append(L[x])

word_count.sort()
print(word_count)
