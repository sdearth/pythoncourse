try:
    file = open("a.txt")
    a_dictionary = {"key": "value"}
    x = a_dictionary["key"]
except FileNotFoundError:
    file = open("a.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    raise TypeError("This is a useless error")