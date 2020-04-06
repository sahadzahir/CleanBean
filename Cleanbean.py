import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from pythymiodw import *
from libdw import pyrebase
from kivy.properties import ObjectProperty
import time
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

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
<Label>:
    markup: True
    color: 0, 0, 0, 1
                    
<BinButt@Button>:
    font_size: 32
    color: 0, 0, 0, 1
    background_normal: 'dustbin.png'
    size: 50, 50
    size_hint: .3, .5                

<BinBar@Button>:
    
    color: 0, 0, 0, 1
    size: 50, 50
    size_hint: .115, .31



<MainMenu>:
    BoxLayout:
        orientation: "vertical"
        spacing: 50
        padding: 50
        Button:
            text: "Floor 3"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_one'
                
        Button:
            text: "Floor 4"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_two'
                
        Button:
            text: "Floor 5"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_three'
<FloorScreenOne>:
    bin1: bin1
    bin2: bin2
    BoxLayout:
                        
        id: bins
        orientation: "vertical"
        spacing: 10
        padding: 10
        
        FloatLayout:
            BinBar
                background_normal: 'grad5.png'
                pos_hint: {'right': 0.358, 'top': 0.68}
            BinBar:
                id: bin1
                background_normal: ''
                
                pos_hint: {'right': 0.358, 'top': 0.68}
            BinButt:
                pos_hint: {'right': 0.45, 'top': 0.8}
                
            BinBar
                background_normal: 'grad5.png'
                pos_hint: {'right': 0.758, 'top': 0.68}
            BinBar:
                id: bin2
                background_normal: ''
                
                pos_hint: {'right': 0.758, 'top': 0.68}
            BinButt:
                pos_hint: {'right': 0.85, 'top': 0.8}
            Label:
                font_size: 32
                text: "Building 1, Floor 3"
                pos_hint: {'right': 1, 'top': 1.45}
            Label:
                font_size: 16
                text: "1.313"
                pos_hint: {'right': 0.8, 'top': 0.8}
                
            Label:
                font_size: 16
                text: "1.314"
                pos_hint: {'right': 1.2, 'top': 0.8}

                 

        Button:
            text: "start updating"
            size_hint: 1, 0.2
            on_press: root.startclock()

        Button:
            text: "Back"
            size_hint: 1, 0.2                        
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'menu'

<FloorScreenTwo>:
    bin1: bin1
    bin2: bin2
    BoxLayout:
                        
        id: bins
        orientation: "vertical"
        spacing: 10
        padding: 10
        
        FloatLayout:
            BinBar
                background_normal: 'grad5.png'
                pos_hint: {'right': 0.358, 'top': 0.68}
            BinBar:
                id: bin1
                background_normal: ''
                
                pos_hint: {'right': 0.358, 'top': 0.68}
            BinButt:
                pos_hint: {'right': 0.45, 'top': 0.8}
                
            BinBar
                background_normal: 'grad5.png'
                pos_hint: {'right': 0.758, 'top': 0.68}
            BinBar:
                id: bin2
                background_normal: ''
                
                pos_hint: {'right': 0.758, 'top': 0.68}
            BinButt:
                pos_hint: {'right': 0.85, 'top': 0.8}
            Label:
                font_size: 32
                text: "Building 1, Floor 4"
                pos_hint: {'right': 1, 'top': 1.45}
            Label:
                font_size: 16
                text: "1.413"
                pos_hint: {'right': 0.8, 'top': 0.8}
                
            Label:
                font_size: 16
                text: "1.414"
                pos_hint: {'right': 1.2, 'top': 0.8}
                 

        Button:
            text: "start updating"
            size_hint: 1, 0.2
            on_press: root.startclock()

        Button:
            text: "Back"
            size_hint: 1, 0.2                        
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'menu'
                
<FloorScreenThree>:
    bin1: bin1
    bin2: bin2
    BoxLayout:
                        
        id: bins
        orientation: "vertical"
        spacing: 10
        padding: 10
        
        FloatLayout:
                    
            BinBar
                background_normal: 'grad5.png'
                pos_hint: {'right': 0.358, 'top': 0.68}
            BinBar:
                id: bin1
                background_normal: ''
                
                pos_hint: {'right': 0.358, 'top': 0.68}
            BinButt:
                pos_hint: {'right': 0.45, 'top': 0.8}
                
            BinBar
                background_normal: 'grad4.png'
                pos_hint: {'right': 0.758, 'top': 0.68}
            BinBar:
                id: bin2
                background_normal: ''
                
                pos_hint: {'right': 0.758, 'top': 0.68}
            BinButt:
                pos_hint: {'right': 0.85, 'top': 0.8}
            Label:
                font_size: 32
                text: "Building 1, Floor 5"
                pos_hint: {'right': 1, 'top': 1.45}
            Label:
                font_size: 16
                text: "1.513"
                pos_hint: {'right': 0.8, 'top': 0.8}
                
            Label:
                font_size: 16
                text: "1.514"
                pos_hint: {'right': 1.2, 'top': 0.8}

        Button:
            text: "start updating"
            size_hint: 1, 0.2
            on_press: root.startclock()

        Button:
            text: "Back"
            size_hint: 1, 0.2                        
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'menu'
""")
 
# Create a class for all screens in which you can include
# helpful methods specific to that screen
class FloorScreenOne(Screen):
    bin1 = ObjectProperty(None)
    bin2 = ObjectProperty(None)
    def message(self):
        print("Size changed")
    def bingetter(self, nom):
        return(firebase.database().child("Bin_%s"% str(nom)).get(user['idToken']).val())
    def update(self, dt):
        binlist = [self.bin1, self.bin2]
        for binno, bins in enumerate(binlist):
            bins.size_hint[1] = self.bingetter(binno+1)*0.3
            
    def startclock(self):
        Clock.schedule_interval(self.update, 0.1)
    pass
 
class FloorScreenTwo(Screen):
    bin1 = ObjectProperty(None)
    bin2 = ObjectProperty(None)
    def message(self):
        print("Size changed")
    def bingetter(self, nom):
        return(firebase.database().child("Bin_%s"% str(nom)).get(user['idToken']).val())
    def update(self, dt):
        binlist = [self.bin1, self.bin2]
        for binno, bins in enumerate(binlist):
            bins.size_hint[1] = self.bingetter(binno+1)*0.3
            
    def startclock(self):
        Clock.schedule_interval(self.update, 3)
    pass 

class FloorScreenThree(Screen):
    bin1 = ObjectProperty(None)
    bin2 = ObjectProperty(None)
    def message(self):
        print("Size changed")
    def bingetter(self, nom):
        return(firebase.database().child("Bin_%s"% str(nom)).get(user['idToken']).val())
    def update(self, dt):
        binlist = [self.bin1, self.bin2]
        for binno, bins in enumerate(binlist):
            bins.size_hint[1] = self.bingetter(binno+1)*0.3
            
    def startclock(self):
        Clock.schedule_interval(self.update, 3)
    pass 
class MainMenu(Screen):
    pass
 
 
# The ScreenManager controls moving between screens
screen_manager = ScreenManager()
 
# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(MainMenu(name="menu"))
screen_manager.add_widget(FloorScreenOne(name="screen_one"))
screen_manager.add_widget(FloorScreenTwo(name="screen_two"))
screen_manager.add_widget(FloorScreenThree(name="screen_three"))
 
class CleanBeanApp(App):
 
    def build(self):
        return screen_manager
 
sample_app = CleanBeanApp()
sample_app.run()
