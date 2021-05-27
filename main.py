from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import Screen 
#from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior 

from kivy.uix.widget import Widget
from kivy.animation import Animation 
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.properties import NumericProperty
from random import randint
from random import seed

#Window.clearcolor = (1,1,1,1)
#Window.size = (360,600)

seed(1)

screen_helper = """
ScreenManager:
    StartScreen:
    DhayamScreen:
    AboutScreen:

<StartScreen>:
    name : 'start'
    MDLabel:
        text : 'Dhayam'
        halign : 'center'
    MDRectangleFlatButton:
        text : 'Play'
        pos_hint : {'center_x':0.5,'center_y':0.4}
        on_press : root.manager.current = 'dhayam'
    MDRectangleFlatButton:
        text : 'About'
        pos_hint : {'center_x':0.5,'center_y':0.3}
        on_press : root.manager.current = 'about'
    MDRectangleFlatButton:
        text : 'Exit'
        pos_hint : {'center_x':0.5,'center_y':0.2}
        on_press : root.manager.current = 'about'

<DhayamScreen>:
    name : 'dhayam'
    GridLayout:
        size: root.height,root.width
        cols : 15
        spacing : 2
        Button:
            id: dice1_button
            size_hint : None, None
            size: 70,70
            pos_hint: {'center_x': 0.5}
            on_press: root.roll_dice1()
            Image:
                id: dice1_image
                source: "dice-5.jpg"
                center_x: self.parent.center_x
                center_y: self.parent.center_y

        Button:
            id: dice2_button
            size_hint : None, None
            size: 70,70
            pos_hint: {'center_x': 0.5}
            on_press: root.roll_dice2()
            Image:
                id: dice2_image
                source: "dice-6.jpg"
                center_x: self.parent.center_x
                center_y: self.parent.center_y

        Button:
            id: player1_button
            size_hint : None, None
            size: 50,50
            pos_hint : None, None
            pos: 370,370 
            on_press: root.move_player1(self)
            Image:
                id: player1_image
                source: "dice-1.jpg"
                center_x: self.parent.center_x
                center_y: self.parent.center_y

        Button:
            id: player2_button
            size_hint : None, None
            size: 50,50
            pos_hint : None, None
            pos: 635,370 
            on_press: root.move_player2(self)
            Image:
                id: player2_image
                source: "dice-2.jpg"
                center_x: self.parent.center_x
                center_y: self.parent.center_y

<AboutScreen>:
    name : 'about'
    MDLabel:
        text : 'Tamil Inc.'
        halign : 'center'
    MDRectangleFlatButton:
        text : 'Exit'
        pos_hint : {'center_x':0.5,'center_y':0.1}
        on_press : root.manager.current = 'start'

"""

class Container(FloatLayout):
    pass

class ColorLabel(Label):
    pass

class BlankLabel(Label):
    pass

class StartScreen(Screen):
    pass

class DhayamScreen(Screen):
    dicer1 = NumericProperty(0)
    dicer2 = NumericProperty(0)
    player1_x = NumericProperty(0)
    player1_y = NumericProperty(0)
    player2_x = NumericProperty(0)
    player2_y = NumericProperty(0)
    def __init__(self,**kwargs):
        super(DhayamScreen, self).__init__(**kwargs)
        the_grid = GridLayout(cols=15, spacing=2)
        for i in range(15):
                for j in range(15):
                    if 5 < j%15 < 9 or 5 < i%15 < 9:
                        newLabel = ColorLabel()
                    else:
                        newLabel = BlankLabel()
                    the_grid.add_widget(newLabel)
        self.root = Container()
        self.root.add_widget(the_grid)
        self.add_widget(self.root)

    def roll_dice1(self):
        print("button press: dicer1")
        #print(instance.id)
        dice_number = randint(1,6);
        self.dicer1 = dice_number
        if dice_number == 1:
            self.ids.dice1_image.source = "dice-1.jpg"
        elif dice_number == 2:
            self.ids.dice1_image.source = "dice-2.jpg"
        elif dice_number == 3:
            self.ids.dice1_image.source = "dice-3.jpg"
        elif dice_number == 4:
            self.ids.dice1_image.source = "dice-4.jpg"
        elif dice_number == 5:
            self.ids.dice1_image.source = "dice-5.jpg"
        elif dice_number == 6:
            self.ids.dice1_image.source = "dice-6.jpg"

    def roll_dice2(self):
        print("button press: dicer2")
        #print(instance.id)
        dice_number = randint(1,6);
        self.dicer2 = dice_number
        if dice_number == 1:
            self.ids.dice2_image.source = "dice-1.jpg"
        elif dice_number == 2:
            self.ids.dice2_image.source = "dice-2.jpg"
        elif dice_number == 3:
            self.ids.dice2_image.source = "dice-3.jpg"
        elif dice_number == 4:
            self.ids.dice2_image.source = "dice-4.jpg"
        elif dice_number == 5:
            self.ids.dice2_image.source = "dice-5.jpg"
        elif dice_number == 6:
            self.ids.dice2_image.source = "dice-6.jpg"

    def move_player1(self, widget):
        print("move player")
        print(self.dicer1)
        #p_x = randint(0,800)
        #p_y = randint(0,800)
        p_x = 53*self.dicer1
        p_y = 370
        animate = Animation(x=p_x, y=p_y, d=2, t='out_bounce')
        print(p_x,p_y)
        animate.start(widget)

    def move_player2(self, widget):
        print("move player")
        print(self.dicer2)
        p_x = randint(0,800)
        p_y = randint(0,800)
        animate = Animation(x=p_x, y=p_y, d=2, t='out_bounce')
        print(p_x, p_y)
        animate.start(widget)

class AboutScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(StartScreen(name='start'))
sm.add_widget(DhayamScreen(name='dhayam'))
sm.add_widget(AboutScreen(name='about'))


class DhayamApp(MDApp):
    def build(self):
        Builder.load_file("BoardImage.kv")
        screen = Builder.load_string(screen_helper)
#        Clock.schedule_interval(Game._turn, 0.1)
        return screen

if __name__ == '__main__':
    app = DhayamApp()
    app.run()
