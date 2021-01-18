# 딕션너리 생성하기
dataset = dict()
dataset['first'] = 1
dataset['second'] = 2
dataset['third'] = 3
print(dataset)

# 딕셔너리 빈도수 측정
data = ['Java', 'Python', 'C', 'Python']
counts = dict()
for name in data:
    '''get 메소드를 사용하여 기존에 존재하는지의 여부에 관계없이 데이터를 추가할 수 있다.'''
    counts[name] = counts.get(name, 0) + 1
print(counts)

# 딕셔너리 값 추출하기
samplelist = {'apple': 1, 'banana': 2, 'grape': 9}
print(list(samplelist))
print(samplelist.keys())
print(samplelist.values())
print(samplelist.items())

# 단어 빈도수 알기
fname = input('파일 이름을 입력해주세요: ')
file = open(fname, 'r')
line = dict()
for text in file:
    text = text.rstrip()
    box = text.split()
    for i in box:
        if i is None:
            continue
        else:
            line[i] = line.get(i, 0) + 1

maxnum = -1
for k, v in line.items():
    if v > maxnum:
        maxnum = v
        key = k

print('result: ', key, maxnum)





