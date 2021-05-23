from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.gridlayout import MDGridLayout

from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior 
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen,ScreenManager

from kivy.properties import NumericProperty
from kivy.lang import Builder

from random import randint
from random import seed


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
    MDRectangleFlatButton:
        text : 'Exit'
        pos_hint : {'center_x':0.5,'center_y':0.1}
        on_press : root.manager.current = 'start'
    GridLayout:
        cols : 15
        spacing : 2

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

class DhayamDice(ButtonBehavior, Image):
    def on_press(self):
        dice_number = randint(1,6);
        if dice_number == 1:
            self.source = "dice-1.jpg"
        elif dice_number == 2:
            self.source = "dice-2.jpg"
        elif dice_number == 3:
            self.source = "dice-3.jpg"
        elif dice_number == 4:
            self.source = "dice-4.jpg"
        elif dice_number == 5:
            self.source = "dice-5.jpg"
        elif dice_number == 6:
            self.source = "dice-6.jpg"
        app.roll_dice(dice_number)

class DhayamScreen(Screen):
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
        #self.player1 = DhayamPlayer(source='')
        self.dice1 = DhayamDice(source='dice-1.jpg')
        self.root.add_widget(self.dice1)
        self.add_widget(self.root)

class AboutScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(StartScreen(name='start'))
sm.add_widget(DhayamScreen(name='dhayam'))
sm.add_widget(AboutScreen(name='about'))

class DhayamPlayer(ButtonBehavior, Image):
    score = NumericProperty(0)
    pawn_grid1 = NumericProperty(0)
    player_number = NumericProperty(0)
    def roll_dice():
        pass
    def move():
        pass

class DhayamApp(MDApp):
    def build(self):
        Builder.load_file("BoardImage.kv")
        screen = Builder.load_string(screen_helper)
        return screen
    
    def roll_dice(self, dicer):
        print("button press")
        print(dicer)

if __name__ == '__main__':
    app = DhayamApp()
    app.run()
