mark = int(input("Please enter your mark: "))

if mark > 100:
    print("Invalid input. Please enter mark between 0 and 100.")

elif mark < 0:
    print("Invalid input. Please enter mark between 0 and 100.")

elif mark >= 80 and mark <= 100:
    print("A+")

elif mark >= 70 and mark < 80:
    print("A")

elif mark >= 60 and mark < 70:
    print("A-")

elif mark >= 50 and mark < 60:
    print("B")

elif mark >= 40 and mark < 50:
    print("C")

elif mark >= 33 and mark <= 40:
    print("D")

else:
    print("Failed")
