#D:\study\prac\Scripts\activate
import cv2
import mediapipe as mp

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from gethands import gethan
camwidth=640
camheight=480

camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)
if not camera.isOpened():
    print("Cannot open webcam")
    #exit()
else :
    print("camera is ON")

                


class Window(QMainWindow):

    def __init__(self):
            super().__init__()

            # set the title
            self.setWindowTitle("Drawscream")
            
            # setting geometry to main window
            #self.setGeometry(100, 100, 800, 600)

            #settings for window
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            
            # default brush size
            self.brushSize = 2
		    # default color
            self.brushColor = Qt.green
            # variables
            # drawing flag
            self.drawing = False

            # QPoint object to tract the point
            self.lastPoint = QPoint(0,0)
            print(self.lastPoint.x(), self.lastPoint.y())
            
            mainMenu = self.menuBar()
            menu = mainMenu.addMenu("menu")
            clear = QAction("clear", self)
            menu.addAction(clear)
            clear.triggered.connect(self.clear)

            closeit= mainMenu.addMenu("close")
            c=QAction("closeit", self)
            closeit.addAction(c)
            closeit.triggered.connect(self.closeit)

            mainMenu.addMenu("PRESS & HOLD SPACE") #instructions
            # creating image object
            self.image = QImage(self.size(), QImage.Format_RGB32)
        
		    # making image color to white
            #self.image.fill(Qt.white)
            
            # setting the geometry of window
            self.showMaximized() 
    
    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
        
    
    def clear(self):
        # make the whole canvas white
        self.image = QImage(self.size(), QImage.Format_RGB32)
		# update
        self.update()



    def keyPressEvent(self, event):
        
        self.drawing=True
        painter = QPainter(self.image)
        
        #painter.begin(self)
        painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        finger=gethan(camwidth, camheight, camera)

        if finger != (0,0) :
            
            print("finger={}".format(finger))
            nextPoint=QPoint()
            nextPoint.setX(finger[0])
            nextPoint.setY(finger[1])
            #print(self.lastPoint, nextPoint)
            painter.drawLine(self.lastPoint, nextPoint)
            
            self.lastPoint=nextPoint
            self.update()
        else:
            print("non")
    
    def closeit(self):
        self.close()
        
    




if __name__ == '__main__':
    
    App = QApplication(sys.argv)
    # create the instance of our Window
    window = Window()
    window.show()
    sys.exit(App.exec())
    