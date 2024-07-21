def add(num1,num2):
  return num1+num2
def sub(num1,num2):
  return num1-num2
def mul(num1,num2):
  return num1*num2
def div(num1,num2):
  return num1/num2
def par(num1,num2):
  return num1%num2

print("Please select operation -\n" "1. Add\n" "2. Subtract\n" "3. Multiply\n" "4. Divide\n" "5. percentage")
select = int(input("Select operations form 1, 2, 3, 4, 5 :"))
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
if select == 1:
	print(f"{number_1} + {number_2} = {add(number_1,number_2)}")
elif select == 2:
	print(f"{number_1} - {number_2} = {sub(number_1, number_2)}")
elif select == 3:
	print(f"{number_1} * {number_2} = {mul(number_1, number_2)}")
elif select == 4:
	print(f"{number_1} / {number_2} = {div(number_1, number_2)}")
elif select == 5:
	print(f"{number_1} % {number_2} = {par(number_1, number_2)}")
else:
	print("Invalid input")
