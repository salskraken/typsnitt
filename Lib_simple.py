from pyb import SPI, Pin, delay


class St:
	DC      = "Y4"
	CS_TFT  = "Y5"
	CS_SD   = "Y3"
	LITE    = "Y2"
	RST     = "Y1"

	XSIZE   = 128
	YSIZE   = 160
	XMAX    = XSIZE-1
	YMAX    = YSIZE-1
	X0      = int(XSIZE/2)
	Y0      = int(YSIZE/2)

	SW_RESET    = 0x01
	SLPIN       = 0x10
	SLP_OUT     = 0x11
	PTLON       = 0x12
	NORON       = 0x13
	INVOFF      = 0x20
	INVON       = 0x21
	DISPOFF     = 0x28
	DISP_ON     = 0x29
	CA_SET      = 0x2A
	RA_SET      = 0x2B
	RAM_WR      = 0x2C
	RAMRD       = 0x2E
	PTLAR       = 0x30
	MAD_CTL     = 0x36
	COL_MOD     = 0x3A
	FRMCT1      = 0xB1
	FRMCT2      = 0xB2
	FRMCT3      = 0xB3
	INVCTR      = 0xB4
	DISSET      = 0xB6
	PWRCT1      = 0xC0
	PWRCT2      = 0xC1
	PWRCT3      = 0xC2
	PWRCT4      = 0xC3
	PWRCT5      = 0xC4
	VMCTR1      = 0xC5
	PWRCT6      = 0xFC
	GAMCTP      = 0xE0
	GAMCTN      = 0xE1

	def __init__(self):
		self.dbg = Pin("X9", Pin.OUT_PP)
		self.dbg.low()
		self.spi = SPI(2, SPI.MASTER, baudrate=5250000)
		ss = Pin(self.CS_TFT, Pin.OUT_PP)
		ss.low()
		self.dc = Pin(self.DC, Pin.OUT_PP)
		self.dc.low()
		self.DC_flag = False
		cs_sd = Pin(self.CS_SD, Pin.OUT_PP)
		cs_sd.high()
		self.lite = Pin(self.LITE, Pin.OUT_PP)
		self.lite.high()
		reset = Pin(self.RST, Pin.OUT_PP)
		reset.low()
		delay(2)
		reset.high()
		delay(200)

	def FastDrawPixel(self, x, y, color):
		self.dc.low()
		self.spi.send(self.CA_SET)
		self.dc.high()
		self.spi.send(bytearray([0, x, 0, x]))
		self.dc.low()
		self.spi.send(self.RA_SET)
		self.dc.high()
		self.spi.send(bytearray([0, y, 0, y]))
		self.dc.low()
		self.spi.send(self.RAM_WR)
		self.dc.high()
		self.DC_flag = True
		self.spi.send(bytearray([color >> 8, color & 0xFF]))

	def init_display(self):
		self.write_cmd(self.SW_RESET)
		delay(200)
		self.write_cmd(self.SLP_OUT)
		self.write_cmd(self.COL_MOD, 0x05)
		delay(200)
		self.dbg.high()
		self.dbg.low()
		self.write_cmd(self.DISP_ON)

	def fill_rect(self, x0, y0, x1, y1, color):
		width = x1 - x0 + 1
		height = y1 - y0 + 1
		self.set_addr_window(x0, y0, x1, y1)
		self.write_bulk(color, width, height)

	def fill_screen(self, color):
		self.fill_rect(0, 0, 127, 159, color)

	def clear_screen(self):
		self.fill_rect(0, 0, 127, 159, self.rgb(255, 255, 255))

	def rgb(self, r, g, b):
		r &= 0xF8
		g &= 0xFC
		b &= 0xF8
		return r << 8 | g << 3 | b >> 3

	def write_cmd(self, cmd, *value):
		if self.DC_flag:
			self.dc.low()
			self.DC_flag = False
		self.spi.send(cmd)
		if len(value):
			self.dc.high()
			self.DC_flag = True
			self.spi.send(bytearray(value))

	def write_bulk(self, value, reps, count=1):
		if self.DC_flag:
			self.dc.low()
		self.spi.send(self.RAM_WR)
		self.dc.high()
		self.DC_flag = True
		val_hi = value >> 8
		val_lo = value & 0xFF
		byte_arr = bytearray([val_hi, val_lo] * reps)
		self.dbg.high()
		for a in range(count):
			self.spi.send(byte_arr)
		self.dbg.low()

	def set_addr_window(self, x0, y0, x1, y1):
		self.write_cmd(self.CA_SET, 0, x0, 0, x1)
		self.write_cmd(self.RA_SET, 0, y0, 0, y1)