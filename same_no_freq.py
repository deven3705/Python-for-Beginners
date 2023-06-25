def count_elements(l,x):
  count = 0
  for i in l:
    if i == x:
      count += 1
  return count


l = [1,1,2,4,3,5,6,6,9,1,3,1]
x = 1
print(f"{x} is occured {count_elements(l,x)} times")


