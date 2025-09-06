#!/usr/bin/env python3
"""Test script to verify Qt binding imports work correctly."""

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

print(f"✅ Successfully imported Qt binding: {_QT_BINDING}")
print(f"QtWidgets module: {QtWidgets}")
print(f"QtCore.QT_VERSION_STR: {getattr(QtCore, 'QT_VERSION_STR', 'N/A')}")

# Test creating a simple widget
app = QtWidgets.QApplication([])
widget = QtWidgets.QLabel("Test Qt Import - Success!")
print(f"✅ Created QLabel widget: {widget}")
print("Qt binding is working correctly!")
