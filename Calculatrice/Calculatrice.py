try:
	from PySide6 import QtWidgets, QtGui, QtCore
	_QT_BINDING = 'PySide6'
except (ModuleNotFoundError, ImportError):
	try:
		from PyQt5 import QtWidgets, QtGui, QtCore
		_QT_BINDING = 'PyQt5'
	except (ModuleNotFoundError, ImportError):
		try:
			from PyQt6 import QtWidgets, QtGui, QtCore
			_QT_BINDING = 'PyQt6'
		except (ModuleNotFoundError, ImportError):
			raise ModuleNotFoundError(
				"No Qt binding found. Please install PySide6:\n"
				"pip install PySide6"
			)
from functools import partial
from custom_ui.fenetrePrincipale import Ui_form_calculatrice

# Fonction de compatibilité pour QShortcut entre Qt5 et Qt6
def create_shortcut(key_sequence, parent, callback):
	"""Crée un QShortcut compatible Qt5/Qt6."""
	try:
		# Qt6: QShortcut est dans QtGui
		return QtGui.QShortcut(QtGui.QKeySequence(key_sequence), parent, callback)
	except AttributeError:
		# Qt5: QShortcut peut être dans QtWidgets
		return QtWidgets.QShortcut(QtGui.QKeySequence(key_sequence), parent, callback)

# Formate les nombres avec des espaces (ex : 76120 = 76 120)
def formatNumberResult(x):
	if isinstance(x, int):
		x = int(x)
	else:
		x = float(x)
	return '{:,}'.format(x).replace(',', ' ')

class Calculatrice(Ui_form_calculatrice, QtWidgets.QWidget):
	def __init__(self):
		super(Calculatrice, self).__init__()
		self.setupUi(self)
		self.modificationSetupUi()
		self.setupConnections()
		self.setupRaccourcisClavier()
		self.show()

	def modificationSetupUi(self):
		self.btns_nombres = [] # liste qui contient tout les chiffres de 0 à 9
		for i in range(self.gridLayout.count()):
			widget = self.gridLayout.itemAt(i).widget()
			if isinstance(widget, QtWidgets.QPushButton):
				widget.setStyleSheet('QPushButton:hover {color: #5b5c5c;}')
				if widget.text().isdigit(): 
					self.btns_nombres.append(widget) 

	def setupConnections(self):
		for btn in self.btns_nombres:
			btn.clicked.connect(partial(self.btnNombrePressed, btn.text()))

		self.btn_moins.clicked.connect(partial(self.btnOperationPressed, '-'))
		self.btn_plus.clicked.connect(partial(self.btnOperationPressed, '+'))
		self.btn_mult.clicked.connect(partial(self.btnOperationPressed, '*'))
		self.btn_div.clicked.connect(partial(self.btnOperationPressed, '/'))
		self.btn_point.clicked.connect(partial(self.btnOperationPressed, '.'))

		self.btn_egal.clicked.connect(self.calculOperation)
		self.btn_c.clicked.connect(self.supprimerResultat)

	def setupRaccourcisClavier(self):
		for btn in range(10):
			create_shortcut(btn, self, partial(self.btnNombrePressed, btn))

		create_shortcut('+', self, partial(self.btnOperationPressed, '+'))
		create_shortcut('-', self, partial(self.btnOperationPressed, '-'))
		create_shortcut('*', self, partial(self.btnOperationPressed, '*'))
		create_shortcut('/', self, partial(self.btnOperationPressed, '/'))
		create_shortcut('.', self, partial(self.btnOperationPressed, '.'))
		
		create_shortcut('Esc', self, self.close)
		create_shortcut('Return', self, self.calculOperation)
		create_shortcut('Enter', self, self.calculOperation)
		create_shortcut('Del', self, self.supprimerResultat) 

	def btnNombrePressed(self, bouton):
		"""Fonction activée quand l'utilisateur appuie sur un chiffre (0-9)"""
		resultat = self.le_resultat.text()
		if resultat == '0':
			self.le_resultat.setText(bouton)
		else:
			self.le_resultat.setText(resultat + bouton)

	def btnOperationPressed(self, operation):
		"""Fonction activée quand l'utilisateur appuie sur une touche d'opération (+, -, /, *)"""
		resultat = self.le_resultat.text()
		self.le_resultat.setText(resultat + " " + operation + " ")

	def supprimerResultat(self):
		"""On reset le texte des deux LineEdit"""
		self.le_resultat.setText('0')
		self.le_operation.setText('')

	def calculOperation(self):
		resultat = self.le_resultat.text()

		# On ajoute le nombre actuel dans le LineEdit resultat au LineEdit operation
		self.le_operation.setText(resultat)
		
		# On evalue (et calcule) le resultat de l'opération
		resultatOperation = eval(self.le_operation.text().replace(" ", ""))
		
		# On met le resultat final dans le LineEdit resultat
		self.le_resultat.setText(formatNumberResult(resultatOperation))

app = QtWidgets.QApplication([])
fenetre = Calculatrice()
# PySide6/PyQt6 renamed exec_ to exec; provide compatibility alias
# so older code calling exec_ continues to work regardless of the binding used.
if _QT_BINDING in ('PySide6', 'PyQt6'):
	if not hasattr(app, 'exec_'):
		app.exec_ = app.exec

app.exec_()