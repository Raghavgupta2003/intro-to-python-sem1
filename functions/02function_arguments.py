# ------------------------------------------------------------
# 1. Function to check EVEN or ODD
# ------------------------------------------------------------
def check_even_odd(x):
    if x % 2 == 0:
        print(x, "is even")
    else:
        print(x, "is odd")

# Driver code
check_even_odd(3)
check_even_odd(5)
print()


# ------------------------------------------------------------
# 2. Default Argument
# ------------------------------------------------------------
def check_numbers(x, y=50):
    print("x =", x, ", y =", y)
    if x % 2 == 0 and y % 2 == 0:
        print("Both even")
    else:
        print("Odd detected")

check_numbers(30)
print()


# ------------------------------------------------------------
# 3. Default Argument (Both defaults)
# ------------------------------------------------------------
def test_default(x=55, y=55):
    if x % 2 == 0 or y % 2 == 0:
        print("Even present")
    else:
        print("Both odd")

test_default()
print()


# ------------------------------------------------------------
# 4. Without Default Arguments (user input)
# ------------------------------------------------------------
def check_pair(x, y):
    if x % 2 == 0 and y % 2 == 0:
        print("Both even")
    else:
        print("Not both even")

a = int(input("Enter x: "))
b = int(input("Enter y: "))
check_pair(a, b)
print()


# ------------------------------------------------------------
# 5. Keyword Arguments
# ------------------------------------------------------------
def display_course(BTech, Branch):
    print("Course:", BTech)
    print("Branch:", Branch)

display_course(BTech="4 years", Branch="CSE")
print()


# ------------------------------------------------------------
# 6. Variable Length Argument (*argv)
# ------------------------------------------------------------
def show_messages(*argv):
    for msg in argv:
        print(msg)

show_messages("Hello", "Welcome to LPU", "Have fun")
print()


# ------------------------------------------------------------
# 7. Variable Keyword Argument (**kwargs)
# ------------------------------------------------------------
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

student_info(Btech="4 years", Branch="CSE-A")
print()
