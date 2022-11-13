tam = int(input())

for i in range(1, tam+1):
   lis = input().split()
   y = 0
   a = lis[27:]
   b = lis[:27]

   for j in range(3):
      try:
         val = int(b[-1][0])
      except ValueError:
         val = 10

      x = val
      y += x
      b = b[:(len(b)-(11-x))]

   b.extend(a)
   print(f"Case {i}: {b[y-1]}")
   