# Exercise 2

# Question 1)
degrees = int(input("Enter degrees:"))
radians = degrees*3.14/180
print("Degrees: "+ str(degrees))
print("Radians: "+ str(radians))

# Question 2)
print("Enter student scores here: ")
x = 0
average = 0
while x < 3:
    student = float(input())
    average = student + average
    x += 1
print(average/3)

# Question 3)
print("Number of students in each group: ")
Leftover1 = 32 - (5*int(input("Class 1: ")))
Leftover2 = 45 - (7*int(input("Class 2: ")))
Leftover3 = 51 - (6*int(input("Class 3: ")))
print("Number of students leftover: ")
print("Class 1: " + str(Leftover1))
print("Class 2: " + str(Leftover2))
print("Class 3: " + str(Leftover3))

# Question 4)
pi = 3.14
pie_diameter = 55.4
pie_radius = pie_diameter / 2
circumference = 2 * pi * pie_radius
circumference_msg = "Jimmy’s pie has a circumference: "
print(circumference_msg, circumference)

# Question 5)
speed = float(input("The speed (m/s): "))
frequency = float(input("The frequency (Hz):"))
print("The wavelength (m): " + str(speed/frequency))
