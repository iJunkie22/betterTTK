__author__ = 'ethan'
import ttk
import Tkinter


class Props(object, Tkinter.Misc):
    def __init__(self):
        self._text = None
        self._background = None
        self._foreground = None

    @property
    def text(self):
        self._text = self.cget('text')
        return self._text

    @text.setter
    def text(self, value):
        self.configure(text=value)
        self._text = value

    @property
    def background(self):
        if self.cget("style"):
            c_style = self.cget("style")
            self._background = self.tk.call("ttk::style", "lookup", c_style, '-background', '', None)
            return self._background

    @background.setter
    def background(self, value):
        if self.cget("style"):
            c_style = self.cget("style")
            Style().background(value=value, style=c_style)
            self._background = value

    @property
    def foreground(self):
        if self.cget("style"):
            c_style = self.cget("style")
            self._foreground = self.tk.call("ttk::style", "lookup", c_style, '-foreground', '', None)
            return self._foreground

    @foreground.setter
    def foreground(self, value):
        if self.cget("style"):
            c_style = self.cget("style")
            Style().foreground(value=value, style=c_style)
            self._foreground = value


class Label(ttk.Label, Props):
        
    def font(self, font=None):
        if font:
            self.configure(font=font)
        else:
            return self.cget("font")

    def style(self, style_name=None):
        if style_name:
            self.configure(style=style_name)
        else:
            return self.cget("style")


class Button(ttk.Button, Props):
    pass


class TextInput(ttk.Entry, Props):
    @property
    def value(self):
        pass

    @value.getter
    def c_value(self):
        textvar = self.cget('textvariable')
        return self.getvar(textvar)


class Style(ttk.Style, object):
    def __str__(self):
        return self.style_name

    @property
    def style_name(self):
        return getattr(self, "_style_name")

    def name_style(self, name):
        setattr(self, "_style_name", name)

    def foreground(self, value=None, style=None):
        if hasattr(self, "_style_name"):
            pass
        else:
            setattr(self, "_style_name", style)
        if value:
            self.configure(self.style_name, foreground=value)
        else:
            return "blah"

    def background(self, value=None, style=None):
        if hasattr(self, "_style_name"):
            pass
        else:
            setattr(self, "_style_name", style)
        if value:
            self.configure(self.style_name, background=value)
        else:
            return "blah"
