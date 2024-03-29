print("Dãy fibonaci từ 1 đến 100 là:")
a,b = 0,1
for i in range(1,101):
  print(a,end=",")
  if a + b >= 100:
    break
  a,b = a+b,a