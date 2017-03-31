# A python class definition for printing formatted text on terminal.
# Initialize TextFormatter object like this:
# >>> cprint = TextFormatter()
# 
# Configure formatting style using .cfg method:
# >>> cprint.cfg('r', 'y', 'i')
# Argument 1: foreground(text) color
# Argument 2: background color
# Argument 3: text style
#
# Print formatted text using .out method:
# >>> cprint.out("Hello, world!")
#
# Reset to default settings using .reset method:
# >>> cprint.reset()

class TextFormatter:

    COLORCODE = {
        'k': 0,  # black
        'r': 1,  # red
        'g': 2,  # green
        'y': 3,  # yellow
        'b': 4,  # blue
        'm': 5,  # magenta
        'c': 6,  # cyan
        'w': 7   # white
    }

    FORMATCODE = {
        'b': 1,  # bold
        'f': 2,  # faint
        'i': 3,  # italic
        'u': 4,  # underline
        'x': 5,  # blinking
        'y': 6,  # fast blinking
        'r': 7,  # reverse
        'h': 8,  # hide
        's': 9,  # strikethrough
    }

    # constructor
    def __init__(self):
        self.reset()

    # function to reset properties
    def reset(self):
        # properties as dictionary
        self.prop = { 'st': None, 'fg': None, 'bg': None }
        return self
    
    # function to configure properties
    def cfg(self, fg, bg=None, st=None):
        # reset and set all properties
        return self.reset().st(st).fg(fg).bg(bg)

    # set text style
    def st(self, st):
        if st in self.FORMATCODE.keys(): 
            self.prop['st'] = self.FORMATCODE[st]
        return self

    # set foreground color
    def fg(self, fg):
        if fg in self.COLORCODE.keys():
            self.prop['fg'] = 30 + self.COLORCODE[fg]
        return self

    # set background color
    def bg(self,bg):
        if bg in self.COLORCODE.keys():
            self.prop['bg'] = 40 + self.COLORCODE[bg]
        return self
    
    # formatting function
    def format(self, string):
        w = [self.prop['st'],self.prop['fg'], self.prop['bg']]
        w = [ str(x) for x in w if x is not None ]
        # return formatted string
        return '\x1b[%sm%s\x1b[0m' % (';'.join(w), string) if w else string

    # output formatted string
    def out(self, string):
        print(self.format(string))
