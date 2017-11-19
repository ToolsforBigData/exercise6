from PIL import Image
import numpy as np

# Function that takes with the image resized to (8,9) and greyscaled
# and returns the hash string of that image
# Input: The greyscaled resized image and the size of the image.
# Output: The hash string
def hashingFun(img,size):
    # Get the pixel values of the image into a numpy matrix as np.array([[],[]])
    pixel_values = np.array(list(img.getdata())).reshape(size)
    # Create the Difference matrix of the pixel values following rule:
    # Compare the adjacent values (x>y). True or False
    Diff_mat = np.diff(pixel_values,axis=1) < 0
    # Initialize the return string 
    retHashstring = ''
    # The hash function - Which through each list in the array (or the row of the array)
    # This function was created by David. Found here: https://app.aula.education/#/dashboard/XrBMVtIrG1/post/fy8PuLKzzn?_k=1ybbi8
    for difference in Diff_mat:
        # Initialize the dec value and the local hex_string
        decimal_value = 0
        hex_string = []
        # Loop trough each value of the row and the index of the value (True/False)
        for index, value in enumerate(difference):
            
            if value:
                # Append to the decimal value 2^(index % 8)
                decimal_value += 2**(index % 8)
                
            if (index % 8) == 7: # If you have reach the end of the row values
                # Convert the decimal value to heximal value and append 0 if the result from hex() is 0
                hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
                # reInitialize the decimal_value variable.
                decimal_value = 0
        # Append the hex_string of the specific row with the return value.
        retHashstring = retHashstring + hex_string[0]
    return retHashstring


#Size for resizing.
size = (8,9)
# Normal cat figure
Cat1_img = Image.open('cat1.png').convert('L')
Cat1_img = Cat1_img.resize(size)
Cat1_img.save('cat1_greyscaleles.png')
Cat1_Hash = hashingFun(Cat1_img,size)

# Cat figure change with having red nose.
Cat2_img = Image.open('cat2.png').convert('L')
Cat2_img = Cat2_img.resize(size)
Cat2_img.save('cat2_greyscaleles.png')
Cat2_Hash = hashingFun(Cat2_img,size)

# Org Superman
OrgSuper_img = Image.open('Org_Superman.jpg').convert('L')
OrgSuper_img = OrgSuper_img.resize(size)
OrgSuper_img.save('OrgSuper_greyscaleles.png')
OrgSuper_Hash = hashingFun(OrgSuper_img,size)

# Change Superman
ChangeSuper_img = Image.open('Change_Superman.jpg').convert('L')
ChangeSuper_img = ChangeSuper_img.resize(size)
ChangeSuper_img.save('ChangeSuper_greyscaleles.png')
ChangeSuper_Hash = hashingFun(ChangeSuper_img,size)

print('The hash for Orginal cat figure:\t {}'.format(Cat1_Hash))
print('The hash for cat with red nose:\t \t {}'.format(Cat2_Hash))
print('The hash for Orginal Superman figure:\t {}'.format(OrgSuper_Hash))
print('The hash for Change Superman figure:\t {}'.format(ChangeSuper_Hash))
