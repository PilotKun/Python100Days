with open("file1.txt", "r") as file1:
    file1data = file1.readlines()

with open("file2.txt", "r") as file2:
    file2data = file2.readlines() 

result = [int(num) for num in file1data if num in file2data]

# write your code above

print(result)