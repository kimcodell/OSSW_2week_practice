def isNumber(a):
  _type = type(a)
  if _type is int or _type is float:
    return True
  else:
    return False

def plus(a,b):
  return a+b

def minus(a,b):
  return a-b

def mul(a,b):
  return float(a) * float(b)

def divide(a,b):
  return a/b

if __name__ == '__main__':
  print('\n첫번째 숫자를 입력하세요.')
  input1 = input('입력: ')

  print('\n원하는 사칙연산 기호 중 하나를 선택하세요. (+, -, *, /)')
  act = input('기호: ')

  print('\n두번째 숫자를 입력하세요.')
  input2 = input('입력: ')

  isValid = isNumber(input1) and isNumber(input2)
  if isValid:
    if act == '+':
      result = plus(input1, input2)
    elif act == '-':
      result = minus(input1, input2)
    elif act == '*':
      result = mul(input1, input2)
    elif act == '/':
      result = divide(input1, input2)
    print(f'사칙연산 결과는 {result} 입니다.')
  else:
    print('입력값이 잘못되었습니다.')
