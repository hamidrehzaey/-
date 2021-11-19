letters = {
	".":0,
	",":0,
	"?":0,
	"!":0,
	"،":0,
	"آ":1,
	"ؤ":6,
	"ئ":10,
	"ء":0,
	" ":0,
	"ا":1,
	"ب":2,
	"ج":3,
	"د":4,
	"ه":5,
	"و":6,
	"ز":7,
	"ح":8,
	"ط":9,
	"ی":10,
	"ک":20,
	"ل":30,
	"م":40,
	"ن":50,
	"س":60,
	"ع":70,
	"ف":80,
	"ص":90,
	"ق":100,
	"ر":200,
	"ش":300,
	"ت":400,
	"ث":500,
	"خ":600,
	"ذ":700,
	"ض":800,
	"ظ":900,
	"غ":1000,
	"گ":2000,
	"چ":3000,
	"پ":4000,
	"ژ":5000,
}
import sys
from PyQt6.QtWidgets import *

class abjd(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(600, 600)
		self.setWindowTitle('تبدیل حروف ابجد به عدد')
		gridlayout = QGridLayout()
		self.setLayout(gridlayout)

		label = QLabel('این برنامه توسط حمید رضائی نوشته شده است.')
		gridlayout.addChildWidget(label)
		label.setGeometry(250, 150, 100, 100)

		entranceLabel = QLabel('حرف یا کلمه مورد نظر را وارد نمایید:')
		gridlayout.addChildWidget(entranceLabel)
		entranceLabel.setGeometry(200, 300, 75, 50)

		global entrance
		entrance = QLineEdit()
		entrance.setAccessibleName('حرف یا کلمه مورد نظر را وارد نمایید:')
		entrance.returnPressed.connect(self.Convert)
		gridlayout.addChildWidget(entrance)
		entrance.setGeometry(200, 375, 75, 100)

		convert = QPushButton('تبدیل کن')
		convert.clicked.connect(self.Convert)
		convert.setDefault(True)
		gridlayout.addChildWidget(convert)
		convert.setGeometry(250, 500, 100, 50)

		resultLabel = QLabel('نتیجه:')
		gridlayout.addChildWidget(resultLabel)
		resultLabel.setGeometry(325, 300, 75, 50)

		global result
		result = QLineEdit()
		result.setAccessibleName('نتیجه:')
		result.setReadOnly(True)
		result.returnPressed.connect(self.Convert)
		gridlayout.addChildWidget(result)
		result.setGeometry(325, 375, 75, 100)

	def Convert(self):
		newList = []
		try:
			for newString in entrance.text():
				letterNumbers = letters[newString]
				newList.append(letterNumbers)
		except:
			result.setText('مقدار وارد شده نادرست است.')

		if newList == []:
			result.setText(str(sum(newList)))

		entrance.setText('')

app = QApplication(sys.argv)
window = abjd()
window.show()
app.exec()