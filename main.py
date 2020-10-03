print("Input two digit ")
print("The first length of the list ")
a = int(input())
print("The second number of the list: ")
b = int(input())
c = []
import  random
for x in range(a):
  c.append(random.randint(0, b))
print(c)
print("Input index: ")
i = int(input())
print(c[i])

