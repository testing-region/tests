from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem



list_helper = """
Screen:
	ScrollView:
		MDList:
			id: scr1	

"""

class DemoApp(MDApp):
	
	def build(self):
		screen = Builder.load_string(list_helper)
		return screen
	
	def on_start(self):
		for i in range(20):
			items = OneLineListItem(text="item " + str(i))
			self.root.ids.scr1.add_widget(items)


DemoApp().run()