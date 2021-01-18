# 리스트 출력하기
friends = ['Sally', 'Eric', 'Jone']
for i in range(len(friends)):
    print(friends[i])

# 리스트 만들기
things = list()
while True:
    name = input("Enter the thing: ")
    if name == 'done':
        break
    things.append(name)
print(things)

# 리스트 값 추출하기
line = "Why didn't you punish me when I first stall the toy car ?"
line2 = "Why$didn't$you$punish$me$when$I$first$stall$the$toy$car$?"
words = line.split()
words2 = line2.split('$')
print(words)
print(words2)

# 리스트 합치기
list1 = [1,2,3,4]
list2 = [5,6,7,8]
print(list1 + list2)