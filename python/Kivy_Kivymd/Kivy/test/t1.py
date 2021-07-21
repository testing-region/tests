from kivy.app import App
from kivy.uix.label import Label

class t1(App):
	def build(self):
		return Label(text='Hello World!,\nHow are you doing?')
		


if __name__ == '__main__':
	t1().run()