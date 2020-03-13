import kivy

kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


    # Inherit Kivy's App class which represents the window
    # for our widgets
    # HelloKivy inherits all the fields and methods
    # from Kivy
class BinGL(GridLayout):
    pass
        # This returns the content we want in the window
class CleanBeanApp(App):    
    def build(self):
            # Return a label widget with Hello Kivy
        return BinGL()


mainApp = CleanBeanApp()
mainApp.run()