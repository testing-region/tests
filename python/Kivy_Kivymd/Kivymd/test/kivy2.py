from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineAvatarListItem, MDList, ImageLeftWidget
from kivy.uix.scrollview import ScrollView


class DemoApp(MDApp):
	def build(self):
		screen = Screen()
		list_view = MDList()
		scroll = ScrollView()
		
		for i in range(20):
			image = ImageLeftWidget(source='/storage/emulated/0/Pictures/gallery/aurora-1197753_1920.jpg')
			items = OneLineAvatarListItem(text='item ' + str(i))
			items.add_widget(image)
			list_view.add_widget(items)
		
		scroll.add_widget(list_view)
		screen.add_widget(scroll)
		return screen
		

DemoApp().run()