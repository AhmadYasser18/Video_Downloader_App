#App
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

#Youtube
from pytubefix import YouTube
from pytubefix.cli import on_progress

import os

# Define the KV layout as a multi-line string
kv = """
<MainWindow>:
    name: "Main"
    GridLayout:
        cols: 1
        Label:
            text: "Download from: "
            font_size: 80
            size_hint:  None,None
            size: root.width, root.height / 3
            
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
        if self.ids.link.text.strip() != "" :
            yt_url = self.ids.link.text.strip()

            yt = YouTube(yt_url, on_progress_callback=on_progress) #, use_po_token=True)
            
            yt_video = yt.streams.get_audio_only()
            
            vid_size = yt_video.filesize_mb
            
            check_pop(vid_size, yt.title)
        
        else:
            self.invalid_popup()


        #yt_video.download()
        
        #print(yt.title)
        

    #Invalid Link Popup
    def invalid_popup(self):
        invalid_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        invalid_layout .add_widget(Label(text=f"Invalid link!\nPlease recheck and enter a valid link."))
        
        button_layout = BoxLayout(orientation='horizontal', spacing=10)
        btn_size = (1,0.6)   
        
        ok_button = Button(text="Ok", size_hint= btn_size, on_release=lambda x: invalid_pop.dismiss())
        
        button_layout.add_widget(ok_button)
        
        invalid_layout.add_widget(button_layout)
        
        #Create the popup
        invalid_pop = Popup(title='Invalid', content=invalid_layout ,size_hint=(1,0.5))
        
        invalid_pop.open()     

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
        
def check_pop(vid_size=0, title = None):
    
    layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
    
    layout.add_widget(Label(text=f"The video size is: {vid_size}.\n Would you like to download: {title}?"))
    
    button_layout = BoxLayout(orientation='horizontal', spacing=10)
    
    btn_size = (1,0.6)
    
    download_button = Button(text="Download", size_hint= btn_size, on_release=lambda x: pop.dismiss())
    cancel_button = Button(text="Cancel", size_hint= btn_size, on_release=lambda x: pop.dismiss())
    
    button_layout.add_widget(download_button)
    button_layout.add_widget(cancel_button)

    layout.add_widget(button_layout)

    # Create the popup
    
    pop = Popup(title='Confirm', 
                content=layout,size_hint=(1,0.5))

    pop.open()


if __name__ == "__main__":
    MyMainApp().run()
