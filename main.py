import sys
from PyQt5 import uic, QtWidgets
from nltk_gender import *
from nltk_sentiment_analysis import *


qtCreatorFile = "mainwindow.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Eventos en la interfaz
        self.buttonTokenize.clicked.connect(self.tokenize)

    #Logica del button
    def tokenize(self):
        input = self.textEditInput.toPlainText()
        combo = self.comboBox.currentText()
        if(combo=="Predice gender"):
            self.textEditOutput.setText(predictionGender(input))
        else:
            self.textEditOutput.setText(sentiment(input))

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

