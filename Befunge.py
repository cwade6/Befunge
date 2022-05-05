import random

def befunge(prog):
    lines= prog.splitlines()
    progs =[list(line) for line in lines]
    height = len(prog)
    weight = len(prog[0][0])

    run= True #run the whole loop
    result = '' #What the output is
    stack = [] #place to keep track of values
    current = progs[0][0] #where are we in the program

    strmode = False #Should the program wright strings
    locate = [0,0] #where the program should move to
    direct = (1, 0) #which way is the string moving
    step = () #used in case of a jump

    def get():
        if stack:
            return stack.pop()
        return 0

    while run is True:
        if strmode:
            if current == '\"':
                strmode = False
            else:
                stack.append(ord(current))

        else:
            if current == '<':
                direct = (-1, 0)
            elif current == '>':
                direct = (1,0)
            elif current == 'v':
                direct = (0,1)
            elif current == '^':
                direct = (0,-1)
            elif current == '?':
                direct = random.choice([(-1,0), (1,0), (0,1), (0,-1)])
            elif current == '+':
                adding = get() + get()
                stack.append(adding)
            elif current == '-':
                a = get()
                subtract = get() - a
                stack.append(subtract)
            elif current == '*':
                multiply = get() * get()
                stack.append(multiply)
            elif current == '/':
                a = get()
                divide = get() // a
                atack.append(divide)
            elif current == '%':
                a = get()
                modu = get() % a
                atack.append(modu)
            elif current == '!':
                val = get()
                if val == 0:
                    stack.append(1)
                else:
                    stack.append(0)
            elif current == '\"':
                strmode =True
            elif current == "'":
                a = get()
                b = get()
                if b>a:
                    stack.append(1)
                else:
                    stack.append(0)
            elif current == '_':
                val = get()
                if val == 0:
                    direct = (1,0)
                else:
                    direct = (-1,0)
            elif current == '|':
                val = get()
                if val ==0:
                    direct = (0,1)
                else:
                    direct = (0,-1)
            elif current == ':':
                val = get()
                stack.append(val)
                stack.append(val)
            elif current == '/':
                a = get()
                b = spop
                stack.append(a)
                stack.append(b)
            elif current == '$':
                get()
            elif current == '.':
                val = get()
                result += str(val)
            elif current == ',':
                val = get()
                result += chr(val)
            elif current =='0' or current == '1' or current == '2' or current == '3' or current == '4'or current == '5'or current == '6'or current == '7'or current == '8'or current == '9':
                stack.append(int(current))
            elif current == '#':
                step = (direct[0] *2, direct[1] *2)
            elif current == '&':
                num = input("input a number: ")
                stack.append(int(num))
            elif current == '~':
                ch = input("input a charater: ")
                stack.append(ord(ch))
            elif current == '@':
                break
        if step:
            locate[0] += step[0]
            locate[1] += step[1]
            step= ()
        else:
            locate[0] += direct[0]
            locate[1] += direct[1]

        locate = [(height + locate[0]) % height, (locate[1]) // 1]
        current = progs[locate[1]][locate[0]]
    return result
