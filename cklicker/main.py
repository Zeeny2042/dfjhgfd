from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.animation import Animation
from kivy.storage.jsonstore import JsonStore
import os
from pathlib import Path

class ClickerApp(App):
    counter = NumericProperty(0)
    record = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_dir = Path(self.user_data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.store = JsonStore(str(self.data_dir / 'clicker_data.json'))
        self.load_record()
    
    def load_record(self):
        try:
            if os.path.exists(self.store.filename):
                self.record = self.store.get('record')['value']
                print(f"Загружен рекорд: {self.record}")
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            self.record = 0
    
    def save_record(self):
        try:
            current_record = self.store.get('record')['value'] if 'record' in self.store else 0
            if self.counter > current_record:
                self.store.put('record', value=self.counter)
                print(f"Сохранён новый рекорд: {self.counter}")
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
    
    def increment_counter(self):
        self.counter += 1
        if self.counter > self.record:
            self.record = self.counter
    
    def on_stop(self):
        self.save_record()

if __name__ == '__main__':
    ClickerApp().run()