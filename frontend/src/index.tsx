import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App'
import './index.scss'
import reportWebVitals from './reportWebVitals'
import { initializeApp } from 'firebase/app';

const firebaseConfig = {
  apiKey: "AIzaSyAQjigaQ9FS1UlSAeGwZmIkoWnv0AnqvEU",
  authDomain: "flashcards-test-7fbf8.firebaseapp.com",
  databaseURL: "https://flashcards-test-7fbf8-default-rtdb.firebaseio.com",
  projectId: "flashcards-test-7fbf8",
  storageBucket: "flashcards-test-7fbf8.appspot.com",
  messagingSenderId: "506242405702",
  appId: "1:506242405702:web:2e9349c19e3ed314704147",
  measurementId: "G-5LBEP5LQTH"
};

const app = initializeApp(firebaseConfig);

const container = document.getElementById('root');
const root = createRoot(container!);
root.render(<React.StrictMode>
  <BrowserRouter>
    <App />
  </BrowserRouter>
</React.StrictMode>);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals()