
#for loop demostraiting range
print("My name is")
for i in range(5):
    print('Jimmy Five Times(' + str(i) + ')')

#adds all numbers from 0 to 100, answer is 5050
total = 0
for num in range(101):
    total = total +num
print(total)

#while loop example
print('My Name is')
i = 0
while i < 5:
    print('Jimmy Five Times(' + str(i) + ')')
    i = i + 1

#range is an arguement that can be seperated by a comma.
for i in range (12,16):
    print(i)

#range can be called with 3 arguements, the first 2 values are the start
#and the stop, the third is the step, which is the ammount it increases by
for i in range (0,10,2):
        print (i)

#this will count down by 1
for i in range (5, -1, -1):
    print(i)