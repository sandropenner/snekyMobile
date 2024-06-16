from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout  # For better positioning
from kivy.properties import ListProperty, NumericProperty, BooleanProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.metrics import dp  # Density-independent pixels for scaling
from kivy.uix.label import Label
import random

class SnakeGame(RelativeLayout):
    snake = ListProperty([(Window.width // 2, Window.height // 2)])
    food = ListProperty([0, 0])
    score = NumericProperty(0)
    game_over = BooleanProperty(False)
    game_started = BooleanProperty(False)

    GRID_SIZE = dp(20)  # Use dp for consistent sizing
    FPS = 10

    # ... (touch handling, start_game, generate_food_position, update remain the same)

    def draw_elements(self):
        self.canvas.clear()  # Clear canvas before redrawing
        with self.canvas:
            for segment in self.snake:
                Color(0, 1, 0)  # Green
                Rectangle(pos=segment, size=(self.GRID_SIZE, self.GRID_SIZE))

            Color(1, 0, 0)  # Red
            Rectangle(pos=self.food, size=(self.GRID_SIZE, self.GRID_SIZE))

        # Dynamically position labels using RelativeLayout's positioning features
        score_label = Label(text=f"Score: {self.score}", size_hint=(None, None), 
                            size=(dp(150), dp(50)), pos_hint={'x': 0.05, 'y': 0.9})  # Example positioning
        self.add_widget(score_label)

        if self.game_over:
            game_over_label = Label(text="Game Over!", font_size=dp(40), 
                                   pos_hint={'center_x': 0.5, 'center_y': 0.6})
            restart_label = Label(text="Tap to restart", font_size=dp(30),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.4})
            self.add_widget(game_over_label)
            self.add_widget(restart_label)

class SnakeApp(App):
    def build(self):
        game = SnakeGame()
        game.draw_elements()  # Initial draw
        return game

if __name__ == '__main__':
    SnakeApp().run()
