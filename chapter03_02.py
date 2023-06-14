# Chapter03-2
# 파이썬 문자형

# 문자열 생성
str1 = "i am Python"
str2 = 'python';
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) # 길이를 구하는 방법

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I'm Boy

print('I\'m boy') # 뒤에 있는 특수문자를 그대로 노출한다.

escape_str1 = "Do you a \"retro games\"?"
print(escape_str1)

# row String
raw_s = r'D:\python\test'
print(raw_s)
print()

# 멀티라인 입력
# 역 슬러시를 이용하라
nulti_str = \
"""
문자열
멀티라인 입력
테스트
"""

print(nulti_str)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Deahon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수 (upper, isalnum, startswith, count ....)

print("Capitalize:", str_o1.capitalize())
print("endswith?:", str_o2.endswith("e"))
print("replace", str_o1.replace("thon", 'good'))
print("sorted", sorted(str_o1))
print("split:", str_o4.split(' '))
print()

# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str)) #__iter__ (반복이 되는것을 의미)

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python"

# 슬라이싱 연습
print(str_s1[0:3]) #처음부터 index 3번째까지 >> N, i, e
print(str_s1[5:])
print(str_s1[:len(str_s1)])
print(str_s1[:len(str_s1)-1])
print(str_s1[1:9:2]) # 3번째 인수는 띄어서
print(str_s1[-5:0]) # 오른쪽부터 세서 간다
print(str_s1[::2])
print(str_s1[::-1]) # 역순

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a))
print(chr(122))