from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from sales import SalesBoard
from rentals import RentalsBoard
from kivymd.uix.textfield import MDTextField

helper="""
ScreenManager:
    id:manager
    name:'manager'
    MenuScreen:
    SalesScreen:
    RentalsScreen:
<MenuScreen>:
    name:"menu"
    MDRectangleFlatButton:
        text:'Go to Sales'
        pos_hint:{'center_x':0.5,'center_y':0.3}
        on_release:root.manager.current='sales2'
    MDRectangleFlatButton:
        text:'Go to Rentals'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_release:root.manager.current='rentals'
<SalesScreen>:
    name:"sales2"
    id:sales2

    MDBoxLayout:
        orientation:'vertical'
        MDBoxLayout:
            id:top_nav
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:.05,.45,45,1
                Rectangle:
                    size:self.size
                    pos:self.pos
            Button:
                text:"Main Menu"
                halign:"center"
                size_hint:.2,1
                background_normal:''
                background_color:.06,.2,.32,1
                on_release:root.manager.current='menu'
            Button:
                text:"Reset"
                halign:"center"
                size_hint:.2,1
                background_normal:''
                background_color:.9,.2,.2,1
                on_release:the_sale.reset()


            Button:
                text:"Sales Dashboard"
                halign:"center"
                background_color:.01,.5,.01,1
            Button:
                text:"Rental Screen"
                halign:"center"
                size_hint:.2,1
                width:100
                background_normal:''
                background_color:.06,.5,.32,1
                on_release:root.manager.current='rentals'
        SalesBoard:
            id:the_sale
            size_hint:1,.7
            padding:20
        MDTextField:
            id:searcher
            hint_text:'Search by Location'
            on_text_validate:the_sale.self_show()
<RentalsScreen>:
    name:"rentals"
    MDBoxLayout:
        orientation:'vertical'
        MDBoxLayout:
            id:top_nav
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:.05,.45,45,1
                Rectangle:
                    size:self.size
                    pos:self.pos
            Button:
                text:"Main Menu"
                halign:"center"
                size_hint:.2,1
                background_normal:''
                background_color:.06,.2,.32,1
                on_release:root.manager.current='menu'
            Button:
                text:"Reset"
                halign:"center"
                size_hint:.2,1
                background_normal:''
                background_color:.1,.2,.9,1
                on_release:the_rent.reset()

            Button:
                text:"Rentals Dashboard"
                halign:"center"
                background_color:.01,.5,.01,1
            Button:
                text:"Sales Screen"
                halign:"center"
                size_hint:.2,1
                width:100
                background_normal:''
                background_color:.6,.01,.32,1
                on_release:root.manager.current='sales2'
        RentalsBoard:
            id:the_rent
            size_hint:1,.9
            padding:20
        MDTextField:
            id:searcher2
            hint_text:'Search by Location'
            on_text_validate:the_rent.self_show()

"""

class MenuScreen(Screen):
    pass
class SalesScreen(Screen):
    pass

class RentalsScreen(Screen):
    pass
##sm=ScreenManager()
##sm.add_widget(MenuScreen(name='menu'))
##sm.add_widget(ProfileScreen(name='profile'))



class DemoApp(MDApp):
    def build(self):
        screen=Builder.load_string(helper)
        return screen
    






DemoApp().run()
