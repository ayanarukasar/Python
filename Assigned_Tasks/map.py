def square_num(n):
  return n * n
nums = [1,2,3]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))