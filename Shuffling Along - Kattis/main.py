size, type_shuffle = input().split()

size = int(size)

odd = size%2

lis = [i for i in range(size)]
res = lis[::-1][::-1]

def in_(count: int, lis: list):
  part = size//2

  a = lis[:part]
  b = lis[part:]
  p_count = 1

  for i in a:
    position = a.index(i) + p_count
    b.insert(position, i)
    p_count += 1

  count+=1

  if b != res:
    return in_(count, b)

  return count

def out_(count: int, lis: list):
    part = (size//2)+1 if odd else size//2

    a = lis[:part]
    b = lis[part:]
    p_count = 1

    for i in b:
      position = b.index(i) + p_count
      a.insert(position, i)
      p_count+=1

    count += 1

    if a != res:
      return out_(count, a)

    return count

shufflers = {"in": in_, "out": out_}
print(shufflers[type_shuffle](0, lis))
