# http://www.checkio.org/mission/prime-palindrome-golf/

def golf(n):
 while n:
  n+=1
  if n==2or str(n)==str(n)[::-1]and all(n%i for i in range(2,n)):return n
