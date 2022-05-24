from threading import Thread
from tkinter import CENTER, Tk, Label, Frame

from api import get_weather_data

WIDTH = HEIGHT = 280

def main():
	root = Tk()
	root.wm_title('Weather Widget')
	root.wm_minsize(250, 250)

	loading_frame = Frame(root, width=WIDTH, height=HEIGHT)
	loading_frame.grid(row=0, column=0, sticky='NW')

	loading = Label(loading_frame, text='Loading...')
	loading.place(relx=0.5, rely=0.5, anchor=CENTER)

	def load_application():
		data = get_weather_data(lat=24.434727, lon=77.162304)
		loading_frame.destroy()

		data_frame = Frame(root, width=WIDTH, height=HEIGHT)
		data_frame.pack()

		for key, value in data.items():
			lab = Label(data_frame, text=f'{key}: {value}')
			lab.pack()

	thread = Thread(target=load_application)
	thread.start()

	root.mainloop()