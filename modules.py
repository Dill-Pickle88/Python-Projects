import math
import random
import statistics
import keyword


print(math.pow(2,3))
print(random.randint(0, 100))

# mean
nums = [1, 5, 33, 12, 46, 33, 2]
print(statistics.mean(nums))

# median
print(statistics.median(nums))

# mode
print(statistics.mode(nums))

# standard deviation
print(statistics.pstdev(nums))


print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))

