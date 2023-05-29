import speech_recognition as sr
import pyttsx3
import cv2
import face_recognition

# Inisialisasi recognizer dan engine TTS
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def listen():
  with sr.Microphone() as source:
    print("Silakan bicara...")
    recognizer.adjust_for_ambient_noise(source) # Menghilangkan noise dari lingkungan sekitar
    audio = recognizer.listen(source) # Mendengarkan suara dari mikrofon
 
  try:
    text = recognizer.recognize_google(audio, language="id-ID") # Menggunakan Google Speech Recognition API
    print("Anda mengatakan:", text)
    return text
  except sr.UnknownValueError:
    print("Maaf, tidak dapat mengenali suara Anda.")
  except sr.RequestError:
    print("Maaf, terjadi kesalahan pada koneksi ke layanan Google Speech Recognition.")
    return ""
  
def speak(text):
 engine.say(text)
 engine.runAndWait()

def face_recognition_demo():
 # Load gambar wajah yang akan dienkode
 known_image = face_recognition.load_image_file("known_face.jpg")
 known_encoding = face_recognition.face_encodings(known_image)[0]
 
 # Menginisialisasi kamera
 video_capture = cv2.VideoCapture(0)

 while True:
   
   # Membaca frame dari kamera
   ret, frame = video_capture.read()

   # Mengubah format frame dari BGR ke RGB
   rgb_frame = frame[:, :, ::-1]

   # Mencari lokasi wajah dalam frame
   face_locations = face_recognition.face_locations(rgb_frame)
   face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
   
   for face_encoding in face_encodings:
     # Membandingkan wajah dengan wajah yang telah dienkode
     matches = face_recognition.compare_faces([known_encoding], face_encoding)
 
     if True in matches:
       speak("Wajah dikenali")
     else:
       speak("Wajah tidak dikenali")

   # Menampilkan frame dengan kotak bingkai di sekitar wajah
   for (top, right, bottom, left) in face_locations:
     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
 
   # Menampilkan frame
   cv2.imshow('Video', frame)

   # Keluar dari loop jika tombol 'q' ditekan
   if cv2.waitKey(1) & 0xFF == ord('q'):
     break
   
 # Melepas sumber daya kamera dan menutup jendela
 video_capture.release()
 cv2.destroyAllWindows()

# Contoh penggunaan
speak("Halo, saya Google Assistant. Apa yang bisa saya bantu?")
input_text = listen()
speak("Anda mengatakan: " + input_text)

if "wajah" in input_text.lower():
  speak("Silakan hadapkan wajah Anda ke kamera")
  face_recognition_demo()
else:
  speak("Maaf, saya hanya bisa membantu dengan pengenalan wajah saatini.")