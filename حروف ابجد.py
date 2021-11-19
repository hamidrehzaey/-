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

class abjad(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(600, 250)
		self.setWindowTitle('تبدیل حروف ابجد به عدد')
		gridlayout = QGridLayout()
		self.setLayout(gridlayout)

		label = QLabel('این برنامه توسط حمید رضائی نوشته شده است.')
		gridlayout.addChildWidget(label)
		"""برای اینکه تمام جمله در کادر lable پیدا باشد طول lable رو 250 گذاشتم و چون توی یک خط هست عرض lable رو 20 گذاشتم
		حالا اگه 600 را منهای 250 کنیم میشه 350 و اگه تقسیم بر دو کنیم میشه 175
		مقدار فاصله از لبه سمت چپ رو 175 وارد کردم که lable دقیقا بیفته وسط
		مقدار عدد دوم که 20 هست فاصله از لبه بالا هست."""
		label.setGeometry(175, 20, 250, 20)

		entranceLabel = QLabel('حرف یا کلمه مورد نظر را وارد نمایید:')
		gridlayout.addChildWidget(entranceLabel)
		entranceLabel.setGeometry(80, 75, 170, 20)

		global entrance
		entrance = QLineEdit()
		entrance.setAccessibleName('حرف یا کلمه مورد نظر را وارد نمایید:')
		entrance.returnPressed.connect(self.Convert)
		gridlayout.addChildWidget(entrance)
		entrance.setGeometry(180, 100, 75, 40)

		convert = QPushButton('تبدیل کن')
		convert.clicked.connect(self.Convert)
		convert.setDefault(True)
		gridlayout.addChildWidget(convert)
		convert.setGeometry(250, 160, 100, 40)

		resultLabel = QLabel('نتیجه:')
		gridlayout.addChildWidget(resultLabel)
		resultLabel.setGeometry(335, 75, 75, 20)

		global result
		result = QLineEdit()
		result.setAccessibleName('نتیجه:')
		result.setReadOnly(True)
		result.returnPressed.connect(self.Convert)
		gridlayout.addChildWidget(result)
		result.setGeometry(335, 100, 75, 40)

	def Convert(self):
		newList = []
		try:
			for newString in entrance.text():
				letterNumbers = letters[newString]
				newList.append(letterNumbers)
		except:
			result.setText('مقدار وارد شده نادرست است.')

		if not newList == []:
			result.setText(str(sum(newList)))

		entrance.setText('')

app = QApplication(sys.argv)
window = abjd()
window.show()
app.exec()