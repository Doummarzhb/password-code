import random
pin= random.randint(1000,9999)
userinput =int(input("enterr 4 digit pin code"))

if   len(str(userinput))!=4:
# len(str(userinput)) >4 or len(str(userinput))<4:
    print("please enter 4 digit")
elif userinput ==pin:
    peint("success ,,, pin code matched")
else:
    print("failure pin code did not match")
    print("the computer generatedthis pin :{pin}")