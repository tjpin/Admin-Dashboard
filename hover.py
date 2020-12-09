from kivy.base import runTouchApp
from kivy.factory import Factory
from kivymd.uix.list import OneLineAvatarListItem, IconLeftWidget
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivy.utils import get_color_from_hex


class HoverBehavior(object):
    hovered = BooleanProperty(False)
    border_point = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass


Factory.register('HoverBehavior', HoverBehavior)


class HoverFlatBtn(MDFlatButton, HoverBehavior):
    def on_enter(self, *args):
        self.md_bg_color = (1, 1, 1, 1)

    def on_leave(self, *args):
        self.md_bg_color = get_color_from_hex('#e62e00')


class HoverIconList(OneLineAvatarListItem, HoverBehavior):
    def on_enter(self, *args):
        self.bg_color = [1, 1, 1, 1]
        self.theme_text_color = "Custom"
        self.text_color = [0, 0, 1, 1]

    def on_leave(self, *args):
        self.bg_color = 0, 0, 1, 1
        self.theme_text_color = "Custom"
        self.text_color = 1, 1, 1, 1
