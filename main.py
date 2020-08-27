#clas notes
print("Hello, world!")
name = input("Enter your name: ")

print ("Hello, "+name+"!")
age = input("Enter your age: ")
age = int(age)
print (age+1)

print ("You will be "+str(age+1)+ "next year.")
print(f"I am {age+1} next year")

#homework
degreec = float(input("Enter temperature in celsius: "))
print (f"{degreec}°in Celsius is equivalent to {1.8*degreec+32}°Fahrenheit.")