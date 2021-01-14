#usr/bin/python3
# python program to swap 2 vars

x = 5
y = 10

# to take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

#create a temporary var and swap values
temp = x
x = y
y = temp

print('The values of x after swapping: {}'.format(x))
print('The values of y after swapping: {}'.format(y))
