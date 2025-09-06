# Calculatrice - Configuration PySide6

## Configuration actuelle ✅

La calculatrice utilise maintenant **PySide6** comme binding Qt principal.

## Modifications apportées

### 1. Binding Qt principal: PySide6
- **Fichiers modifiés**: `Calculatrice.py` et `custom_ui/fenetrePrincipale.py`
- **Changement**: PySide6 est maintenant le premier choix (au lieu de PySide2)
- **Ordre de priorité**:
  1. **PySide6** (Qt6) - Binding principal recommandé
  2. PyQt5 (Qt5) - Fallback si PySide6 non disponible
  3. PyQt6 (Qt6) - Alternative Qt6

### 2. Suppression de PySide2
- PySide2 (Qt5) a été retiré du code
- Le code est maintenant optimisé pour Qt6
- Meilleure compatibilité avec les systèmes modernes

### 3. Optimisations Qt6
- Gestion native de `app.exec()` vs `app.exec_()`
- Compatibilité des fonts entre Qt5/Qt6
- Messages d'erreur simplifiés

### 2. Compatibilité Qt5/Qt6
- **Problème**: `font.setWeight(75)` ne fonctionne qu'avec Qt5, Qt6 nécessite un enum
- **Solution**: Fonction de compatibilité qui essaie les deux syntaxes

### 3. Compatibilité exec_()
- **Problème**: Qt6 a renommé `exec_()` en `exec()`
- **Solution**: Alias de compatibilité pour tous les bindings Qt6

## Comment utiliser

### Lancer la calculatrice
```bash
python Calculatrice.py
```

### Fonctionnalités
- Interface graphique complète avec boutons numériques
- Opérations de base: +, -, *, /
- Raccourcis clavier pour tous les boutons
- Formatage des grands nombres avec espaces

### Raccourcis clavier
- `0-9`: Chiffres
- `+`, `-`, `*`, `/`: Opérations
- `Enter`: Égal (=)
- `Esc`: Fermer l'application
- `Del`: Effacer (C)

## Bindings Qt supportés

Le code fonctionne maintenant avec n'importe lequel de ces bindings Qt:
- ✅ **PySide2** (Qt5) - Original mais non installé
- ✅ **PySide6** (Qt6) - Recommandé pour nouveaux projets  
- ✅ **PyQt5** (Qt5) - Alternative stable
- ✅ **PyQt6** (Qt6) - Version moderne

## Installation des dépendances

Si vous n'avez aucun binding Qt installé:

```bash
# Option recommandée - PySide6 (Qt6)
pip install PySide6

# Ou PyQt5 si vous préférez Qt5
pip install PyQt5

# Ou PyQt6 pour la dernière version
pip install PyQt6
```

## Test de compatibilité

Un script de test est inclus pour vérifier quel binding sera utilisé:
```bash
python test_calculator_qt.py
```
