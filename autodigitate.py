from pynput.keyboard import Key, Controller ,Listener
from time import sleep
import pyperclip

def get_word():
	input("copy the word and press Enter")
	word = pyperclip.paste()
	print("the word is:")
	print(word)
	#validate word copy
	if input("Correct? S/N  ") not in ["S","s"]:
		print("Reboot...")
		return get_word()
	else:
		return word
def key_word(word,keyboard = Controller()):
	tabs = 0
	for char in word:
		if char == '\n':
			keyboard.press(Key.down)
			keyboard.release(Key.down)
			keyboard.press(Key.shift)
			for _ in range(tabs):
				keyboard.press(Key.tab)
				keyboard.release(Key.tab)
			keyboard.release(Key.shift)

		elif char == '\t':
			tabs = tabs + 1
			keyboard.press(Key.tab)
			keyboard.release(Key.tab)
			pass
		else:
			keyboard.press(char)
			keyboard.release(char)
		sleep(0.01)
def detect_key_pressed(*expected_keys):
	def on_press(key_read):
		if key_read in expected_keys:
			return False
	with Listener(on_press=on_press) as listener:
		listener.join()
if __name__=="__main__":
	word = get_word()
	print("locate where you are going to key the word and press SHIFT.")
	detect_key_pressed(Key.shift,Key.shift_r)
	sleep(0.3)
	print("start...")
	key_word(word)
	print("done.")
