ch = input("Enter a string: ")

firstCh = ch[0]
lastCh = ch[-1]

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
spacleChar = "!@#$%^&*()_+-=[]{};':\",.<>/?\\|`~ "
if(firstCh in alpha and lastCh in spacleChar):
  print("Yes")
else:
  print("No")