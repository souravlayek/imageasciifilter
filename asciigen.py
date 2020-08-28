import sys
import math
from PIL import Image, ImageFont, ImageDraw

class ImgToAscii():
    def __init__(self):
        self.chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
        self.charList = list(self.chars)
        self.charlistLen = len(self.charList)
        self.interval = self.charlistLen/256
        self.filename = ""
        self.scalefactor = 0.1
        self.oneCharW = 8
        self.oneCharH = 18
        self.fnt = ImageFont.truetype("font.ttf",15)
        self.op_name = None
        self.ext_name = "png"
        self.op_img = None
    def input(self):
        print("enter the file location here \n")
        self.filename = input(">>   ")
    def getChar(self,iText):
        return self.charList[math.floor(iText*self.interval)]

    def getScaleFactor(self, width, height):
        if (width * height) > 90000:
            sf = 0.2
        else:
            sf = 0.5
        self.scalefactor = sf
    def process(self):
        try:
            print("========== processing start ===========")
            img = Image.open(self.filename)
            width, height = img.size
            self.getScaleFactor(width, height)
            img = img.resize((int(self.scalefactor*width),int(self.scalefactor*height*(self.oneCharW/self.oneCharH))),Image.NEAREST)
            width, height = img.size
            op_img = Image.new("RGB",(width*self.oneCharW,height*self.oneCharH),color=(0,0,0))
            d = ImageDraw.Draw(op_img)
            # load the image
            pix = img.load()
            for i in range(height):
                for j in range(width):
                    if img.mode == "RGBA":
                        r,g,b,a = pix[j,i]
                    else:
                        r,g,b = pix[j,i]
                    # convert grayscale image
                    gs = ((r+g+b)//3)
                    pix[j,i] = (gs, gs, gs)
                    d.text((j*self.oneCharW,i*self.oneCharH),self.getChar(gs),font=self.fnt, fill=(r,g,b))
            self.op_img = op_img
            print("========== Done ===========")
        except:
            print("========== Error ===========")
            exit()
    def output(self):
        op_file_name = input("enter rendered file name: eg-demo   :  ")
        self.op_name = op_file_name
        print("do you want yo change file to jpg default is png")
        ext = input("Type 'Y' if yes or 'N' for no  :   ")
        if ext.lower() == 'y':
            self.ext_name = 'jpg'
    def final_render(self):
        self.op_img.save(f"{self.op_name}.{self.ext_name}")
    def main(self):
        self.input()
        self.process()
        self.output()
        self.final_render()
    


def imgToAscii():
    try:
        ita = ImgToAscii()
        ita.main()
    except:
        print("sorry!! Process ending....")

if __name__ == "__main__":
    imgToAscii()