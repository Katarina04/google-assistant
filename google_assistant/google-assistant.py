import speech_recognition as sr
import pyttsx3
from googlesearch import search
import pyaudio

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

# Contoh penggunaan
speak("Halo, saya Google Assistant. Apa yang bisa saya bantu?")
input_text = listen()
speak("Anda mengatakan: " + input_text)


# menambahkan fungsi pencarian menggunakan Google dengan menggunakan modul googlesearch-python

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
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()

def google_search(query, num_results):
  speak("Saya mencari informasi mengenai " + query)
  results = list(search(query, lang="id", stop=num_results)) # Menggunakan googlesearch untuk mencari
  speak("Berikut adalah beberapa hasil yang saya temukan:")
  return results[:num_results]

# Contoh penggunaan

speak("Halo, saya Google Assistant. Apa yang bisa saya bantu?")
input_text = listen()
num_results = 3
search_results = google_search(input_text, num_results)

for result in search_results:
  print(result)