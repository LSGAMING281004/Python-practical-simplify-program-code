#1. Area and perimeter of a circle
import math
r = float(input("Enter Radius:"))  
print(f"Area: {math.pi * r**2:.2f}, Perimeter: {2 * math.pi * r:.2f}")

#2. Fibonacci series
a, b, n = 0, 1, int(input("Enter number of fibo:")) 
for _ in range(n): print(a); a, b = b, a + b

#3. Gcd of two numbers
import math
print(math.gcd(30,60))

#4. Valid Prime number
n = int(input("Enter Number:"))
print("Prime" if n > 1 and all(n % i for i in range(2, int(n**0.5) + 1)) else "Not Prime") 

#5. Sum of squares
print(sum(i**2 for i in range(1, int(input("Enter value:"))+1)))

#6. Sum of the elements in an array
print(sum(map(int, input("Enter multiple numbers with space:").split())))

#7. Largest elements in an array
print(max(map(int, input("Enter multiple numbers with space:").split())))

#8. Palindrome
s = input("Enter string name:"); print("Palindrome" if s == s[::-1] else "Not a Palindrome")

#9. List
lst = list(map(str, input("Enter list of string:").split())); print("List:", lst)

#List operation: Length, Reverse, Copy, Clear
lst = list(map(int, input("Enter multi integers with spaces:").split())) 
print(len(lst), lst[::-1], lst[:], [])
