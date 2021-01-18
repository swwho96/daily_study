FirstWord = 'Hello World'
SecondWord = 'Bye World'
Space = '  abc   '
line = 'Do_you-want/a^build$a~snowman?'
Email = 'tjtmddn24@naver.com'


# 문자열 길이 구하기
print(len(FirstWord))
# Hell 출력하기
print(FirstWord[0:4])
# Hello World Bye World 출력하기
print(FirstWord + ' ' + SecondWord)
# Hello 찾기
if 'Hello' in FirstWord:
    print("Yes. Hello in " + FirstWord)
# 소문자로 변환하기
print(FirstWord.lower() + ' ' + SecondWord.lower())

# 대문자로 변환하기
print(FirstWord.upper() + ' ' + SecondWord.upper())

# 왼쪽 공백 제거
print(Space.rstrip())

# 오른쪽 공백 제거
print(Space.lstrip())

# 좌우 공백 제거
print(Space.strip())

# 시작 문자 찾기
print(line.startswith('Do'))
print(line.startswith('do'))

# 문자열 파싱(이메일 주소에서 아이디 추출하기)
position = (Email.find('@'))
ID = Email[0:position]
print(ID)

# python 문자열 변경
words = 'Connect Foundation'
if 'F' in words:
    words.lower()
    # words[7] = '&'는 문자열을 변경할 수 없다.
    words = words[:7] + '&' + words[8:]
else:
    print(words)

print(words)