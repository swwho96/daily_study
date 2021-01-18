"""튜플만들기"""
x = ('apple', 'banana', 'grape')
y = 1, 10, 50, 100
z = 2, 1, 5, 10

'''x[2] = 'watermelon' 튜플은 변경 불가능'''
print(x[2])
print(y)
if y < z:
    print(True)

'''튜플정렬 : 키로 정렬하기'''
data = {'banana': 23, 'apple': 16, 'boxes': 67}
print(sorted(data.items()))

'''튜플정렬 : 값으로 정렬하기'''
datalist = list()
for k, v in data.items():
    datalist.append((v, k))
print(sorted(datalist, reverse=True))

'''단어 빈도수 Top5 선정하기'''
fname = input('Enter the file name: ')
fp = open(fname)
result = list()
frequency = dict()

# 단어 빈도수 입력
for text in fp:
    text.rstrip()
    line = text.split()
    for words in line:
        frequency[words] = frequency.get(words, 0) + 1

# 값을 기준으로 정렬 (list comprehension)
result = sorted([(v, k) for k, v in frequency.items()], reverse=True)

# 빈도수 상위 5개 출력
for v, k in result[:5]:
    print(k, v)
