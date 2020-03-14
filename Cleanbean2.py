import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from pythymiodw import *
from libdw import pyrebase
from kivy.properties import ObjectProperty
import time


projectid = "cleanbean-9e2f5"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = "AIzaSyA6H-rDpfGJZcTqFhf69t3VYbbOzfUW0EM"
email = "kenzho_lim@mymail.sutd.edu.sg"
password = "123456"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}


# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()
fbinfo = db.child("Reading").get(user['idToken'])
incoming = fbinfo.val()



    # Inherit Kivy's App class which represents the window
    # for our widgets
    # HelloKivy inherits all the fields and methods
    # from Kivy
class BinGL(GridLayout):
    bin1 = ObjectProperty(None)
    def message(self):
        print("Size changed")
    def example(self):
        return(firebase.database().child("Reading").get(user['idToken']).val())
    def update(self):
        while firebase.database().child("Reading").get(user['idToken']).val():
            self.bin1.size_hint[1] = firebase.database().child("Reading").get(user['idToken']).val()
            time.sleep(4)
            print("height changed to ", self.bin1.size_hint[1])

                
        
    
        # This returns the content we want in the window
class CleanBeanApp(App):    

    def build(self):
        
        return BinGL()


instance = BinGL()

mainApp = CleanBeanApp()
mainApp.run()