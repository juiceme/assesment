
class RotateImage:
    """Rotates a N*N bitmap image in place"""
    def rotate(self, input_image):
        if type(input_image) is not list:
            print("Input is not a bitmap in 2-dimensional list format")
            return False
        if type(input_image[0]) is not list:
            print("Input is not a bitmap in 2-dimensional list format")
            return False
        if len(input_image) is not len(input_image[0]):
            print("Input image needs to be N*N square array")
            return False
        
        # Check whether the array is even or odd, this is needed to determine
        # if the center pixel need to be rotated or not
        if len(input_image) % 2 == 0:
            rounds = len(input_image)-1
            for i in range(int(len(input_image)/2)):
                for j in range(i, rounds-i):
                    swap = input_image[i][j]
                    input_image[i][j] = input_image[rounds-j][i]
                    input_image[rounds-j][i] = input_image[rounds-i][rounds-j]
                    input_image[rounds-i][rounds-j] = input_image[j][rounds-i]
                    input_image[j][rounds-i] = swap
            return input_image

def printimage(image):
    for x in range(len(image)):
        for y in range(len(image)):
            print(str(image[x][y]) + " ", end = '')
        print()
    print()

    
a = RotateImage()
image1 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
image2 = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16] ]
#output1 = a.rotate(image1)
printimage(image2)
output2 = a.rotate(image2)
printimage(output2)
        
