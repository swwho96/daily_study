# 개행문자 입력하기
print('hello\nworld')

# 파일 열기
fp = open('text.txt', 'r')
count = 0
for line in fp:
    count += 1
    '''print()는 자동 개행을 하기 때문에 오른쪽 공백 제거가 필요하다'''
    print(line.rstrip())
print("lines", count)

# 특정 문장 찾기
fp = open('text.txt', 'r')
count = 0
for line in fp:
    line.rstrip()
    if line.startswith('This'):
        print(line)

# 특정 문장 찾기(not 사용)
fp = open('text.txt', 'r')
count = 0
for line in fp:
    line.rstrip()
    if not line.startswith('This'):
        continue
    print(line)
    
# 원하는 파일 읽기
fname = input("파일 이름을 입력하세요(확장자 포함): ")
while True:
    try:
        fp = open(fname, 'r')
    except:
        print("Open Error - Can't find the file:", fname)
        break
    print('Success!')

# 파일 내용 대문자로 변환하기
fname = input("파일 이름을 입력하세요(확장자 포함): ")
while True:
    try:
        fp = open(fname, 'r')
    except:
        print("Open Error - Can't find the file:", fname)
        continue
    fp = open(fname, 'r')
    for line in fp:
        line = line.rstrip()
        print(line.upper())
    quit()
