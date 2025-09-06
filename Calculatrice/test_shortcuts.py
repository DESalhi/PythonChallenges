#!/usr/bin/env python3
"""Test des raccourcis clavier de la calculatrice PySide6."""

try:
	from PySide6 import QtWidgets, QtGui, QtCore
	print("✅ PySide6 importé avec succès")
except:
	print("❌ Erreur: PySide6 non disponible")
	exit(1)

def test_qshortcut():
	"""Test que QShortcut fonctionne avec PySide6."""
	try:
		app = QtWidgets.QApplication([])
		widget = QtWidgets.QWidget()
		
		# Test QShortcut dans QtGui (Qt6)
		shortcut = QtGui.QShortcut(QtGui.QKeySequence('Ctrl+Q'), widget)
		print("✅ QShortcut créé avec succès dans QtGui")
		
		# Test de la fonction de compatibilité
		def dummy_callback():
			pass
			
		def create_shortcut(key_sequence, parent, callback):
			try:
				return QtGui.QShortcut(QtGui.QKeySequence(key_sequence), parent, callback)
			except AttributeError:
				return QtWidgets.QShortcut(QtGui.QKeySequence(key_sequence), parent, callback)
		
		test_shortcut = create_shortcut('F1', widget, dummy_callback)
		print("✅ Fonction de compatibilité QShortcut fonctionne")
		
		return True
		
	except Exception as e:
		print(f"❌ Erreur QShortcut: {e}")
		return False

if __name__ == "__main__":
	print("🧪 Test des raccourcis clavier PySide6...")
	if test_qshortcut():
		print("🎯 Tous les tests QShortcut passent!")
	else:
		print("❌ Échec des tests QShortcut")
