
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
        print("OK")
        

    
a = RotateImage()
a.rotate([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
        
