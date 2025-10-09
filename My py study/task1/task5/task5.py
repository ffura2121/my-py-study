new_dt = frozenset([1,2,5,7,3,3,5,4,"сто", False, 88, "OK",1231,4,43])
print(new_dt)


nums = [1,2,5,7,3,3,5,4]
nums = set(nums)
print(nums)

# data = set("Hello")
data = {4,3,1,2,99,1231,43}
data.add(321)
data.update(["сто", False, 88, "OK"])
data.remove(1231)
data.pop()
 
print(data)