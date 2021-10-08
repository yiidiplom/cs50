#print ("hello")
#name = input("Name: ")
#print("Hello, "+ name+"!")
#print(f"Hello {name}!")
# n = int(input("Number: "))
# if n>0:
	# print (f"{n} - is positive")
# elif n<0:
	# print ("n - is negative")
# else:
	# print ("n - is zero")

class Point():
	def __init__(self,x1,y1):
		self.x = x1
		self.y = y1

p=Point(5,7)
print(f"x={p.x}  y={p.y}")