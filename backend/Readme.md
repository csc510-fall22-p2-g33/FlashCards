# Getting Started with Firebase

## Features:

1. Login and Sign up - Hosted on [Firebase](https://firebase.google.com/)
                                         
2. Based on Python-Flask

## Setting up Firebase:

1. Go to [Firebase](https://firebase.google.com/)
2. Login/Register your account
3. Click on add project
4. Give project name
5. Optional: select google analytics
6. Create project
7. Under "Get started by adding Firebase to your app", click on web app
8. Name the web app and copy the "apiKey", "authDomain", "databaseURL", "storageBucket" from the code given there
9. Go to login.py and app.py, and add the values you copied above
10. Go to console, click on Authentication (On the left sidebar), click on sign-in method, and enable email/password sign in as well as Google sign in
11. Go to console, click on Realtime Database, click on Rules, and set the rules to the following, updating the read and write date to after the current day if need be.
```
{
  "rules": {
    ".read": "now < 1673179600000",  // 2023-01-08
    ".write": "now < 1673179600000",  // 2023-01-08
    "deck": {
      ".indexOn": ["userId", "visibility", "shared_uids"]
    },
    "card": {
      ".indexOn": ["deckId"]
    },
    "user": {
      ".indexOn": ["userId", "email"]
    },
    "CI-rtdb": {
      "deck": {
        ".indexOn": ["userId", "visibility", "shared_uids"]
      },
      "card": {
        ".indexOn": ["deckId"]
      },
      "user": {
      ".indexOn": ["userId", "email"]
    	}
    }
  }
}

```

## Setting Up Backend Server:

### With Flask Run
```
cd [repository]/backend
pip install -r requirements.txt
FLASK_APP=src.api:app FLASK_RUN_PORT=8000 FLASK_RUN_HOST=0.0.0.0 python3 -m flask run
```

### With Gunicorn
```
cd [repository]/backend
pip install -r requirements.txt
gunicorn --bind=0.0.0.0:8000 src.api:app
```
