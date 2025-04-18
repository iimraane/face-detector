# Détection de Visages en Temps Réel

## Description

Ce script utilise OpenCV pour accéder à la caméra système, détecter les visages à l’aide du classificateur Haar Cascade pré‑entraîné et dessiner un rectangle vert autour de chaque visage détecté en temps réel.

---

## Prérequis

- **Python 3.x**  
- Modules Python :

  ```bash
  pip install opencv-python
  ```

---

## Configuration

Aucune configuration externe nécessaire. Le fichier XML du classificateur est chargé depuis le package OpenCV :

```python
cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
```

---

## Structure

```
detector.py       # Détection basique et encadrement des visages
recognition.py    # (Optionnel) Reconnaissance faciale avec face_recognition
```

---

## Utilisation

1. Branchez et allumez votre caméra.  
2. Lancez le script :

   ```bash
   python detector.py
   ```

3. Une fenêtre nommée **Video** s’ouvre et affiche le flux caméra avec des rectangles verts autour des visages.  
4. Pour quitter, appuyez sur la touche `q`.

---

## Explication du code

1. **Chargement du classificateur**  
   ```python
   face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
   ```
2. **Capture vidéo**  
   ```python
   video_capture = cv2.VideoCapture(0)
   ```
3. **Boucle principale** :  
   - Lecture d’une image (`read()`)  
   - Conversion en niveaux de gris (`cvtColor`)  
   - Détection des visages (`detectMultiScale`)  
   - Dessin de rectangles verts (`rectangle`)  
   - Affichage (`imshow`)  
4. **Arrêt** :  
   - Sortie de boucle sur `q`  
   - Libération des ressources (`release()`, `destroyAllWindows()`)

---

## Personnalisation

- **Paramètres de détection** :  
  - `scaleFactor` (zoom)  
  - `minNeighbors` (robustesse)  
  - `minSize` (taille minimale)  
- **Apparence du rectangle** : modifier la couleur ou l’épaisseur du tracé.  
- **Résolution vidéo** : utiliser `cap.set(cv2.CAP_PROP_FRAME_WIDTH, …)` et `CAP_PROP_FRAME_HEIGHT`.

---

## Dépannage

- **Caméra non détectée** :  
  - Vérifiez l’indice du périphérique (`0`, `1`, etc.).  
  - Assurez‑vous que le module caméra est libre.  
- **Lenteur ou plantage** :  
  - Réduisez la résolution de capture.  
  - Ajustez les paramètres du classificateur.  
- **Aucun visage détecté** :  
  - Testez avec des conditions d’éclairage différentes.  
  - Réduisez `minNeighbors` et `minSize`.

---

## Licence

Please just don't steal my code..
