#!/usr/bin/env python3
"""Test script pour vérifier que PySide6 est bien utilisé."""

print("Test du binding Qt...")

try:
	from PySide6 import QtWidgets, QtGui, QtCore
	print("✅ PySide6 importé avec succès!")
	print(f"Version Qt: {QtCore.QT_VERSION_STR}")
	print(f"Version PySide6: {QtCore.PYSIDE_VERSION_STR}")
	
	# Test simple de création d'application
	app = QtWidgets.QApplication([])
	print("✅ QApplication créée avec succès")
	
	# Test de compatibilité exec_()
	if hasattr(app, 'exec_'):
		print("✅ app.exec_() disponible")
	else:
		print("ℹ️ app.exec_() non disponible (normal pour Qt6), utilisation d'app.exec()")
		
	print("🎯 PySide6 fonctionne parfaitement!")
	
except ImportError as e:
	print(f"❌ Erreur d'import PySide6: {e}")
	print("Veuillez installer PySide6: pip install PySide6")
