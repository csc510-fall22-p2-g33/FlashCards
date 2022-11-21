import pyrebase

config = {
  'apiKey': "AIzaSyAQjigaQ9FS1UlSAeGwZmIkoWnv0AnqvEU",
  'authDomain': "flashcards-test-7fbf8.firebaseapp.com",
  'databaseURL': "https://flashcards-test-7fbf8-default-rtdb.firebaseio.com",
  'projectId': "flashcards-test-7fbf8",
  'storageBucket': "flashcards-test-7fbf8.appspot.com",
  'messagingSenderId': "506242405702",
  'appId': "1:506242405702:web:2e9349c19e3ed314704147",
  'measurementId': "G-5LBEP5LQTH"
}

firebase = pyrebase.initialize_app(config)