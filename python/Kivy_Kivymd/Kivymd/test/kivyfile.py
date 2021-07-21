from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton


class TestApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "Amber"
		self.theme_cls.primary_hue = "A700"
		self.theme_cls.theme_style = "Dark"		
		screen = Screen()
		btn = MDRectangleFlatButton( text = "Hello World!", pos_hint = { "center_x" : 0.5, "center_y" : 0.5} )
		screen.add_widget(btn)		
		return screen


TestApp().run()