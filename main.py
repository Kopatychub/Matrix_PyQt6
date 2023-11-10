from PyQt6.QtWidgets import QApplication, QMainWindow
from win import Ui_MainWindow

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        
        self.ui.pushButton.clicked.connect(self.set_nums)
        
    def initUI(self):
        self.setWindowTitle('Matrix')
        
    def set_nums(self):
        def u(n):
                if n < 0:
                    return ''
                else:
                    return '+'
        def decision(m):
            a=m[0]*m[4]*m[8]
            b=m[3]*m[7]*m[2]
            c=m[1]*m[5]*m[6]
            
            d=m[2]*m[4]*m[6]
            i=m[0]*m[5]*m[7]
            f=m[1]*m[3]*m[8]

            
            txt = f'{a}{u(b)}{b}{u(c)}{c}{u(d*(-1))}{d*(-1)}{u(i*(-1))}{i*(-1)}{u(f*(-1))}{f*(-1)}'
            print(txt)
            
            summ = eval(txt)
            
            return [txt, summ]
        
        
        matrix = [int(getattr(self.ui, f'lineEdit_{i+1}').text()) for i in range(12)]
        
        
        mat = []            
        # delta 
        for i in range(9):
            object_name = f'del_{i+1}'
            getattr(self.ui, object_name).setText(str(matrix[i]))
            mat.append(matrix[i])
            
        self.ui.del_des.setText(decision(mat)[0] +" = "+str(decision(mat)[1])) 
        
        
        mat = []            
        # delta x
        for i in range(9):
            object_name = f'delx_{i+1}'
                        
            match i:
                case 0:
                    getattr(self.ui, object_name).setText(str(matrix[9]))
                    mat.append(matrix[9])
                case 3:
                    getattr(self.ui, object_name).setText(str(matrix[10]))
                    mat.append(matrix[10])
                case 6:
                    getattr(self.ui, object_name).setText(str(matrix[11]))
                    mat.append(matrix[11])
                case _:
                    getattr(self.ui, object_name).setText(str(matrix[i]))
                    mat.append(matrix[i])
                    
        self.ui.delx_des.setText(decision(mat)[0] +" = "+str(decision(mat)[1])) 

        
        
        mat = []            
        # delta y
        for i in range(9):
            object_name = f'dely_{i+1}'
                        
            match i:
                case 1:
                    getattr(self.ui, object_name).setText(str(matrix[9]))
                    mat.append(matrix[9])
                case 4:
                    getattr(self.ui, object_name).setText(str(matrix[10]))
                    mat.append(matrix[10])
                case 7:
                    getattr(self.ui, object_name).setText(str(matrix[11]))
                    mat.append(matrix[11])
                case _:
                    getattr(self.ui, object_name).setText(str(matrix[i]))
                    mat.append(matrix[i])
                    
        self.ui.dely_des.setText(decision(mat)[0] +" = "+str(decision(mat)[1])) 

        
        
        mat = []            
        # delta z
        for i in range(9):
            object_name = f'delz_{i+1}'
            
            match i:
                case 2:
                    getattr(self.ui, object_name).setText(str(matrix[9]))
                    mat.append(matrix[9])
                case 5:
                    getattr(self.ui, object_name).setText(str(matrix[10]))
                    mat.append(matrix[10])
                case 8:
                    getattr(self.ui, object_name).setText(str(matrix[11]))
                    mat.append(matrix[11])
                case _:
                    getattr(self.ui, object_name).setText(str(matrix[i]))
                    mat.append(matrix[i])
                    
        self.ui.delz_des.setText(decision(mat)[0] +" = "+str(decision(mat)[1])) 


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()          