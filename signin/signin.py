from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('signin/signin.kv')

class SigninWindow(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(*kwargs)

class SigninApp(App):
	def build(self):
		return SigninWindow()

if __name__=="__main__":
	SigninApp().run()
			