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