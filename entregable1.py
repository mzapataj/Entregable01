def primerPunto(a,b):
  numeros = []
  count = 0
  for i in range(a-1,b+1):  
      for j in range(a-1,b+1):
        if(i!=j and containsSameNumbers(j,i)):
          #print(i)
          #print(j)
          count +=1
          break
  return count 

def count_digits(number):
  digits={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
  for i in range(10):
    for n in number.zfill(len(str(abs(b-a+1)))):
      if n == str(i):
        digits[i] += 1
  return digits
  
def containsSameNumbers(a,b):
    s = count_digits(str(a))
    t = count_digits(str(b))
    if (s !=[0,0,0,0,0,0,0,0,0,0] or t !=[0,0,0,0,0,0,0,0,0,0]) and t == s:
      print(str(s))
      return True
    
    return False
print("Donde a<=b\n")  
a = int(input("Ponga su a:"))
b = int(input("Ponga su b:"))
print(b-a+1-primerPunto(a,b))