# 1.
write_file = open("name.txt", "w")
name = input("your name?")
print(name, file=write_file)
write_file.close()
# 2.
read_file = open("name.txt", "r")
name = read_file.read().split()
read_file.close()
print(f"Your name is {name}")
# 3.
read_file = open("numbers.txt", "r")
num1 = int(read_file.readline())
num2 = int(read_file.readline())
read_file.close()
print(num1 + num2)
# 4.
read_file = open("numbers.txt", "r")
sum_of_num = 0
for line in read_file:
    num = int(line)
    sum_of_num = sum_of_num + num
print(sum_of_num)
