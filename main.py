from core.baseapp import BaseApp
from view.view_book import *

class MainApp(BaseApp):
    def _init_(self):
        self.books = []

    def list_book(self):
        self.list_book = ()


if _name_ == "_main_":
    app = MainApp()
    app.run()
