 q = input("Hello, I am calculator v2. to start the robots write yes:")

if q == "yes":
   k = input("choose symbols. + plus - minus / division * multiplier" )
  
   r = int(input ("See the first number:"))
  
   t = int(input ("See the second number:"))

if k == "+":
    c = r + t
    print("Answer:")
    print(int(c))

if k == "-":
    c = r - t
    print("Answer:")
    print(int(c))

if k == "*":
    c = r * t
    print("Answer:")
    print(int(c))

if k == "/":
    c = r / t
    print("Answer:")
    print(int(c))
   

  