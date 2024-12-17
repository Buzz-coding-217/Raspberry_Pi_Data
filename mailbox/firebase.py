import pyrebase

# Firebase configuration
firebase_config = {
  "apiKey": "AIzaSyCOFOCT6fF9PhB6TXB_fiZWjeOJNHUmyb4",
  "authDomain": "mailbox-2b829.firebaseapp.com",
  "databaseURL": "https://mailbox-2b829-default-rtdb.firebaseio.com",
  "projectId": "mailbox-2b829",
  "storageBucket": "mailbox-2b829.appspot.com",
  "messagingSenderId": "1012165531027",
  "appId": "1:1012165531027:web:59152dd7001516cd7f4466",
  "measurementId": "G-G0ZKDPKN37"
};

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)

# Get a reference to the Firebase Realtime Database
db = firebase.database()

# Increment the "mails" variable
def increment_mails():
    try:
        mails_ref = db.child("mails").child("count")
        current_value = mails_ref.get().val()  # Get the current value of "mails/count"

        if current_value is None:
            current_value = 0

        new_value = current_value + 1
        db.child("mails").set(new_value)  # Set the new incremented value

        print(f"Successfully incremented 'mails/count' variable. New value: {new_value}")
    except Exception as e:
        print(f"Failed to increment 'mails/count' variable: {e}")

if __name__ == "__main__":
    increment_mails()
