from manim import *

class CreateCircle(Scene):
	def construct(self):
		circle = Circle()
		circle.set_fill(opacity=0.5)
		self.play(Create(circle))