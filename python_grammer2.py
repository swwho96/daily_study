# 논리 연산자
score = 85
sex = 'female'
if score > 90 and sex == 'female':
    print("A학점입니다.")
elif score > 80 or sex == 'female':
    print("B학점입니다.")
else:
    print("C학점입니다.")

data = 1
sex = 'male' if data == 0 else 'female'
print("성별은 ", sex, '입니다.')

a = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9]
remove = {8, 9}
result = [i for i in a if i not in remove]
print(result)

x = 65
if 0 < x < 70:
    print("x가 범위 안에 존재합니다.")

# 반복문(while)
sum = 0
i = 1
while i <= 9:
    sum += i
    i += 1
print(sum)
'''range(시작값, 끝값+1) -> 시작값 ~ 끝값'''
for num in range(1, 11):
    sum += num
print("1부터 10까지의 합은", sum, "입니다.")

'''구구단 프로그램
for p in range(1, 10):
    for k in range(1, 10):
        print(p, "*", k, "=", p*k)'''


# 함수
number = 3

def add(a, b):
    return a + b

def function():
    global number
    return number + 123

print(function())
print(add(658, 9723))
print((lambda c, d: c+d)(658, 9723))

# 입출력
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)

n, m, k = map(int, input().split())
print(n, m, k)

import sys
data = sys.stdin.readline().rstrip()
print(data)

print("숫자와 문자열은", str(n), "콤마로 합칠 수 있습니다.")
print(f"숫자와 문자열은 {n} 콤마로 합칠 수 있습니다.")