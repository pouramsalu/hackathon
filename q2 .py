# The chef's phone shows a Battery Low notification if the battery level is 15% or less. Given that the battery level of Chef's phone is X%, determine whether it would show a Battery low notification.
# Input Format
# First-line will contain T, the number of test cases. Then the test cases follow.
# Each test case contains a single line of input, an integer X, denoting the battery level of the phone.

# For each test case, output in a single line Yes, if the battery level is 15% or below. Otherwise, print No. You may print each character of Yes and No in uppercase or lowercase (for example, Yes, YES, yes yes will be considered identical).
# Sample Input 1 
# 3
# 15
# 3
# 65
# Sample Output 1 
# Yes
# Yes
# No
# Explanation
# Test Case 1: The battery level is 15. Thus, it would show a battery low notification.
# Test Case 2: The battery level is 3, which is less than 15. Thus, it would show a battery low notification.
# Test Case 3: The battery level is 65, which is greater than 15. Thus, it would not show a battery low notification.


i=1
while i<=3:
    num=int(input("enter any battery level is"))
    if num>=15:
        print("yes")
    elif num<15:
        print("no")
    i+=1

