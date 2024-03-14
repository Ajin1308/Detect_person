import face_recognition
import numpy as np
import cv2
import mysql.connector
import image_blobs

db = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    password = 'Aswin@321',
    database = 'ajindb'
)

cam = cv2.VideoCapture(0)

# Function to fetch images from MySQL
def load_images_from_mysql():
    cursor = db.cursor()
    cursor.execute("SELECT image, name, address, phone FROM persons")
    rows = cursor.fetchall()
    known_face_encodings = []
    known_face_names = []

    for row in rows:
        image_blob = row[0]
        name = row[1]
        address = row[2]
        phone = row[3]

        # Convert blob to numpy array
        nparr = np.frombuffer(image_blob, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Compute face encoding
        face_encoding = face_recognition.face_encodings(img)[0]

        known_face_encodings.append(face_encoding)
        known_face_names.append(name)

    return known_face_encodings, known_face_names

known_face_encodings, known_face_names = load_images_from_mysql()

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    success, frame = cam.read()

    # Resize frame to speed up processing
    s_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_frame = s_frame[:, :, ::-1]

    if process_this_frame:
        # Find all the faces and face encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face matches any known face
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match is found, use the name associated with it
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with the name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()