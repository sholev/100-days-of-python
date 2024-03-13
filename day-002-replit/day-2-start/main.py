import math
print("Data Types:")

print("\nString:")
string = "Hello"
print(string[len(string) - 1])

print("\nInteger:")
integer = 123_456_789
print(integer)

print("\nFloat:")
pi = math.pi
print(pi)

print("\nBoolean:")
boolean = True & False
print(boolean)

print("\nType Conversion/Checking:")
num_char = len("Hello")
print(type(num_char))
print("Length: " + str(num_char))

num = 123
print(type(num))
print(type(str(num)))

print(70 + float("100.5"))
print(str(70) + str(100.5))

print("\nMathematical Operations:")

print("\nPower:")
print(2 ** 3)

print("\nNumber Manipulation:")
print(8 // 3)
print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 3))

result = 4 / 2
result /= 2
print(result)

score = 0
score += 1
print(score)

print("\nf-Strings:")
score = 7
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")