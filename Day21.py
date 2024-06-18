# INHERITANCE

# class Animal:
#     def __init__(self):
#         self.num_eyes=2
#     def breathe(self):
#         print("Inhale, exhale.")
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Moving in water")
# nemo=Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)


# class Animal:
#     def __init__(self):
#         self.num_eyes=2
#     def breathe(self):
#         print("Inhale, exhale.")
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#     def breathe(self):
#         super().breathe()
#         print("Doing under water")
#     def swim(self):
#         print("Moving in water")
# nemo=Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)


# Slicing
keys=["a","b","c","d","e","f"]
print(keys[2:5])
print(keys[2:])
print(keys[1:])
print(keys[:5])
print(keys[2:5:2])
print(keys[::-1])