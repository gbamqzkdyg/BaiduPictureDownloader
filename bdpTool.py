import bdPic
import tkinter as tk
import os

isFinished = False

def start(name, total, button, stateLabel, frame):
	global isFinished
	if isFinished:
		isFinished = False
		button['text'] = '下载'
		stateLabel['text'] = ''
		frame.grid(row = 0, columnspan = 2)
	else:
		bdPic.download(name, total)
		isFinished = True
		button['text'] = '继续下载'
		stateLabel['text'] = '下载完成！'
		frame.grid_forget()
	
def main():
	root = tk.Tk()
	root.title('bdpTool')
	frame = tk.Frame(root)
	frame.grid(row = 0, columnspan = 2)
	inputNamePrompt = tk.Label(frame, text = '请输入图片关键字：')
	inputNamePrompt.grid(row = 0, column =0)
	nameEntry = tk.Entry(frame)
	nameEntry.grid(row = 0, column =1)
	inputNumberPrompt = tk.Label(frame, text = '请输入下载图片数：')
	inputNumberPrompt.grid(row = 1, column =0)
	numberEntry = tk.Entry(frame)
	numberEntry.grid(row = 1, column =1)
	button = tk.Button(root, text = '下载', command = lambda: start(nameEntry.get(), int(numberEntry.get()), button, stateLabel, frame))
	button.grid(row = 2, column = 0)
	stateLabel = tk.Label(root, text = '')
	stateLabel.grid(row = 2, column = 1)
	root.mainloop()

main()