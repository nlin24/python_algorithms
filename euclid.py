def gcd(num1, num2):
  r = 0
  n = 0
  if num1 >= num2:
    r = num1 % num2
    n = num2
  else:
    r = num2 % num1
    n = num1
  while r > 0:
    t = r 
    r = n % r
    n = t
  return n

def gcd_recurse(a,b):
  if a % b == 0:
    return b
  else:
    if b > a:
      b = b % a
      return gcd_recurse(b,a)
    else:
      a = b
      b = a % b
    return gcd_recurse(a,b)

if __name__ == '__main__':
  print(str(gcd_recurse(60,96)))

    