from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
import os

# Define the KV layout as a multi-line string
kv = """
<MainWindow>:
    name: "Main"
    GridLayout:
        cols: 1
        
        Button:
            text: "Linkedin"
            
            background_color : 0,0,1,1
            on_release:
                app.root.current = "Linkedin" 
                root.manager.transition.direction = "left"


        Button:
            text: "Youtube"
            background_color : 1,0,0,1
            on_release:
                app.root.current = "Youtube" 
                root.manager.transition.direction = "right"



<LinkedinWin>:
    name: "Linkedin"
    GridLayout:
        cols:1
        
        GridLayout:
            cols: 2
            Label:
                text: "Link: "
                size_hint:  None,None
                size: root.width/3, root.height / 7
                
            TextInput:
                id: link
                multiline: False
                size_hint:  None,None
                size: 2*root.width/3, root.height / 7
                
            Label:
                text: "Name: "
                size_hint:  None,None
                size: root.width/3, root.height / 7
            TextInput:
                id: vid_name
                multiline: False
                size_hint:  None,None
                size: 2*root.width/3, root.height / 7
                        
            
        Button:
            text: "Clear"
            size_hint: None, None
            size: root.width, root.height / 8
            on_press: root.clear_content()
            
            
        Image:
            source: 'LinkedIn-Logo.wine.png'
            size_hint_y :  None
            height:  root.height/5
            
        Button:
            text: "Download"
            size_hint: None, None
            size: root.width, root.height / 5
            
                
        Button:
            text: "Go Back"
            size_hint: None, None
            size: root.width, root.height / 5
            on_release:
                app.root.current = "Main"
                root.manager.transition.direction = "right"
            
            

                        
<YoutubeWin>:
    name: "Youtube"
    GridLayout:
        cols:1
        
        GridLayout:
            cols: 2
            Label:
                text: "Link: "
                size_hint:  None,None
                size: root.width/3, root.height / 7
                
            TextInput:
                id: link
                multiline: False
                size_hint:  None,None
                size: 2*root.width/3, root.height / 7
                
            Label:
                text: "Name: "
                size_hint:  None,None
                size: root.width/3, root.height / 7
            TextInput:
                id: vid_name
                multiline: False
                size_hint:  None,None
                size: 2*root.width/3, root.height / 7
                        
                      
            
        Button:
            text: "Clear"
            size_hint: None, None
            size: root.width, root.height / 8
            on_press: root.clear_content()
            
        
        Image:
            source: '1024px-YouTube_Logo_2017.svg.png'
            size_hint_y :  None
            height:  root.height/5
            
        Button:
            text: "Download"
            size_hint: None, None
            size: root.width, root.height / 5
            on_press: root.download()
                
            
        Button:
            text: "Go Back"
            size_hint: None, None
            size: root.width, root.height / 5
            on_release:
                app.root.current = "Main"
                root.manager.transition.direction = "left"
     
    
"""

# Load the KV string
Builder.load_string(kv)

class MainWindow(Screen):
    pass

class LinkedinWin(Screen):
    def clear_content(self):
        self.ids.link.text = ""
        self.ids.vid_name.text = ""

class YoutubeWin(Screen):
    
    def download(self):
        check_pop()
        
    def clear_content(self):
        self.ids.link.text = ""
        self.ids.vid_name.text = ""

class WindowManager(ScreenManager):
    pass

class MyMainApp(App):
    def build(self):
        # Create the window manager and add the screens
        wm = WindowManager()
        wm.add_widget(MainWindow(name="Main"))
        wm.add_widget(LinkedinWin(name="Linkedin"))
        wm.add_widget(YoutubeWin(name="Youtube"))
        return wm
        
def check_pop():
    pop = Popup(title='Confirm',
                  content=Label(text='The video size is: ')
                ,size_hint=(1,0.5)
                )
    

    pop.open()


if __name__ == "__main__":
    MyMainApp().run()

