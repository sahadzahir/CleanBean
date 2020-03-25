import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from pythymiodw import *
from libdw import pyrebase
from kivy.properties import ObjectProperty
import time
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen


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
fbinfo = db.child("Bin_1").get(user['idToken'])
incoming = fbinfo.val()

# You can create your kv code in the Python file
Builder.load_string("""
<ScreenOne>:
    bin1: bin1
    bin2: bin2
    GridLayout:
        
        
        id: bins
        rows: 2
        padding: 40
        spacing: 80
        
            
                 
                    
        BoxLayout:
            Button:
                id: bin1
                background_normal: 'red.png'
                text: " %f" % root.bingetter(1)
                size_hint: 0.5, 0.0
        BoxLayout:        
            Button:
                id: bin2
                background_normal: 'red.png'
                text: " %f" % root.bingetter(2)
                size_hint: 0.5, 0.0         
                
        BoxLayout:
            Button:
                text: "refresh"
                on_press: root.update()
            Button:
                text: "start updating"
                on_press: root.startclock()
        BoxLayout:
            Button:
                text: "Go to Screen 2"
                on_press:
                    # You can define the duration of the change
                    # and the direction of the slide
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'screen_two'
     
<ScreenTwo>:
    BoxLayout:
        Button:
            text: "Go to Screen 1"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_one'
""")
 
# Create a class for all screens in which you can include
# helpful methods specific to that screen
class ScreenOne(Screen):
    bin1 = ObjectProperty(None)
    bin2 = ObjectProperty(None)
    def message(self):
        print("Size changed")
    def bingetter(self, nom):
        return(firebase.database().child("Bin_%s"% str(nom)).get(user['idToken']).val())
    def update(self, dt):
        binlist = [self.bin1, self.bin2]
        for binno, bins in enumerate(binlist):
            bins.size_hint[1] = self.bingetter(binno+1)
            bins.text = " %s" % self.bingetter(binno+1)
    def startclock(self):
        Clock.schedule_interval(self.update, 1)
    pass
 
 
 
class ScreenTwo(Screen):
    pass
 
 
# The ScreenManager controls moving between screens
screen_manager = ScreenManager()
 
# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
 
class CleanBeanApp(App):
 
    def build(self):
        return screen_manager
 
sample_app = CleanBeanApp()
sample_app.run()
