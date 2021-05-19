#question number 1
# user input tempertaure in fahrenheit

temp = input("Input the  temperature in f or c units: ")
degree = int(temp[:-1])
i = temp[-1]

if i.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  t = "Celsius"

# if improper units, tell user to input proper convention
else:
  print("Input proper convention.")
  quit()
print("The temperature in", t, "is", result, "degrees.")



# question number 2
# user input tempertaure in fahrenheit or celsius
temp = input("Input the  temperature in f or c units: ")
degree = int(temp[:-1])
i = temp[-1]

# if entered with c units, convert to fahrenheit
if i.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  t = "Fahrenheit"

  # if not, convert to celsius
elif i.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  t = "Celsius"

# if improper units, tell user to input proper convention
else:
  print("Input proper convention.")
  quit()
print("The temperature in", t, "is", result, "degrees.")


# question number 3
n = str(input("Enter words, when x is pressed, the number of words that were typed will be printed"))

#if the x key is pressed
if x key pressed:
#count number of words
  res = len(n.split())
  
# print number of words
print ("The number of words in string are : " +  str(res))
# end the program
end

# question number 4
# set password
password = ("1234")
guess = input("Enter the password: ")
while guess != password:
    print ("incorrect password")
    guess = input("Enter the password: ")
    if guess == password:
        print ("Login successful!")


# question number 5
# set count and create list
count = 0
lis = []
# create loop
while count <= 9: 
    number=input("Enter a number: ")
    count += 1
    lis.append(number)
print ("The numbers you entered were: ")
# print each number on a seperate line
print ("\n".join(lis))