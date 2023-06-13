# Chapter02-1
# 파이썬완전 기초
# Print 사용법

# 기본 출력
print('Python Start!')

print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('000', '1111', '1234', sep='-')

print()

# end 옵션
print('welcome to', end=' ')
print('IT', end=' ')
print('Web Site', end='')

print()

# file 옵션
import sys
print('Learn Python', file=sys.stdout)

print()

# format 사용(d, s, f)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

print()

#  %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('{:.5s}'.format('nice'))
print('{:.5s}'.format('asdfhjaksdhf')) # 5자리 수 다음부터 잘려라

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

print()

# %f
print('%f' % (3.1123123441234))
print('{:f}'.format(3.12345123))
print('%06.2f' % (3.11235412355123))
print('{:06.2f}'.format(3.4123512315))

print()

