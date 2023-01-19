
## Practicing textbook problems here:

####################################################################################

# Sentinel-Controlled Iteration -- Class Grade Average w/ User Input

#total = 0
#grade_counter = 0

#grade = int(input('Enter grades, end with -1: '))

#while grade != -1:
    #total += grade
    #grade_counter += 1
    #grade = int(input('Enter grade, end with -1: '))

#if grade_counter != 0:
    #average = total / grade_counter
    #print(f'Class average is {average:.2f}') # .2f formats the average number as a floating-point number with two decimals
#else:
    #print('No grades were entered')

####################################################################################

# Nested Control Statements Program

passes = 0
failures = 0

for student in range(10):
    grade = int(input('Exam result pass(1) or fail(2): '))

    if grade == 1:      ## this if statement is the NESTED statement in this program
        passes += 1
    else:
        failures += 1

print()
print(f'Total passing grades is {passes}')
print(f'Total failing grades is {failures}')
print()

if passes > 8:
    print('Bonus to instructor')

