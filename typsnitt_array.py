"""
Det här programmet skriver ut tecken på Adafruit-displayen. Det här programmet ska importeras i ett program där
tecken ska skrivas ut på skärmen. Anropa Char-klassen och metoden char_in. Skriv sedan in det du vill att den ska
skriva ut på skärmen. Du kan välja vilken rad texten ska skrivas ut på, var på skärmen, vilken färg texten ska ha.
Teckena är 7+1 pixlar höga, och bredden är inte fast. Varje rad är 8+1 pixel hög, en pixelrad är alltid tom. Det får
plats 14 rader med tecken på skärmen.
"""

from Lib_simple import St
import array
st = St()

p = st.FastDrawPixel
rgb = st.rgb
a = array.array
r = st.fill_rect


class Char:
	x = 128     				# xposition för skärmen
	y = 9						# yposition för skärmen
	b = 6						# teckenbredd
	r = 1    # radnummer (en rad tar 8 pixlar plus två som är ett mellanrum)
	colour = rgb(0, 0, 0)  	    # teckenfärg
	print_x = array.array("b", ())		# lista som berättar hur tecknet ska se ut: x
	print_y = array.array("b", ())
	lista = "!#$%&'()*+,-./ 0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
	# visa tecken som inte finns med
	#
	# lista som visar vilka tecken som finns
	# !"#$%&'()*+,-./ 0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
	# Tillgängliga tecken:
	# !"#$%&'()*+,-./ 0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

	def rad(self, reset_xyr=False, colour=rgb(255, 255, 255)):
		if self.y > 150 - self.b:
			self.r += 1
			self.y = 9
		if 14 >= self.r > 0:
			self.x = 128 - self.r * 9
		else:
			if reset_xyr is True:
				st.fill_rect(127 - self.r * 9, 9, 134 - self.r * 9, 150, colour)

	def loop(self):
		self.rad()
		for out_x, out_y in zip(self.print_x, self.print_y):
			p(out_x + self.x, out_y + self.y, self.colour)
		self.y += self.b

	def char_out(self, char=None):
		if char == "A":    # A
			self.b = 6
			self.print_x = a("b", (6, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (2, 1, 3, 1, 3, 0, 4, 0, 1, 2, 3, 4, 0, 4, 0, 4))
			self.loop()

		elif char == " ":    # mellanslag
			self.b = 0
			self.rad()
			self.y += 5

		elif char == "B":    # B
			self.b = 5
			self.print_x = a("b", (6, 6, 6, 5, 5, 4, 4, 3, 3, 3, 2, 2, 1, 1, 0, 0, 0))
			self.print_y = a("b", (0, 1, 2, 0, 3, 0, 3, 0, 1, 2, 0, 3, 0, 3, 0, 1, 2))
			self.loop()

		elif char == "C":    # C
			self.b = 5
			self.print_x = a("b", (6, 6, 6, 5, 4, 3, 2, 1, 0, 0, 0))
			self.print_y = a("b", (1, 2, 3, 0, 0, 0, 0, 0, 1, 2, 3))
			self.loop()

		elif char == "D":    # D
			self.b = 5
			self.print_x = a("b", (6, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0, 0))
			self.print_y = a("b", (0, 1, 2, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 1, 2))
			self.loop()

		elif char == "E":    # E
			self.b = 5
			self.print_x = a("b", (6, 6, 6, 6, 5, 4, 3, 3, 3, 2, 1, 0, 0, 0, 0))
			self.print_y = a("b", (0, 1, 2, 3, 0, 0, 0, 1, 2, 0, 0, 0, 1, 2, 3))
			self.loop()

		elif char == "F":    # F
			self.b = 5
			self.print_x = a("b", (6, 6, 6, 6, 5, 4, 3, 3, 3, 2, 1, 0))
			self.print_y = a("b", (0, 1, 2, 3, 0, 0, 0, 1, 2, 0, 0, 0))
			self.loop()

		elif char == "G":    # G
			self.b = 6
			self.print_x = a("b", (6, 6, 6, 6, 5, 4, 3, 3, 3, 3, 2, 2, 1, 1, 0, 0, 0, 0))
			self.print_y = a("b", (1, 2, 3, 4, 0, 0, 0, 2, 3, 4, 0, 4, 0, 4, 1, 2, 3, 4))
			self.loop()

		elif char == "H":    # H
			self.b = 5
			self.print_x = a("b", (6, 6, 5, 5, 4, 4, 3, 3, 3, 3, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (0, 3, 0, 3, 0, 3, 0, 1, 2, 3, 0, 3, 0, 3, 0, 3))
			self.loop()

		elif char == "I":    # I
			self.b = 4
			self.print_x = a("b", (6, 6, 6, 5, 4, 3, 2, 1, 0, 0, 0))
			self.print_y = a("b", (0, 1, 2, 1, 1, 1, 1, 1, 0, 1, 2))
			self.loop()

		elif char == "J":    # J
			self.b = 5
			self.print_x = a("b", (6, 5, 4, 3, 2, 1, 1, 0, 0))
			self.print_y = a("b", (3, 3, 3, 3, 3, 0, 3, 1, 2))
			self.loop()

		elif char == "K":    # K
			self.b = 6
			self.print_x = a("b", (6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (0, 4, 0, 3, 0, 2, 0, 1, 0, 2, 0, 3, 0, 4))
			self.loop()

		elif char == "L":    # L
			self.b = 5
			self.print_x = a("b", (6, 5, 4, 3, 2, 1, 0, 0, 0, 0))
			self.print_y = a("b", (0, 0, 0, 0, 0, 0, 0, 1, 2, 3))
			self.loop()

		elif char == "M":    # M
			self.b = 6
			self.print_x = a("b", (6, 6, 5, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (0, 4, 0, 1, 3, 4, 0, 2, 4, 0, 2, 4, 0, 4, 0, 4, 0, 4))
			self.loop()

		elif char == "N":    # N
			self.b = 6
			self.print_x = a("b", (6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (0, 4, 0, 1, 4, 0, 2, 4, 0, 3, 4, 0, 4, 0, 4, 0, 4))
			self.loop()

		elif char == "O":    # O
			self.b = 6
			self.print_x = a("b", (6, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0, 0))
			self.print_y = a("b", (1, 2, 3, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 1, 2, 3))
			self.loop()

		elif char == "P":    # P
			self.b = 5
			self.print_x = a("b", (6, 6, 6, 5, 5, 4, 4, 3, 3, 3, 2, 1, 0))
			self.print_y = a("b", (0, 1, 2, 0, 3, 0, 3, 0, 1, 2, 0, 0, 0))
			self.loop()

		elif char == "Q":    # Q
			self.b = 6
			self.print_x = a("b", (6, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 2, 1, 1, 0, 0, 0))
			self.print_y = a("b", (1, 2, 3, 0, 4, 0, 4, 0, 4, 0, 2, 4, 0, 3, 1, 2, 4))
			self.loop()

		elif char == "R":    # R
			self.b = 5
			self.print_x = a("b", (6, 6, 6, 5, 5, 4, 4, 3, 3, 3, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (0, 1, 2, 0, 3, 0, 3, 0, 1, 2, 0, 2, 0, 3, 0, 3))
			self.loop()

		elif char == "S":    # S
			self.b = 5
			self.print_x = a("b", (6, 6, 6, 5, 4, 3, 3, 2, 1, 0, 0, 0))
			self.print_y = a("b", (1, 2, 3, 0, 0, 1, 2, 3, 3, 0, 1, 2))
			self.loop()

		elif char == "T":    # T
			self.b = 6
			self.print_x = a("b", (6, 6, 6, 6, 6, 5, 4, 3, 2, 1, 0))
			self.print_y = a("b", (0, 1, 2, 3, 4, 2, 2, 2, 2, 2, 2))
			self.loop()

		elif char == "U":    # U
			self.b = 6
			self.print_x = a("b", (6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0, 0))
			self.print_y = a("b", (4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 1, 2, 3))
			self.loop()

		elif char == "V":    # V
			self.b = 6
			self.print_x = a("b", (6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0))
			self.print_y = a("b", (0, 4, 0, 4, 0, 4, 0, 4, 1, 3, 1, 3, 2))
			self.loop()

		elif char == "W":    # W
			self.b = 6
			self.print_x = a("b", (6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0))
			self.print_y = a("b", (0, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4, 1, 3))
			self.loop()

		elif char == "X":    # X
			self.b = 6
			self.print_x = a("b", (6, 6, 5, 5, 4, 4, 3, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (0, 4, 0, 4, 1, 3, 2, 1, 3, 0, 4, 0, 4))
			self.loop()

		elif char == "Y":    # Y
			self.b = 6
			self.print_x = a("b", (6, 6, 5, 5, 4, 4, 3, 2, 1, 0))
			self.print_y = a("b", (0, 4, 0, 4, 1, 3, 2, 2, 2, 2))
			self.loop()

		elif char == "Z":    # Z
			self.b = 6
			self.print_x = a("b", (6, 6, 6, 6, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0))
			self.print_y = a("b", (0, 1, 2, 3, 4, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4))
			self.loop()

		elif char == "1":    # 1
			self.b = 3
			self.rad()
			p(self.x + 5, self.y, self.colour)
			r(self.x, self.y + 1, self.x + 6, self.y + 1, self.colour)
			self.y += self.b

		elif char == "2":    # 2
			self.b = 5
			self.print_x = a("b", (6, 6, 5, 5, 4, 3, 2, 1, 0, 0, 0, 0))
			self.print_y = a("b", (1, 2, 0, 3, 3, 2, 1, 0, 0, 1, 2, 3))
			self.loop()

		elif char == "3":    # 3
			self.b = 5
			self.print_x = a("b", (6, 6, 6, 5, 4, 3, 3, 2, 1, 0, 0, 0))
			self.print_y = a("b", (0, 1, 2, 3, 3, 1, 2, 3, 3, 0, 1, 2))
			self.loop()

		elif char == "4":    # 4
			self.b = 5
			self.print_x = a("b", (6, 6, 5, 5, 4, 4, 3, 3, 3, 3, 2, 1, 0))
			self.print_y = a("b", (0, 3, 0, 3, 0, 3, 0, 1, 2, 3, 3, 3, 3))
			self.loop()

		elif char == "5":    # 5
			self.b = 5
			self.print_x = a("b", (6, 6, 6, 6, 5, 4, 3, 3, 3, 3, 2, 1, 0, 0, 0))
			self.print_y = a("b", (0, 1, 2, 3, 0, 0, 0, 1, 2, 3, 3, 3, 0, 1, 2))
			self.loop()

		elif char == "6":    # 6
			self.b = 5
			self.print_x = a("b", (6, 6, 6, 5, 4, 3, 3, 3, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (1, 2, 3, 0, 0, 0, 1, 2, 0, 3, 0, 3, 1, 2))
			self.loop()

		elif char == "7":    # 7
			self.b = 5
			self.print_x = a("b", (6, 6, 6, 6, 5, 4, 3, 2, 1, 0))
			self.print_y = a("b", (0, 1, 2, 3, 3, 2, 2, 1, 1, 0))
			self.loop()

		elif char == "8":    # 8
			self.b = 5
			self.print_x = a("b", (6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (1, 2, 0, 3, 0, 3, 1, 2, 0, 3, 0, 3, 1, 2))
			self.loop()

		elif char == "9":    # 9
			self.b = 5
			self.print_x = a("b", (0, 0, 1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6))
			self.print_y = a("b", (2, 1, 0, 3, 3, 3, 2, 1, 3, 0, 3, 0, 2, 1))
			self.loop()

		elif char == "0":    # 0
			self.b = 5
			self.print_x = a("b", (6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (1, 2, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 1, 2))
			self.loop()

		elif char == "a":    # a
			self.b = 5
			self.print_x = a("b", (4, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0, 0))
			self.print_y = a("b", (1, 2, 3, 0, 3, 0, 3, 0, 3, 1, 2, 3))
			self.loop()

		elif char == "b":    # b
			self.b = 5
			self.print_x = a("b", (6, 5, 4, 3, 3, 3, 2, 2, 1, 1, 0, 0, 0))
			self.print_y = a("b", (0, 0, 0, 0, 1, 2, 0, 3, 0, 3, 0, 1, 2))
			self.loop()

		elif char == "c":    # c
			self.b = 5
			self.print_x = a("b", (4, 4, 4, 3, 2, 1, 0, 0, 0))
			self.print_y = a("b", (1, 2, 3, 0, 0, 0, 1, 2, 3))
			self.loop()

		elif char == "d":    # d
			self.b = 5
			self.print_x = a("b", (6, 5, 4, 3, 3, 3, 2, 2, 1, 1, 0, 0, 0))
			self.print_y = a("b", (3, 3, 3, 1, 2, 3, 0, 3, 0, 3, 1, 2, 3))
			self.loop()

		elif char == "e":    # e
			self.b = 5
			self.print_x = a("b", (4, 4, 3, 3, 2, 2, 2, 2, 1, 0, 0, 0))
			self.print_y = a("b", (1, 2, 0, 3, 0, 1, 2, 3, 0, 1, 2, 3))
			self.loop()

		elif char == "f":    # f
			self.b = 4
			self.print_x = a("b", (6, 5, 4, 3, 3, 3, 2, 1, 0))
			self.print_y = a("b", (2, 1, 1, 0, 1, 2, 1, 1, 1))
			self.loop()

		elif char == "g":    # g
			self.b = 5
			self.print_x = a("b", (4, 4, 4, 3, 3, 2, 2, 1, 1, 1, 0, -1, -1, -1))
			self.print_y = a("b", (1, 2, 3, 0, 3, 0, 3, 1, 2, 3, 3, 0, 1, 2))
			self.loop()

		elif char == "h":    # h
			self.b = 5
			self.print_x = a("b", (6, 5, 4, 3, 3, 3, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (0, 0, 0, 0, 1, 2, 0, 3, 0, 3, 0, 3))
			self.loop()

		elif char == "i":    # i
			self.b = 2
			self.rad()
			p(self.x + 5, self.y, self.colour)
			r(self.x, self.y, self.x + 3, self.y, self.colour)
			self.y += self.b

		elif char == "j":    # j
			self.b = 4
			self.print_x = a("b", (5, 3, 2, 1, 0, -1, -1))
			self.print_y = a("b", (2, 2, 2, 2, 2, 0, 1))
			self.loop()

		elif char == "k":    # k
			self.b = 5
			self.print_x = a("b", (6, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (0, 0, 0, 3, 0, 2, 0, 1, 0, 2, 0, 3))
			self.loop()

		elif char == "l":    # l
			self.b = 2
			self.rad()
			r(self.x, self.y, self.x + 6, self.y, self.colour)
			self.y += self.b

		elif char == "m":    # m
			self.b = 6
			self.print_x = a("b", (4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0, 0))
			self.print_y = a("b", (0, 1, 3, 0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4))
			self.loop()

		elif char == "n":    # n
			self.b = 5
			self.print_x = a("b", (4, 4, 3, 3, 3, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (0, 2, 0, 1, 3, 0, 3, 0, 3, 0, 3))
			self.loop()

		elif char == "o":    # o
			self.b = 5
			self.print_x = a("b", (4, 4, 3, 3, 2, 2, 1, 1, 0, 0))
			self.print_y = a("b", (1, 2, 0, 3, 0, 3, 0, 3, 1, 2))
			self.loop()

		elif char == "p":    # p
			self.b = 5
			self.print_x = a("b", (4, 4, 4, 3, 3, 2, 2, 1, 1, 1, 0, -1))
			self.print_y = a("b", (0, 1, 2, 0, 3, 0, 3, 0, 1, 2, 0, 0))
			self.loop()

		elif char == "q":    # q
			self.b = 5
			self.print_x = a("b", (4, 4, 4, 3, 3, 2, 2, 1, 1, 1, 0, -1))
			self.print_y = a("b", (3, 2, 1, 3, 0, 3, 0, 3, 2, 1, 3, 3))
			self.loop()

		elif char == "r":    # r
			self.b = 5
			self.print_x = a("b", (4, 4, 4, 3, 3, 2, 1, 0))
			self.print_y = a("b", (0, 2, 3, 0, 1, 0, 0, 0))
			self.loop()

		elif char == "s":    # s
			self.b = 5
			self.print_x = a("b", (4, 4, 4, 3, 2, 2, 1, 0, 0, 0))
			self.print_y = a("b", (1, 2, 3, 0, 1, 2, 3, 0, 1, 2))
			self.loop()

		elif char == "t":    # t
			self.b = 4
			self.print_x = a("b", (6, 5, 4, 3, 3, 3, 2, 1, 0))
			self.print_y = a("b", (1, 1, 1, 0, 1, 2, 1, 1, 2))
			self.loop()

		elif char == "u":    # u
			self.b = 5
			self.print_x = a("b", (4, 4, 3, 3, 2, 2, 1, 1, 0, 0, 0))
			self.print_y = a("b", (0, 3, 0, 3, 0, 3, 0, 3, 1, 2, 3))
			self.loop()

		elif char == "v":    # v
			self.b = 6
			self.print_x = a("b", (4, 4, 3, 3, 2, 2, 1, 1, 0))
			self.print_y = a("b", (0, 4, 0, 4, 0, 4, 1, 3, 2))
			self.loop()

		elif char == "w":    # w
			self.b = 6
			self.print_x = a("b", (4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0))
			self.print_y = a("b", (0, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4, 1, 3))
			self.loop()

		elif char == "x":    # x
			self.b = 6
			self.print_x = a("b", (4, 4, 3, 3, 2, 1, 1, 0, 0))
			self.print_y = a("b", (0, 4, 1, 3, 2, 1, 3, 0, 4))
			self.loop()

		elif char == "y":    # y
			self.b = 6
			self.print_x = a("b", (4, 4, 3, 3, 2, 2, 1, 0, -1))
			self.print_y = a("b", (0, 4, 0, 4, 1, 3, 2, 1, 0))
			self.loop()

		elif char == "z":    # z
			self.b = 6
			self.print_x = a("b", (4, 4, 4, 4, 4, 3, 2, 1, 0, 0, 0, 0, 0))
			self.print_y = a("b", (0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4))
			self.loop()

		elif char == ".":    # .
			self.b = 4
			self.rad()
			st.fill_rect(self.x, self.y, self.x + 1, self.y + 1, self.colour)
			self.y += self.b

		elif char == ":":    # :
			self.b = 4
			self.rad()
			st.fill_rect(self.x, self.y, self.x + 1, self.y + 1, self.colour)
			st.fill_rect(self.x + 4, self.y, self.x + 5, self.y + 1, self.colour)
			self.y += self.b

		elif char == ";":    # ;
			self.b = 4
			self.print_x = a("b", (5, 5, 4, 4, 2, 2, 1, 1, 0, -1))
			self.print_y = a("b", (0, 1, 0, 1, 0, 1, 0, 1, 1, 0))
			self.loop()

		elif char == ",":    # ,
			self.b = 4
			self.print_x = a("b", (2, 2, 1, 1, 0, -1))
			self.print_y = a("b", (0, 1, 0, 1, 1, 0))
			self.loop()

		elif char == "!":    # !
			self.b = 3
			self.rad()
			st.fill_rect(self.x, self.y, self.x, self.y, self.colour)
			st.fill_rect(self.x + 2, self.y, self.x + 6, self.y, self.colour)
			self.y += self.b

		elif char == "?":    # ?
			self.b = 6
			self.print_x = a("b", (6, 6, 6, 5, 5, 4, 3, 2, 0))
			self.print_y = a("b", (1, 2, 3, 0, 4, 3, 2, 2, 2))
			self.loop()

		elif char == "'":    # '
			self.b = 2
			self.print_x = a("b", (6, 5, 4))
			self.print_y = a("b", (0, 0, 0))
			self.loop()

		elif char == '"':    # "
			self.b = 4
			self.print_x = a("b", (6, 6, 5, 5, 4, 4))
			self.print_y = a("b", (0, 2, 0, 2, 0, 2))
			self.loop()

		elif char == "_":    # _
			self.b = 7
			self.print_x = a("b", (0, 0, 0, 0, 0, 0))
			self.print_y = a("b", (0, 1, 2, 3, 4, 5))
			self.loop()

		elif char == "@":    # @
			self.b = 8
			self.print_x = a("b", (6, 6, 6, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, -1))
			self.print_y = a("b", (2, 3, 4, 1, 5, 0, 3, 4, 6, 0, 2, 4, 6, 0, 3, 4, 6, 1, 4, 6, 2, 3, 6, 5))
			self.loop()

		elif char == "#":    # #
			self.b = 7
			self.print_x = a("b", (6, 6, 5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, -1, -1))
			self.print_y = a("b", (1, 3, 1, 3, 0, 1, 2, 3, 4, 5, 1, 3, 1, 3, 0, 1, 2, 3, 4, 5, 1, 3, 1, 3))
			self.loop()

		elif char == "%":    # %
			self.b = 8
			self.print_x = a("b", (6, 6, 5, 5, 5, 4, 4, 3, 2, 2, 1, 1, 1, 0, 0))
			self.print_y = a("b", (1, 6, 0, 2, 5, 1, 4, 3, 2, 5, 1, 4, 6, 0, 5))
			self.loop()

		elif char == "/":    # /
			self.b = 6
			self.print_x = a("b", (6, 5, 4, 3, 2, 1, 0))
			self.print_y = a("b", (4, 3, 3, 2, 1, 1, 0))
			self.loop()

		elif char == "`":    # `
			self.b = 3
			self.print_x = a("b", (6, 5))
			self.print_y = a("b", (0, 1))
			self.loop()

		elif char == "&":    # &
			self.b = 6
			self.print_x = a("b", (6, 5, 5, 4, 4, 3, 3, 2, 2, 2, 1, 1, 0, 0, 0))
			self.print_y = a("b", (2, 1, 3, 1, 2, 1, 2, 0, 2, 4, 0, 3, 1, 2, 4))
			self.loop()

		elif char == "*":    # *
			self.b = 6
			self.print_x = a("b", (6, 6, 6, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 2, 2, 2))
			self.print_y = a("b", (0, 2, 4, 1, 2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 0, 2, 4))
			self.loop()

		elif char == "$":    # $
			self.b = 6
			self.print_x = a("b", (6, 5, 5, 5, 5, 4, 4, 3, 3, 3, 2, 2, 1, 1, 1, 1, 0))
			self.print_y = a("b", (2, 1, 2, 3, 4, 0, 2, 1, 2, 3, 2, 4, 0, 1, 2, 3, 2))
			self.loop()

		elif char == "(":    # (
			self.b = 4
			self.print_x = a("b", (6, 5, 4, 3, 2, 1, 0))
			self.print_y = a("b", (2, 1, 0, 0, 0, 1, 2))
			self.loop()

		elif char == ")":    # )
			self.b = 4
			self.print_x = a("b", (6, 5, 4, 3, 2, 1, 0))
			self.print_y = a("b", (0, 1, 2, 2, 2, 1, 0))
			self.loop()

		elif char == "[":    # [
			self.b = 4
			self.print_x = a("b", (6, 6, 6, 5, 4, 3, 2, 1, 0, 0, 0))
			self.print_y = a("b", (0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 2))
			self.loop()

		elif char == "]":    # ]
			self.b = 4
			self.print_x = a("b", (6, 6, 6, 5, 4, 3, 2, 1, 0, 0, 0))
			self.print_y = a("b", (2, 1, 0, 2, 2, 2, 2, 2, 0, 1, 2))
			self.loop()

		elif char == "{":    # {
			self.b = 4
			self.print_x = a("b", (6, 6, 5, 4, 3, 2, 1, 0, 0))
			self.print_y = a("b", (1, 2, 1, 1, 0, 1, 1, 1, 2))
			self.loop()

		elif char == "}":    # }
			self.b = 4
			self.print_x = a("b", (6, 6, 5, 4, 3, 2, 1, 0, 0))
			self.print_y = a("b", (1, 0, 1, 1, 2, 1, 1, 1, 0))
			self.loop()

		elif char == "^":    # ^
			self.b = 6
			self.print_x = a("b", (6, 5, 5, 4, 4))
			self.print_y = a("b", (2, 1, 3, 0, 4))
			self.loop()

		elif char == "+":    # +
			self.b = 6
			self.print_x = a("b", (5, 4, 3, 3, 3, 3, 3, 2, 1))
			self.print_y = a("b", (2, 2, 0, 1, 2, 3, 4, 2, 2))
			self.loop()

		elif char == "-":    # -
			self.b = 6
			self.print_x = a("b", (3, 3, 3, 3, 3))
			self.print_y = a("b", (0, 1, 2, 3, 4))
			self.loop()

		elif char == "=":    # =
			self.b = 6
			self.print_x = a("b", (4, 4, 4, 4, 4, 2, 2, 2, 2, 2))
			self.print_y = a("b", (0, 1, 2, 3, 4, 0, 1, 2, 3, 4))
			self.loop()

		elif char == "|":    # |
			self.b = 2
			self.print_x = a("b", (6, 5, 4, 3, 2, 1, 0, -1))
			self.print_y = a("b", (0, 0, 0, 0, 0, 0, 0, 0))
			self.loop()

		elif char == "<":    # <
			self.b = 5
			self.print_x = a("b", (5, 4, 4, 3, 2, 2, 1))
			self.print_y = a("b", (3, 1, 2, 0, 1, 2, 3))
			self.loop()

		elif char == ">":    # >
			self.b = 5
			self.print_x = a("b", (5, 4, 4, 3, 2, 2, 1))
			self.print_y = a("b", (0, 2, 1, 3, 2, 1, 0))
			self.loop()

		elif char == "\\":    # \
			self.b = 6
			self.print_x = a("b", (6, 5, 4, 3, 2, 1, 0))
			self.print_y = a("b", (0, 1, 1, 2, 3, 3, 4))
			self.loop()

		elif char == "~":    # ~
			self.b = 6
			self.print_x = a("b", (4, 3, 3, 3, 2))
			self.print_y = a("b", (1, 0, 2, 4, 3))
			self.loop()

		elif char == "\n":    # newline
			self.y = 1244
			self.rad()

		else:    # Det här tecknet skrivs ut om tecknet inte finns tillgänligt här
			self.b = 6
			self.rad()
			st.fill_rect(self.x - 1, self.y, self.x + 6, self.y + 4, self.colour)
			self.y += self.b

	def char_in(self, chars, rad=0, colour=rgb(0, 0, 0), xx=115, yy=9, print_x_y=False):
		self.x = xx
		self.y = yy
		self.r = rad
		self.rad()
		self.colour = colour
		for c in chars:
			self.char_out(c)
			if print_x_y:
				print(self.x, self.y)