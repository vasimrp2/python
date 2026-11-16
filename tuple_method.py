fruit = ("Apple","Banana","Mango","Apple","Grapes","Apple")
print(fruit)
print(fruit.count("Apple"))  # return 3
print(fruit.count("apple"))  # return 0 becoz count taken case sensative name.
print(fruit[3]) # take whose index is 3
print(fruit[0:2]) # take only items between index 0 and 2
print(fruit[1:]) # take all from index 1

#implicit tuple
arr = "a","b","c","d"
print(arr)
print(arr[2])
print(arr[0:3])
print(arr[1:3])

# nested tuple
arr1 = (("vasim","36"),("Wajid","35"),("Azim","33"))
print(arr1)
print(arr1[0])
print(f"{arr1[0][0]} - {arr1[0][1]}")
print(f"{arr1[2][0]} - {arr1[2][1]}")