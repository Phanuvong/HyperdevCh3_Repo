
# Create the calculations for each operations
def operator(op, x, y):
    # a functions for checking and calculating each operators
    try:
        if op == '+':
            ans_num = x + y
        elif op == '-':
            ans_num = x - y
        elif op == '*':
            ans_num = x * y
        elif op == '/':
            # check for divide by 0 Errors
            if y == 0:
                raise ZeroDivisionError()
            else:
                ans_num = x / y
        else:
            # no operator Error
            print("Error | you have entered an invalid operations")
            return
        return (ans_num)
    except ZeroDivisionError:
        print("Error | can't divide by zero")
        quit()


# Create calculator interface aka Input for 2 integers and operations
num_1 = input("Enter base number(Enter Redo to use last answer): ")
operations = input("Enter an operations( +, -, *, /): ")

# Create an Error to check for syntax errors
try:
    int_2 = float(input("Enter modifying number: "))
except ValueError:
    print("Error | modifying number isn't a number")
    quit()

# check and equate for redo
r_list = []
if num_1 == "Redo":
    # Open up text file for previous equations
    try:
        redo = open('./Hyperdev15_test/equations.txt', 'r')
        r_lines = redo.readlines()  # Read all lines into a list
    except FileNotFoundError:
        print("Error | text file not implemented")  # Check for file error
        quit()
    else:
        try:
            if r_lines:  # Check if there are any lines in the file
                last_ans = r_lines[-1]  # To get the last answered number
                r_ans = last_ans.strip().split('=')[1]
                r_list.append(float(r_ans.strip()))
            else:
                print("The file is empty.")
        except IndexError:
            # check for previous input in file
            print("Error | Their are no previous files")
            quit()
    finally:
        redo.close()

# covert num_1 into a float
try:
    if len(r_list) > 0:
        int_1 = float(r_list[0])
    else:
        int_1 = float(num_1)
except ValueError:
    # check for syntax error
    print("Error | base number isn't number ")
    quit()

# Outcome of calculations
ans_num = operator(operations, int_1, int_2)

# check for equation.txt error
try:
    equ = open('./Hyperdev15_test/equations.txt', 'r+')
except FileNotFoundError:
    print("Error | text file not implemented")
    quit()
equ.close()

# answers to the text file
equ = open('./Hyperdev15_test/equations.txt', 'a')
out_come = f"{int_1} {operations} {int_2} = {ans_num}\n"
print(out_come)
equ.write(out_come)
equ.close()
# Redo tool too use for previous equation from text file
