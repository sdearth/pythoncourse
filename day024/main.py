# with manages the file - closes it when done
with open("/Users/sdearth/Desktop/my_file.txt" ) as file:
    contents = file.read()
    print(contents)

# open for append
with open("/Users/sdearth/Desktop/my_file.txt", mode="a") as file:
    file.write("\nnew text")