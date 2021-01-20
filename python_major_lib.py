# 내장함수
result = sum([1,2,3,4])
print("sum()함수를 이용한 1~4의 합 :", result)

result = min(7,3,10,9,1)
print("min()함수를 이용한 최솟값 찾기 :", result)

result = max(7,3,10,9,1)
print("max()함수를 이용한 최댓값 찾기 :", result)

result = eval("5+8*7-10")
print("eval()함수를 이용해서 문자열 수식을 계산 :", result)

data = sorted([9,8,2,5,6,3,7,4])
print("sorted() 오름차순 정렬 :", data)

data = sorted([9,8,2,5,6,3,7,4], reverse=True)
print("sorted(revere=Ture) 내림차순 정렬 :", data)

# itertools
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(permutations(data, 2))
print("3개중 2개를 뽑아 나열 :", result)
result = list(combinations(data, 2))
print("3개중 2개를 뽑아 순서에 상관없이 나열 :", result)
result = list(product(data, repeat=2))
print("3개중 2개를 뽑아 나열(중복 허용) :", result)
result = list(combinations_with_replacement(data, 2))
print("3개중 2개를 뽑아 순서에 상관없이 나열(중복 허용) :", result)

# heapq
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print("힙 정렬 :", result)

def maxheapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = maxheapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print("힙 정렬(내림차순) :", result)

# bisect
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4
print("이진 탐색 트리 왼쪽 인덱스값 :", bisect_left(a, x))
print("이진 탐색 트리 오른쪽 인덱스값 :", bisect_right(a, x))

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print("데이터중 4의 개수 :", count_by_range(a, 4, 4))
print("데이터중 0과 3사이의 속하는 숫자 개수 :", count_by_range(a, 0, 3))

# collections
from collections import deque
data = deque([7, 8, 9])
data.appendleft(6)
data.append(10)
print("삽입은 append(), 삭제는 pop() :", list(data))

# math
import math
print("5! =",math.factorial(5))
print("100의 제곱근 =", math.sqrt(100))
print("14와 21의 최대공약수 :", math.gcd(14, 21))
print("파이 :", math.pi)
print("자연상수 e :", math.e)
