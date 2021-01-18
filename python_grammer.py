# 정수형 데이터
a = 2021
b = -2020
c = 0
print("정수형 데이터 :", a, b, c)

# 실수형 데이터
a = 10.98
b = -18.384
c = 5.
d = -.7
e = 2e10
print("실수형 데이터 :", a, b, c, d, e)

# 2진수의 오차
a = 0.3 + 0.6
print("10진수의 합 계산 :", a)
print("2진수의 합 계산 :", round(a, 4))

# 사칙연산
a = 10
b = 3
print("사칙연산 :", a+b, a-b, a/b, a//b, a%b)
print("거듭제곱 계산 :", a**b)

# 리스트 만들기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("리스트 출력하기 :", a)

# 빈 리스트 선언
a = list()
print("list()로 빈 리스트 선언 :", a)
a = []
print("[]로 빈 리스트 선언 :", a)

# 크기가 N이고, 모든 값이 0인 리스트 초기화
n = 10
a = [0]*n
print("모든 값이 0인 리스트 만들기 :", a)

# 리스트 인덱싱하기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("리스트 4번째 숫자 :", a[3])
print("리스트 뒤에서 부터 출력하기 :", a[-1])
print("리스트 특정 위치의 값들 출력하기 :", a[1:6])

# 리스트 컴프리헨션
array = [i for i in range(2, 11, 2)]
print("리스트 컴프리헨션으로 2의 배수 출력하기 :", array)
n = 3
m = 4
array = [[0]*n for _ in range(m)]
print("2차원 리스트 출력하기 :", array)

# 리스트 관련 메서드
a = [9, 7, 8, 5, 4, 6, 1, 2, 7, 8, 9, 8, 7, 1, 5]
a.append(3)
print("3을 삽입한 리스트 :", a)
a.sort()
print("리스트 오름차순 정렬 :", a)
a.sort(reverse=True)
print("리스트 내림차순 정렬 :", a)
a.reverse()
print("리스트 역순 출력 :", a)
a.insert(10, 10)
print("리스트 특정 위치에 값 삽입 :", a)
print("리스트 특정 값(7) 세기 :", a.count(7))
a.remove(5)
print("5 삭제하기 :", a)
a.remove(5)
print("5 삭제하기 :", a)

# 값 일괄 삭제하기
a = {1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9, 9, 9, 9, 10}
remove_set = {8, 9}
result = [i for i in a if i not in remove_set]
print("8,9 일괄 삭제하기 :", result)

# 따옴표 넣기
print("\'따옴표\'나 \"큰따옴표\"는 \를 통해서 넣을 수 있습니다.")

# 문자열 합치기
print("문자열은" + " " + "+로 합칠 수 있습니다.")
print("동일한 문자열은" * 2 + " " + "*로 쉽게 표현할 수 있습니다.")

# 튜플
a = (1,2,3,4,5)
print("튜플은 ()를 사용하고, 값 변경이 불가능합니다. :", a)

# 딕셔너리
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['포도'] = 'Grape'
print("딕셔너리 구조는 키:값으로 이루어져 있습니다. :", data)
if '바나나' in data:
    print("바나나가 존재합니다.")
keys = data.keys()
values = data.values()
print(keys, values)

# 집합
a = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = {1, 3, 5}
print("집합은 set([])이나 {}를 통해 선언할 수 있습니다. :", a)
print("합집합(a|b) :", a|b)
print("교집합(a&b) :", a&b)
print("차집합(a-b) :", a-b)
a.add(10)
a.update([11, 12])
a.remove(1)
print("add()로 단일 값 삽입, update([])로 일괄 삽입, remove로 삭제 :", a)