# import numpy as np 
# result=np.random.choice(["head","tail"])
# print(result)
# import numpy as np

# dice = np.random.randint(1, 7)

# print(dice)
# import numpy as np

# dice = np.random.choice([1, 2, 3, 4, 5, 6], size=2)

# even = np.sum((dice == 2) | (dice == 4) | (dice == 6))

# probability = even / 2
# print(dice)
# print(even)
# print(probability)


import numpy as np

dice = np.random.choice([1, 2, 3, 4, 5, 6], size=2)

even = np.sum(dice % 2 == 0)

probability = even / 2

print(dice)
print(even)
print(probability)
# dice=np.random.choice([1,2,3,4,5,6])
# print(dice)