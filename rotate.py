
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

        # the input matrix is rotated by going through the elements in spiraling
        # fashion, each 4 sides in one go. The algorithm works on both matrices
        # having even and odd number of rows.
        rounds = len(input_image)-1
        for i in range(int(len(input_image)/2)):
            for j in range(i, rounds-i):
                swap = input_image[i][j]
                input_image[i][j] = input_image[rounds-j][i]
                input_image[rounds-j][i] = input_image[rounds-i][rounds-j]
                input_image[rounds-i][rounds-j] = input_image[j][rounds-i]
                input_image[j][rounds-i] = swap
        return True
            
    def show(self, image):
        for x in range(len(image)):
            for y in range(len(image)):
                print(str(image[x][y]) + " ", end = '')
            print()
        print()

        
# --- test the image rotation with two small images 

a = RotateImage()
image1 = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
image2 = [ [1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16] ]

a.show(image1)
a.rotate(image1)
a.show(image1)   
a.show(image2)
a.rotate(image2)
a.show(image2)
