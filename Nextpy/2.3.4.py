class Pixel:
    def __init__(self,x=0,y=0,red=0,green=0,blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue


    def set_cords(self, x,y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) // 3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        print('X: ', self._x, ", Y: ", self._y, ", Color: (",self._red,",",self._green,",",self._blue,")")



if __name__ == "__main__":
    pix = Pixel(5,6,250,0,0)
    pix.print_pixel_info()
    pix.set_grayscale()
    pix.print_pixel_info()
