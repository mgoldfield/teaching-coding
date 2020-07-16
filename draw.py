import turtle
import warnings
from textwrap import dedent

warnings.filterwarnings("ignore", category=Warning) 
turtle.speed(0)

cmd = ''
cmdset = ''


# the triple quotes allow us to make a long string
instructions = """
f: forward
b: backward
r: right
l: left
c: color
o: curve
pu: pen up
pd: pen down
i: print instructions again
clear: clear screen, reset program, and continue
pprog: print last 20 lines of the program
stop: close screen and print out program"""

print(instructions)

# reminder '\n' means newline in a string

while cmd != 'stop':

	try: # this is to catch errors like what bean said, 
		#so it still prints the code at the end

		cmd = input("Give me a command: ")

		if cmd == 'f':  # forward
			n = input("How far? ")
			turtle.forward(int(n))
			cmdset += 'turtle.forward(' + str(n) + ')\n'

		elif cmd == 'b':
			n = input("How far? ")
			turtle.backward(int(n))	
			cmdset += 'turtle.backward(' + str(n) + ')\n'

		elif cmd == 'r': 
			n = input("How far? ")
			turtle.right(int(n))	
			cmdset += 'turtle.right(' + str(n) + ')\n'	

		elif cmd == 'l':
			n = input("How far? ")
			turtle.left(int(n))		
			cmdset += 'turtle.left(' + str(n) + ')\n'

		elif cmd == 'c': 
			c = input("What color? ")
			turtle.color(c)
			cmdset += 'turtle.color("' + str(c) + '")\n'

		elif cmd == 'clear':
			turtle.reset()
			cmdset = ''

		elif cmd == 'i':
			print(instructions)

		elif cmd == 'pu':
			turtle.penup()
			cmdset += 'turtle.penup()\n'

		elif cmd == 'pd':
			turtle.pendown()
			cmdset += 'turtle.pendown()\n'

		elif cmd == 'pprog':
			cmdlist = turtle.split('\n')
			if len(cmdlist) > 20:
				print(cmdlist[-20:])
			else:
				print(cmdlist)

		elif cmd == 'o':
			l = int(input("Length? "))
			t = float(input("Tightness (turn per length)? ")) # float is a decimal number (instead of a whole number)
			d = input("Direction (r/l)? ")

			# draw the curve
			tot_len = 1.0
			tot_turn = 1.0
			while tot_len < l:
				ratio = tot_turn / tot_len
				if ratio >= t:
					turtle.forward(1)
					tot_len += 1
				else:
					if d == 'r':
						turtle.right(1)
					elif d == 'l':
						turtle.left(1)
					else:
						print('bad direction')
						raise Exception("bad direction")
					tot_turn += 1

			# the code below constructs the loop text to print at the end
			if d == 'r':
				d = 'right'
			else:
				d = 'left'
			add_to_cmdset = """
			tot_len = 1.0
			tot_turn = 1.0
			while tot_len < {}:
				ratio = tot_turn / tot_len
				if ratio >= {}:
					turtle.forward(1)
					tot_len += 1
				else:
					turtle.{}(1)
					tot_turn += 1
			"""
			cmdset += dedent(add_to_cmdset.format(l, t, d))
			# that's the end of constructing the loop text 

		elif cmd == 'stop':
			break # end command loop
		else:
			print("I don't know that command...")
	except Exception as e:
		print(e)
		print("oops... ")
		pass

cmdset = 'import turtle\n\n' + cmdset + '\nturtle.done()'

print("\n\nHere's the program:\n")
print(cmdset + '\n\n')

turtle.bye()
print("bye!")


