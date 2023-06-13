# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n)) # int = 정수형

# 동시 선언
x = y = z = 700
print(x, y, z)

# 선언
var = 75

# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))

# 재선언이 되면 위에 있는것을 가지고 올 수 없다.

# Object Referernces
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))

print()

m = 400
print(m, n)
print(type(m), type(n))

print()


# id(identity)확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 파이썬은 자체적으로 동일한 값에 대해서는 동일한 인스턴스로 확인하여 하나의 오브젝트로 만든다. (파이썬의 최적화)

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates > method
# Pascal Case : NumberOfColegeGraduates > class
# Snake Case : number_of_colleage_graduates > 파이썬에서 class 할때 많이 사용

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7

# 특수문자나, 숫자로 시작되는 변수는 안된다
# 특수문자는 '_', '$' 만 된다.

