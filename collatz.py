import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLineEdit,  QLabel
import matplotlib.pyplot as plt

class App(QWidget):

    inputArr = []
    iterationsArr = []

    def __init__(self):
        super().__init__()
        self.title = 'Collatz simulator'
        self.setMinimumSize(400, 130) 
        self.label = QLabel(self)
        self.label.setText("Set sequence: ")
        self.label.move(20, 10)
        self.line = QLineEdit(self)
        self.line.move(20, 40)    
        self.button = QPushButton("Calculate", self)
        self.button.move(20, 80)
        self.button.clicked.connect(self.plot)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.show()

    def collatz(self, input):
        testNumber = input
        initial = input
        iterations = 0       
        print("now testing: " + str(testNumber))
        print(str(int(testNumber)))

        while testNumber != 1:
            if testNumber % 2 == 0: 
                testNumber/=2 
                print(str(int(testNumber)))

            else:
                testNumber*=3
                testNumber+=1
                print(str(int(testNumber)))

            iterations+=1

        print("tested number: " + str(initial))
        print("iterations: " + str(iterations))
        print("------------")

        self.inputArr.append(initial)
        self.iterationsArr.append(iterations)

    def plot(self):
        self.sequence = list(range(1, int(self.line.text())))
        for i in self.sequence:
            self.collatz(i)
  
        plt.figure(num="Simulation result")
        plt.plot(self.inputArr, self.iterationsArr)
        plt.ylabel("Iterations")
        plt.xlabel("Tested number(s)")  
        plt.show()

       
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())





  



