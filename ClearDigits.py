def remove_digits(s):
    arr = []  

    for char in s:
        if char.isdigit():
            if arr: 
                arr.pop()
        else:
            arr.append(char)

    return "".join(arr)


print(remove_digits("abc")) 
print(remove_digits("abc123")) 
print(remove_digits("hello5world")) 
print(remove_digits("1234")) 
print(remove_digits("ab3cd5ef7g")) 