a = float(input("Write the first number: "))
b = float(input("Write the second number: "))
oper = input("Select the basic operator(+,-, *,/) ")

if oper == "+":
    print(a+b)
elif oper == "-":
    print(a-b)
elif oper == "*":
    print(a*b)
elif oper == "/":
    print(a/b)
else:
    print("Wrong operator entry!")