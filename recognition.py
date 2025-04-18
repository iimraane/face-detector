import cv2
import face_recognition

# Charger une image de référence et l'encoder
image_reference = face_recognition.load_image_file("ton_image_reference.jpg")
encoding_reference = face_recognition.face_encodings(image_reference)[0]

# Initialiser la caméra
video_capture = cv2.VideoCapture(0)

while True:
    # Lire une image depuis la caméra
    ret, frame = video_capture.read()
    
    # Convertir l'image en RGB pour face_recognition
    rgb_frame = frame[:, :, ::-1]
    
    # Détection des visages et encodage
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Comparer les visages
        matches = face_recognition.compare_faces([encoding_reference], face_encoding)
        name = "Inconnu"
        
        if True in matches:
            name = "Nom du visage connu"
        
        # Dessiner un rectangle autour du visage
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        
        # Ajouter le nom
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Afficher la vidéo
    cv2.imshow('Video', frame)
    
    # Quitter avec 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
video_capture.release()
cv2.destroyAllWindows()
