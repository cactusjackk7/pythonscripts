#usr/bin/python3
# taking kms input from user
kilometers = float(input("Enter value in kms: "))

#conversion factor
conv_fac = 0.621371

#calculate files
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
