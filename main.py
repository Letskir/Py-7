from PyQt5.QtWidgets import QApplication                        
from PyQt5.QtWidgets import QMainWindow, QMessageBox              
from PyQt5.QtWidgets import QFileDialog     
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt  
from PIL import Image, ImageFilter
from ui import Ui_main_win         
import os


                                                       
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main_win()
        self.ui.setupUi(self)


app = QApplication([])
ex = Widget()

ex.show()
     
class ImageProccesor():
    def __init__(self):
        self.current_image =  None
        self.name_file = None
        self.papka_images= "\obrob"
        self.a=False
    
    def load_images(self, filename):
        self.filename= filename
        image_path=os.path.join(workdir,filename)
        self.image = Image.open(image_path)

    def preview(self, path):
        ex.ui.photo_lab.hide()
        pixmapimage=QPixmap(path)
        w, h =ex.ui.photo_lab.width(), ex.ui.photo_lab.height()
        pixmapimage=pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        ex.ui.photo_lab.setPixmap(pixmapimage)
        ex.ui.photo_lab.show()
        self.a = True
    
    def saveImage(self):
        path =os.path.join(workdir, self.papka_images)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path=os.path.join(path, self.filename)
        self.image.save(image_path)
    
    def do_bw(self):
        if self.a:
            self.image=self.image.convert("L")
            self.saveImage()
            image_path=os.path.join(workdir, self.papka_images, self.filename)
            self.preview(image_path)

    def do_blur(self): 
        if self.a:
            self.image=self.image.filter(ImageFilter.BLUR)
            self.saveImage()
            image_path=os.path.join(workdir, self.papka_images, self.filename)
            self.preview(image_path)

    def do_mirrow(self):
        if self.a:
            self.image= self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.saveImage()
            image_path=os.path.join(workdir, self.papka_images, self.filename)
            self.preview(image_path)
        
    def do_left(self):
        if self.a:
            self.image= self.image.rotate(90)
            self.saveImage()
            image_path=os.path.join(workdir, self.papka_images, self.filename)
            self.preview(image_path)
        
    def do_right(self):
        if self.a:
            self.image= self.image.rotate(-90)
            self.saveImage()
            image_path=os.path.join(workdir, self.papka_images, self.filename)
            self.preview(image_path)
    
    def do_save(self):
        if self.a:
            save_dir=QFileDialog.getExistingDirectory()
            image_path = os.path.join(save_dir, "changed_"+self.filename) 
            self.image.save(image_path)
filename=""
workdir=""
extensions=[".png", ".jpg"]
work_image=ImageProccesor()
def filter(extensions):
    global filename,workdir
    workdir=QFileDialog.getExistingDirectory()
    if workdir!="":
        filename=os.listdir(workdir)
        result=[]
        for file in filename:
            for ext in extensions:
                if file.endswith(ext):
                    result.append(file)
        ex.ui.photo_list.addItems(result)

def test():
     global filename,workdir
     ex.ui.photo_list.clear()
     filter(extensions)
                
def showChoseImage():
    if ex.ui.photo_list.currentRow() >=0:
        filename = ex.ui.photo_list.currentItem().text()
        work_image.load_images(filename)
        image_path=os.path.join(workdir,filename)
        work_image.preview(image_path)
        
ex.ui.photo_list.currentRowChanged.connect(showChoseImage)

ex.ui.white_black_btn.clicked.connect(work_image.do_bw)

ex.ui.blur_btn.clicked.connect(work_image.do_blur) 

ex.ui.mirrow_btn.clicked.connect(work_image.do_mirrow)

ex.ui.left_btn.clicked.connect(work_image.do_left)

ex.ui.right_btn.clicked.connect(work_image.do_right)

ex.ui.save_btn.clicked.connect(work_image.do_save)

ex.ui.photo_files.clicked.connect(test)




app.exec_() 