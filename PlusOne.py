digits = list(map(int,input("enter the Digits").split()))

chk = "".join(map(str,digits)) #coverts the int input to string 
sum1 = str(int(chk) + 1) # converts str to int and add +1 
result = list(map(int,sum1))  #converts Back to list and int
print(result)
