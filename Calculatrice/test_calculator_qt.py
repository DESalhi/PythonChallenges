#!/usr/bin/env python3
"""Quick test to show which Qt binding the calculator will use."""

# Same import logic as the calculator
try:
	from PySide2 import QtWidgets, QtGui, QtCore
	_QT_BINDING = 'PySide2'
except ModuleNotFoundError:
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
					"No Qt binding found. Please install one of: PySide2, PySide6, PyQt5, or PyQt6.\n"
					"Example: pip install PySide6"
				)

print(f"✅ Calculator will use Qt binding: {_QT_BINDING}")
print(f"Qt version: {getattr(QtCore, 'QT_VERSION_STR', 'Unknown')}")

# Test font weight compatibility
font = QtGui.QFont()
try:
	# Test Qt5 style
	font.setWeight(75)
	print("✅ Qt5-style font.setWeight(75) works")
except TypeError:
	try:
		# Test Qt6 style  
		font.setWeight(QtGui.QFont.Weight.Bold)
		print("✅ Qt6-style font.setWeight(Font.Weight.Bold) works")
	except:
		print("⚠️  Font weight setting may have issues")

print("🎯 Calculator should work correctly!")
