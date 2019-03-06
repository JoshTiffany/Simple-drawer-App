import os

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class PainterWidget(FloatLayout):
    """Color List"""
    paint_color = ListProperty([0, 0, 1, 1])
    """Line Width list"""
    line_width = NumericProperty(1.0)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(rgba=self.paint_color)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        touch.ud['line'].points += touch.x, touch.y

    """Clear canvas"""

    def clear(self, obj):
        self.canvas.clear()

    """List of colors"""

    def blue(self, instance):
        self.paint_color = [0, 0, 1, 1]

    def red(self, instance):
        self.paint_color = [1, 0, 0, 1]

    def green(self, instance):
        self.paint_color = [0, 1, 0, 1]

    def yellow(self, instance):
        self.paint_color = [2, 2, 0, 1]

    def purple(self, instance):
        self.paint_color = [1, 0, 1, 1]

    def black(self, instance):
        self.paint_color = [0, 0, 0, 1]

    """Line width sizes"""

    def line_size1(self, instance):
        self.line_width = (1.0)

    def line_size2(self, instance):
        self.line_width = (2.0)

    def line_size3(self, instance):
        self.line_width = (3.0)

    def line_size4(self, instance):
        self.line_width = (4.0)

    """Save popup"""

    def popupsave(self, instance):
        box = BoxLayout(orientation='vertical', spacing=100)

        self.userinput = TextInput(text='', size_hint=(None, None), size=(200, 50), pos_hint={"x": .25},
                                   multiline=False)
        box.add_widget(self.userinput)
        box.add_widget(Button(text="Save", size_hint=(None, None), size=(200, 50), pos_hint={"x": .25},
                              on_press=self.popupc))

        self.popup = Popup(title='Save as', content=box, size_hint=(None, None), size=(400, 400))

        self.popup.open()

    def popupc(self, instance):
        box = BoxLayout(orientation="vertical", spacing=25)
        box.add_widget(Label(text=("Already a file, please rename"), size_hint=(None, None), size=(.1, .1),
                             pos_hint={"x": .50}, font_size='12sp'))

        box.add_widget(Button(text="Close", size_hint=(None, None), size=(100, 50), pos_hint={"x": .20}
                              , on_press=self.errorc))
        exists = os.path.isfile(self.userinput.text + ".png")
        if exists:
            self.export_to_png(self.userinput.text + ".png")
            """Error popup"""
            self.error = Popup(title="Error", content=box, size_hint=(None, None), size=(200, 200))

            self.error.open()
        else:
            self.export_to_png(self.userinput.text + ".png")
            self.popup.dismiss()

    def errorc(self, instance):
        self.error.dismiss()


class PaintApp(App):

    def build(self):
        """Parent widget"""
        parent = FloatLayout(size=Window.size)
        self.painter = PainterWidget()
        parent.add_widget(self.painter)
        """Clear Button"""
        parent.add_widget(
            Button(text='Clear', size_hint=(.07, .07), pos_hint={'x': .0, 'y': .93}, on_press=self.painter.clear))

        drpName = []
        drpName2 = []
        """Color drop down"""
        for i in range(10):
            drpName.append(DropDown())
            btnName = Button(text="Colors", size_hint=(.07, .07), pos_hint={'x': .07, 'y': .93}, )

            btn1 = Button(text="Blue", size_hint_y=None, height=btnName.height, on_release=self.painter.blue)
            btn2 = Button(text="Red", size_hint_y=None, height=btnName.height, on_release=self.painter.red)
            btn3 = Button(text="Green", size_hint_y=None, height=btnName.height, on_release=self.painter.green)
            btn4 = Button(text="Yellow", size_hint_y=None, height=btnName.height, on_release=self.painter.yellow)
            btn5 = Button(text="Purple", size_hint_y=None, height=btnName.height, on_release=self.painter.purple)
            btn6 = Button(text="Black", size_hint_y=None, height=btnName.height, on_release=self.painter.black)
            drpName[i].add_widget(btn1)
            drpName[i].add_widget(btn2)
            drpName[i].add_widget(btn3)
            drpName[i].add_widget(btn4)
            drpName[i].add_widget(btn5)
            drpName[i].add_widget(btn6)
            btnName.bind(on_release=drpName[i].open)
            parent.add_widget(btnName)
        """Size drop down"""
        for i in range(10):
            drpName2.append(DropDown())
            btnName2 = Button(text="Size", size_hint=(.07, .07), pos_hint={'x': .14, 'y': .93}, )

            size1 = Button(text="1", size_hint_y=None, height=btnName2.height, on_release=self.painter.line_size1)
            size2 = Button(text="2", size_hint_y=None, height=btnName2.height, on_release=self.painter.line_size2)
            size3 = Button(text="3", size_hint_y=None, height=btnName2.height, on_release=self.painter.line_size3)
            size4 = Button(text="4", size_hint_y=None, height=btnName2.height, on_release=self.painter.line_size4)
            drpName2[i].add_widget(size1)
            drpName2[i].add_widget(size2)
            drpName2[i].add_widget(size3)
            drpName2[i].add_widget(size4)
            btnName2.bind(on_release=drpName2[i].open)
            parent.add_widget(btnName2)
        """Save widget"""
        parent.add_widget(
            Button(text='Save', size_hint=(.07, .07), pos_hint={'x': .93, 'y': .93}, on_press=self.painter.popupsave))

        return parent


if __name__ == "__main__":
    PaintApp().run()
