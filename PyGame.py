# PyGame 1.1
# ============

from pyb import Pin, udelay, micros, elapsed_micros
from Lib_TFT_St7735 import St7735
from typsnitt import Char
char = Char()
st = St7735()
enter = Pin('X8', Pin.IN, Pin.PULL_UP)
down = Pin('X7', Pin.IN, Pin.PULL_UP)
left = Pin('X5', Pin.IN, Pin.PULL_UP)
right = Pin('Y11', Pin.IN, Pin.PULL_UP)
up = Pin('Y9', Pin.IN, Pin.PULL_UP)
back = Pin('X6', Pin.IN, Pin.PULL_UP)
menu = Pin('Y12', Pin.IN, Pin.PULL_UP)
f1 = Pin('X4', Pin.IN, Pin.PULL_UP)
f2 = Pin('Y10', Pin.IN, Pin.PULL_UP)
p = st.FastDrawPixel
r = st.fill_rect
c = st.fill_circle
rram = st.draw_rect
cram = st.draw_circle
line = st.draw_line
rgb = st.rgb24_16
clear = st.clear_screen
fill = st.fill_screen

st.init_display()
st.clear_screen()
st.fill_screen(rgb(255, 255, 255))


class Game:
	x = 0
	y = 0
	x2 = 0
	y2 = 0
	level = 1
	jump = 0
	mark = True
	dead = False
	bounce = False
	quit_game = False
	change_delay = False
	page = 1
	pages = 1
	ticks = 0
	d = 33000

	def background(self):
		if self.level is 1:
			fill(rgb(0, 192, 255))
			r(7, 0, 9, 70, rgb(0, 128, 0))
			r(0, 0, 6, 70, rgb(192, 64, 0))
			r(7, 100, 9, 159, rgb(0, 128, 0))
			r(0, 100, 6, 159, rgb(192, 64, 0))
		elif self.level is 2:
			fill(rgb(0, 192, 255))
			r(7, 0, 9, 30, rgb(0, 128, 0))
			r(0, 0, 6, 30, rgb(192, 64, 0))
			r(7, 120, 159, 30, rgb(0, 128, 0))
			r(0, 120, 6, 159, rgb(192, 64, 0))
			r(0, 31, 18, 119, rgb(192, 64, 0))
			r(19, 31, 21, 119, rgb(0, 128, 0))
			r(7, 120, 9, 159, rgb(0, 128, 0))
			r(19, 54, 21, 64, rgb(255, 255, 0))
			r(54, 0, 59, 159, rgb(192, 64, 0))
			r(60, 0, 62, 159, rgb(0, 128, 0))

	def player(self, a=x, b=y, colour=rgb(0, 0, 0)):
		self.x = a
		self.y = b
		r(self.x, self.y + 2, self.x + 5, self.y + 3, colour)
		r(self.x, self.y + 6, self.x + 5, self.y + 7, colour)
		r(self.x + 6, self.y + 4, self.x + 13, self.y + 5, colour)
		r(self.x + 8, self.y, self.x + 9, self.y + 1, colour)
		r(self.x + 10, self.y + 2, self.x + 11, self.y + 3, colour)
		r(self.x + 8, self.y + 8, self.x + 9, self.y + 9, colour)
		r(self.x + 10, self.y + 6, self.x + 11, self.y + 7, colour)
		r(self.x + 14, self.y + 2, self.x + 15, self.y + 3, colour)
		r(self.x + 14, self.y + 6, self.x + 15, self.y + 7, colour)
		r(self.x + 16, self.y + 4, self.x + 17, self.y + 5, colour)

	def game_menu(self):
		info_page = 1
		info_pages = 1
		sta = "The game is starting."
		if menu.value() is 0:
			print("\nGAME MENY")
			print("========================================")
			print("|| BACK: Back to game")
			print("|| UP: Info")
			print("|| MENU: Next page")
			print("|| LEFT: Go to level")
			print("|| ENTER: Restart level")
			print("|| RIGHT: Quit")
			print("|| F1: Teleport")
			print("|| DOWN: Animations and objects")
			print("|| F2: Speed")
			print("|| Page", self.page, "/", self.pages)
			print("========================================\n")
			udelay(1000000)
			while True:
				if back.value() is 0:
					print("The game is starting.")
					udelay(1000000)
					return
				if up.value() is 0:
					print("\nWelcome to PyGame!\n\nPress UP to make a small jump.")
					print("If you fall or hit a wall, you will DIE!")
					print("If you walk on a yellow thing, you will make a big jump.")
					print("Press ENTER to start!")
					print("\nYou are at x" + str(self.x), "y" + str(self.y), "\nLevel:", self.level)
					print("Page", info_page, "/", info_pages, "\n")
					while True:
						if back.value() is 0:
							print(sta)
							udelay(1000000)
							return
						if menu.value() is 0:
							break
						if enter.value() is 0:
							print(sta)
							udelay(1000000)
							return
				if left.value() is 0:
					try:
						go_to_level = int(input("Go to level: "))
						self.level = go_to_level
						if self.level is 2:
							self.background()
							print("\nLevel", self.level)
							r(119, 69, 121, 81, rgb(0, 0, 0))
							r(110, 79, 120, 81, rgb(0, 0, 0))
							r(109, 69, 111, 81, rgb(0, 0, 0))
							r(99, 69, 111, 71, rgb(0, 0, 0))
							r(99, 69, 101, 81, rgb(0, 0, 0))
							self.x = 10
							self.y = 0
							self.player(self.x, self.y)
							while True:
								if enter.value() is 0:
									print(sta)
									udelay(1000000)
									self.background()
									return
						elif self.level is 1:
							self.background()
							print("\nLevel", self.level)
							r(99, 79, 121, 81, rgb(0, 0, 0))
							self.x = 10
							self.y = 0
							self.player(self.x, self.y)
							while True:
								if enter.value() is 0:
									print(sta)
									udelay(1000000)
									self.background()
									return
						self.background()
					except ValueError:
						print("The game is starting.")
						udelay(1000000)
				if right.value() is 0:
					print("\nQuit game?")
					while True:
						if enter.value() is 0:
							self.quit_game = True
							for deather53dw in range(10):
								fill(rgb(0, 0, 0))
								udelay(100000)
								self.background()
							clear()
							return
						if back.value() is 0:
							print(sta)
							udelay(1000000)
							return
				if enter.value() is 0:
					self.background()
					self.x = 10
					self.y = 0
					self.background()
					print("\nLevel", self.level)
					self.player(a=self.x, b=self.y, colour=rgb(0, 192, 255))
					self.player(a=self.x, b=self.y)
					if self.level is 2:
						r(119, 69, 121, 81, rgb(0, 0, 0))
						r(110, 79, 120, 81, rgb(0, 0, 0))
						r(109, 69, 111, 81, rgb(0, 0, 0))
						r(99, 69, 111, 71, rgb(0, 0, 0))
						r(99, 69, 101, 81, rgb(0, 0, 0))
						while True:
							if enter.value() is 0:
								udelay(1000000)
								self.background()
								return
					elif self.level is 1:
						self.background()
						print("\nLevel", self.level)
						r(99, 79, 121, 81, rgb(0, 0, 0))
						self.player(a=10, b=0)
						while True:
							if enter.value() is 0:
								udelay(1000000)
								self.background()
								return
						self.background()
					self.background()
				if f1.value() is 0:
					try:
						tp_x = int(input("Xteleport to: "))
						tp_y = int(input("Yteleport to: "))
						while True:
							if enter.value() is 0:
								self.player(a=self.x, b=self.y, colour=rgb(0, 192, 255))
								self.x = tp_x
								self.y = tp_y
								udelay(1000000)
								return
							if back.value() is 0:
								print("The game is starting.")
								udelay(1000000)
								return
					except ValueError:
						return
				if down.value() is 0:
					print("ANIMATIONS AND OBJECTS: ")
					print("Player")
					print("Ground: dirt and grass")
					print("Sky")
					print("Bouncer")
					print("Level number")
					print("Death cross")
					print("Death player")
					print("Walking animation")
					print("Small jump animation")
					print("Big jump / bouncer animation")
					print("Fall animation")
					print("Death animation")
					print("Quit animation")
					while True:
						if back.value() is 0:
							clear()
							self.background()
							self.player(self.x, self.y, rgb(0, 0, 0))
							print("The game is starting.")
							udelay(1000000)
							return
						elif f1.value() is 0:
							print("\nDeath animation")
							for fake_death in range(10):
								fill(rgb(128, 0, 0))
								udelay(100000)
								self.background()
							clear()
							self.background()
							r(3, 75, 124, 85, rgb(0, 0, 0))
							r(80, 50, 90, 110, rgb(0, 0, 0))
							self.player(self.x, self.y, rgb(128, 0, 0))
						elif f2.value() is 0:
							print("\nQuit animation")
							for fake_quit in range(10):
								fill(rgb(0, 0, 0))
								udelay(100000)
								self.background()
							clear()
				if f2.value() is 0:
					try:
						delay = int(input("Delay: "))
						while True:
							if back.value() is 0:
								print("The game is starting.")
								udelay(1000000)
								return
							self.player(a=self.x, b=self.y, colour=rgb(0, 192, 255))
							self.d = delay * 1000
							print(sta)
							self.change_delay = True
							udelay(1000000)
							return
					except ValueError:
						print(sta)
						return

	def ram(self, ax, ay, bx, by, t, colour):
		self.x = ax
		self.y = ay
		self.x2 = bx
		self.y2 = by
		for q in range(t):
			rram(self.x, self.y, self.x2, self.y2, colour)
			self.x += 1
			self.y += 1
			self.x2 -= 1
			self.y2 -= 1

	def death(self):
		print("\nYou DIED!! :( :o ː( ;( !!")
		for deather53 in range(10):
			fill(rgb(128, 0, 0))
			udelay(100000)
			self.background()
			self.dead = True
		clear()
		self.background()
		r(3, 75, 124, 85, rgb(0, 0, 0))
		r(80, 50, 90, 110, rgb(0, 0, 0))
		print("You came to level", self.level, "\n")
		char.char_in("YOU DIED!!", 1, colour=rgb(255, 0, 0))
		char.char_in("YOU CAME TO LEVEL", xx=60, colour=rgb(255, 0, 0))
		char.char_in(str(self.level), xx=60, yy=109, colour=rgb(255, 0, 0))
		self.player(self.x, self.y, rgb(128, 0, 0))
		return

	def move(self, d=33000):
		if not self.change_delay:
			self.d = d
		big_jump = [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2]
		small_jump = [2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, -1, -1, -1, -1, -2, -2, -2, -2, -2]
		while True:
			if self.quit_game is True:
				return
			start = micros()
			self.player(a=self.x, b=self.y, colour=rgb(0, 192, 255))
			self.y += 1
			self.player(a=self.x, b=self.y)
			self.game_menu()
			elapsed_micros(start)
			udelay(int(self.d - elapsed_micros(start)))
			fps = 1 / (elapsed_micros(start) / 1000000)
			print(int(fps), "fps")
			if enter.value() is 0 or self.bounce is True and self.mark is True:
				self.jump = 2
				self.mark = True
				for ficedula in big_jump:
					start = micros()
					self.player(a=self.x, b=self.y, colour=rgb(0, 192, 255))
					self.x += ficedula
					self.y += 1
					self.ticks += 1
					if self.level is 2 and self.y > 30 - 7 and self.x < 22 and self.y < 120 and self.ticks > 17:
						self.x = 22
						break
					if self.level is 2 and self.x > 37 and self.dead is False:
						self.death()
						return
					if 30 - 7 < self.y < 119 - 2 and self.x < 22 and self.level is 2:
						self.death()
						return
					if 70 - 2 < self.y < 100 - 7 and self.jump is 0 and self.level is 1:
						self.mark = False
						break
					self.player(a=self.x, b=self.y)
					elapsed_micros(start)
					udelay(int(self.d - elapsed_micros(start)))
					fps = 1 / (elapsed_micros(start) / 1000000)
					print(int(fps), "fps")
				self.ticks = 0
				self.jump = 0
				self.bounce = False
			if up.value() is 0 and self.mark is True:
				self.jump = 1
				self.mark = True
				for ficedula2 in small_jump:
					start = micros()
					self.player(a=self.x, b=self.y, colour=rgb(0, 192, 255))
					self.x += ficedula2
					self.y += 1
					self.ticks += 1
					if self.level is 2 and self.y > 30 - 7 and self.x < 22 and self.y < 120 and self.ticks > 12:
						self.x = 22
					if 30 - 7 < self.y < 119 - 2 and self.x < 22 and self.level is 2:
						self.death()
						return
					if self.level is 2 and self.x > 37 and self.dead is False:
						self.death()
						return
					if 70 - 2 < self.y < 100 - 7 and self.jump is 0 and self.level is 1:
						self.mark = False
						break
					self.player(a=self.x, b=self.y)
					elapsed_micros(start)
					udelay(int(self.d - elapsed_micros(start)))
					fps = 1 / (elapsed_micros(start) / 1000000)
					print(int(fps), "fps")
				self.ticks = 0
				self.jump = 0
			if self.y > 170:
				if self.level is 2:
					print("\nYOU WON!!\n")
					st.fill_screen(rgb(255, 255, 255))
					char.char_in("YOU WON!!", xx=60, yy=60)
					return
				self.level += 1
				self.x = 10
				self.y = 0
				self.background()
				print("\nLevel", self.level)
				self.player(a=self.x, b=self.y, colour=rgb(0, 192, 255))
				self.player(a=self.x, b=self.y)
				if self.level is 2:
					char.char_in("LEVEL 2", xx=104, yy=30)
					while True:
						self.game_menu()
						if enter.value() is 0:
							udelay(1000000)
							break
				self.background()
			if 70 - 2 < self.y < 100 - 7 and self.jump is 0 and self.level is 1:
				self.mark = False
			if self.y > 120 - 2 and self.jump is 0 and self.level is 2:
				self.mark = False
			if 53 - 2 < self.y < 65 - 7 and self.level is 2:
				self.bounce = True
			if self.mark is False:
				for ficedula_bird_death in range(17):
					start = micros()
					if ficedula_bird_death is 0:
						self.y -= 1
					if self.x < 1:
						break
					if self.y > 100 - 7 and self.level is 1 and self.x < 10 and self.dead is False:
						self.death()
						return
					self.player(a=self.x, b=self.y, colour=rgb(0, 192, 255))
					ficedula_fall = int(ficedula_bird_death / 2)
					self.x -= ficedula_fall
					self.y += 1
					if 70 - 2 >= self.y >= 100 - 7 and self.level is 1 and self.x < 10:
						self.x = 10
						break
					if self.y > 120 - 2 and self.x <= 10 and self.level is 2:
						self.x = 10
						self.mark = True
						self.y -= 0
						break
					self.player(a=self.x, b=self.y)
					elapsed_micros(start)
					udelay(int(self.d - elapsed_micros(start)))
					fps = 1 / (elapsed_micros(start) / 1000000)
					print(int(fps), "fps")
				if self.x < 1 and self.dead is False:
					self.death()
					return
			if self.quit_game:
				return
			if 120 > self.y > 22 > self.x and self.dead is False and self.level is 2:
				self.death()
				self.quit_game = True
				return

print("\nWelcome to PyGame!\n\nPress UP to make a small jump.\nPress ENTER to make a big jump.")
print("If you fall or hit a wall, you will DIE! \nIf you walk on a yellow thing, you will make a big jump.")
print("Press MENU to go to the game menu.")
print("Press ENTER to start!\n")
char.char_in("WELCOME TO PYGAME!", 1)
char.char_in("PRESS UP TO MAKE A", 2)
char.char_in("SMALL JUMP.", 3)
char.char_in("PRESS ENTER TO MAKE A", 4)
char.char_in("BIG JUMP.", 5)
char.char_in("IF YOU FALL OR HIT A WALL,", 6)
char.char_in("YOU WILL DIE!", 7)
char.char_in("IF YOU WALK ON A YELLOW", 8)
char.char_in("THING, YOU WILL MAKE A", 9)
char.char_in("BIG JUMP.", 10)
char.char_in("PRESS MENU TO GO TO THE", 11)
char.char_in("GAME MENU.", 12)
char.char_in("PRESS ENTER TO START!", 14)
while True:
	if enter.value() is 0:
		udelay(1000000)
		break
game = Game()
ram = game.ram
game.background()
print("\nLevel", game.level)
char.char_in("LEVEL 1", xx=104, yy=30)
game.player(a=10, b=0)
while True:
	game.game_menu()
	if enter.value() is 0:
		udelay(1000000)
		game.background()
		game.move()
		break


# Nivåer: 2

# Ändringar:
# + Lagt till tidsräknare
# + Lagt till en animation när man går ur spelet
# + Lagt till en inställning som gör så att man kan ändra hur fort spelet går
# * Ändrat fördröjningstiden så att fördröjningen ALLTID är 25 ms
# * Ändrat så att gubben rör på sig hälften så mycket varje tick
# * Gubben går nu lite långsammare
# * Fixat en bug i nivå 2 som gör så att man kan ha sönder marken
