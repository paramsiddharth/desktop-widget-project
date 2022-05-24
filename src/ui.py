from io import BytesIO
from threading import Thread
from tkinter import CENTER, PhotoImage, Tk, Label, Frame, Toplevel
from urllib.request import urlopen
from base64 import b64encode

from api import get_weather_data
from config import get_config

WIDTH = HEIGHT = 300

def main():
	root = Tk()
	root.wm_title('Weather Widget')
	root.wm_minsize(250, 250)
	root.wm_iconphoto(True, PhotoImage(file='icon.png'))

	loading_frame = Frame(root, width=WIDTH, height=HEIGHT)
	loading_frame.grid(row=0, column=0, sticky='NW')

	loading = Label(loading_frame, text='Loading...')
	loading.place(relx=0.5, rely=0.5, anchor=CENTER)

	def load_application():
		config = get_config()

		data = get_weather_data(lat=config['lat'], lon=config['lon'])
		req = urlopen(data.get('icon'))
		icon = req.read()
		req.close()
		icon = b64encode(icon)

		loading_frame.destroy()

		d = Frame(root, width=WIDTH, height=HEIGHT)
		d.pack(pady=(20, 20))

		Label(d, text=data['location'], font='Arial 17 bold').pack(pady=(0, 5))

		photo = PhotoImage(data=icon)

		img = Label(d, image=photo, bg='gray')
		img.image = photo
		img.pack(pady=(5, 5))

		Label(d, text=data['description'].capitalize(), font='Arial 12').pack()

		d2 = Frame(d)
		d2.pack()

		Label(d2, text=f"{data['temp']}°", font='Arial 10', fg='green').grid(row=0, column=0)
		Label(d2, text=f"{data['temp_felt']}°", font='Arial 10', fg='blue').grid(row=0, column=1)
		Label(d2, text=f"({data['temp_min']}°-{data['temp_max']}°)", font='Arial 10', fg='red').grid(row=0, column=2)

		Label(d, text=f"Pressure: {data['pressure']}", font='Arial 10').pack()
		Label(d, text=f"Humidity: {data['humidity']}%", font='Arial 10').pack()
		Label(d, text=f"Time zone: {data['timezone']}", font='Arial 10').pack()
		Label(d, text=f"Sea level: {data['sea_level']}", font='Arial 10').pack()
		Label(d, text=f"Wind speed: {data['wind_speed']} ({data['wind_direction'].capitalize()})", font='Arial 10').pack()
		Label(d, text=f"Wind gust: {data['wind_gust']}", font='Arial 10').pack()

	thread = Thread(target=load_application)
	thread.start()

	root.mainloop()