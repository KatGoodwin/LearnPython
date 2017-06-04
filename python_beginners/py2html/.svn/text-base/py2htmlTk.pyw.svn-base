"""######################################
####  A Tkinter GUI for py2html   ####
######################################
The main use for this program is to create
marked up Python code for inclusion into a web page.

The markup process is general enough that it can be used
for other formats - such as using forum posting
tags.


################
#### TO USE ####
################

1.] Paste code into the top multi-line field or
use the "File->Open Source File ..." to a read file
in.

2.] Click the "Make Web-Page" or "Make Block" buttons to make a
complete web page or just a block of HTML.

3.] Click "Copy All to Clipboard" or select the code you want and type 'CTRL-C'.

You can edit the results in the output field before copying to the clipboard.
To save the text to a file choose "File->Save Output As ..." in the file menu.

NOTE: Clicking the Save As button will save whatever the contents of the Output
area happens to be. You can use this feature to do small editing jobs on
web-page temaplates and style files (See Configuration section).

The out-of-the box configuration will markup Python code with
IDLE like default colours using a stylesheet. There are other possibilities
to be selected in the Configuration menu or you can define your own.


#######################
#### CONFIGURATION ####
#######################

If you select "Configuration->Modify Configuration" you can change how
code is marked up.

You can replace the default web-page template with your own. The program
expects a text file with one %s field where the code is to be inserted.
Clicking "View" pastes the files content into the Output area where it can be
inspected and edited if required.

Select the style file you need to use.

################
Modifying layout.
################
This program not only marks up the code with tags but it can also apply some simple rules
to the code layout to make it consistent.
"Don't ..." Don't make any changes to the codes layout !
"Style 1 "  Assignment/comparision operators are given a space either side. Other binary operators
            have spaces removed from either side. Sequence operators e.g. comma have a space to the right.
            In function/method definitions - assignment operators have no space either side. This complies to
            some extent with PEP8 guideline.
"Style 2 "  As Style 1 except that binary opeartors are given one space either side. The space is also applied
            to unary (+-~) operators!

I use this feature to tidy up my own code. I produce the webpage, copy its contents to the clipboard
and paste it over the original code in IDLE. :)

##############
Using Entities.
##############
These options allow the replacement of characters by browser safe codes.(They may be interpreted as HTML). 
For example the < character is replaced by the sequence &lt; This  tells the browser to just display the <
character and not try to use it as the beginning of an HTML tag. The third option < > & " is normally what
you want ok but if your code contains non-english accented characters or symbols then it may be better to use
the fourth oprion. When producing marked up code for posting into a forum for example iit s a a good idea to
preview it first and confim the entity settings are correct for that site. The writers of web-based forms
do not seem to agree which entities must be translated.

###########################
Replace spaces and newlines.
###########################
Similar to entities but required if you are pasting the code into a page that does not preserve the layout
of the text.
(Normal web settings are to replace multiple spaces with just one and ignore newline characters.)
This setting replaces multiple spaces with a sequence of space and the &nbsp; entity. Newlines are
replaced by <br> and multiple newlines are replaced by <br> space <br>...

#####################
#### STYLE FILES ####
#####################
Style files detail what tags are applied to mark up the code.
The Configuration dialog allows the selection of style files. All style files found in the working directory
are automatically listed.

You can modify the tags used for highlighting and defining the enclosing
block by selecting one of the style files. (You can even edit the file in teh Output area.) Several examples
are provided for you to explore. Style files are user editable text, here is an example:

    #User editable HTML style substitutions
    # This file uses font tags
    # Format:
    # styleName | start | end
    #


    block | <pre class="python_code" id="pycode"> | </pre>
    key | <font color="#000000">|</font> 
    num | <font color="#000000"> | </font>
    str | <font color="green"> | </font>
    op  | <font color="#000000"> | </font>
    com | <font color="red"> | </font>
    res | <font color="orange"> | </font>
    def | <font color="blue"> | </font>
    brk | <font color="#000000"> | </font>

Note:
This program will create a temporary file for previewing. It is not deleted
but it is overwritten each time.
--END--
"""
import py2html
import Tkinter
import ScrolledText
import tkFileDialog
import tkMessageBox
import glob


try: 
    import cPickle as pickle
except ImportError: 
    import pickle
    
__version__ = "0.65"
__author__ = "Paul Hardwick <paul@peck.org.uk>"
__date__ = "13 March 2004"
class pdict(dict): 
    '''A persistent dictionary class with versioning
        
        a = pdict("name")
        a["tom"]=8.4
        a["harry"]="three"
        b = pdict("name",dictionary) #pre-load b with a dictionary (ignore any data in "name")
        a.save() # store data in file "name_pdict"

        Sub-class to create your own version handling:
        class x(pdict):
            class_version = "1.3"

            def update_version(self):
                print "do my own data conversion here"
    '''
    
    class_version = "0.0" #the version of the class - used for comparison with pickled data
    class_ext = "_pdict" #mangling file extension used for pickle file (to advoid overwritting other files)
    
    def __new__(cls, pd_name, *tdata): 
        '''Called before __init__, returns a new pdict or an un-pickled pdict.'''
        if not len(tdata): 
            try: 
                data = pickle.loads(open("%s%s"%(pd_name, cls.class_ext), "rb").read())
                if not isinstance(data, pdict): 
                    raise TypeError, "pickle file not a pdict object pickle"
                return data
            except IOError: 
                return dict.__new__(cls) #actually sub-classed to pdict in assignment
        else: 
            if not isinstance(tdata[0], dict): 
                raise TypeError, "expected a dictionary for second argument"
            return dict.__new__(cls, *tdata) #actually sub-classed to pdict in assignment
        
    def __setstate__(self, state): 
        '''Called by the un-pickling process - allows instance data to be correctly re-created.
        Note: __init__ is not called'''
        self.class_version = state["class_version"]
        self._pd_name = state["_pd_name"]

    def __init__(self, pd_name, *tdata): 
        '''Sets up the pickle file name for this instance. If this instance is
        re-created from a pickle then version checking is done'''
        dict.__init__(self, tdata)
        if not isinstance(pd_name, str): 
            raise TypeError, "first argument must be a string for pickle name"
        self._pd_name = pd_name
        #check if loaded from a pickle...
        if hasattr(self, "class_version") and (self.class_version != self.__class__.class_version): 
            self.update_version() #do version checking/conversion
        else: 
            self.class_version = self.__class__.class_version
        
    def getversion(self): 
        '''Returns the version number of this persistent object'''
        return self.class_version

    def update_version(self): 
        '''This method is called by __init__ if the pickled datatype loaded from file is not the same value as self.class_version.
        Overide this method in a sub-class to perfom whatever tasks you need.
        Update data and use data.save() if necessary. Nothing returned.
        '''
        raise TypeError, "The class and pickle versions do not match."


    def save(self): 
        '''Save data to file.'''
        data = pickle.dumps(self)
        f = open("%s%s"%(self._pd_name, self.class_ext), "wb")
        f.write(data)
        f.close()
        
class GUIconverter: 
  
    def __init__(self): 

        self.root = Tkinter.Tk()
        self.root.geometry('640x480+120+0')
        self.frame0 = Tkinter.Frame(self.root)
        self.makemenu()

        self.format_options = ["Don't modify layout", 
                               'Use layout style 1', 
                               'Use layout style 2']
        self.format_op = Tkinter.StringVar()
        self.format_op.set(self.format_options[1])
        self.settings = {"name": Tkinter.StringVar(), 
                        "browser": Tkinter.IntVar(), 
                        "template": Tkinter.StringVar(), 
                        "stylefile": Tkinter.StringVar(), 
                        "formatstyle": Tkinter.StringVar(), 
                        "entities": Tkinter.StringVar(), 
                        "replace": Tkinter.IntVar(), 
                        "pysrccol": Tkinter.StringVar(), 
                        "pysrccolbk": Tkinter.StringVar(), 
                        "pysrcfont": Tkinter.StringVar(), 
                        "pysrcsize": Tkinter.StringVar(), 
                        "pyoutcol": Tkinter.StringVar(), 
                        "pyoutcolbk": Tkinter.StringVar(), 
                        "pyoutfont": Tkinter.StringVar(), 
                        "pyoutsize": Tkinter.StringVar(), 
                         }
        self.format_options = ["Don't modify layout", 
                               'Use layout style 1', 
                               'Use layout style 2']
        self.entity_options = ["None", 
                               '< > &', 
                               '< > & "', 
                               '< > & " \'', 
                               '< > & " \' and all none ASCII']
        pdict.class_ext = ".p2h"
        self.labeltext = Tkinter.StringVar()
        self.labeltext.set("Output:")
        self.filedsettings = pdict("default")
        if not self.filedsettings.keys(): 
            self.defaultconfig()
        else: 
            self.initconfig()
        for n in self.settings: 
            print n, self.settings[n].get()
        self.frame1 = Tkinter.Frame(self.root, bg = 'red', borderwidth = 4, relief = Tkinter.GROOVE)
        self.frame2 = Tkinter.Frame(self.root)
        
        self.root.title("PY2HTML syntax highlighter")

        
        #frame1
        subframe = Tkinter.Frame(self.frame1)
        Tkinter.Label(subframe, text = "Paste in Python code (CTRL-V):").pack(side = Tkinter.LEFT, anchor = Tkinter.W)
        self.clear = Tkinter.Button(subframe, text = "Clear Input", background = 'grey', command = self.ClearInput)
        self.clear.pack(side = Tkinter.RIGHT, anchor = Tkinter.E)
        subframe.pack(expand = Tkinter.N, fill = Tkinter.X)
        self.input = ScrolledText.ScrolledText(self.frame1, height = 10)
        self.input.config(bg = self.settings["pysrccolbk"].get(), 
                          fg = self.settings["pysrccol"].get(), 
                          font = (self.settings["pysrcfont"].get(), int(self.settings["pysrcsize"].get()), 'normal'))
        self.input.pack(side = Tkinter.TOP, anchor = Tkinter.N, expand = Tkinter.Y, fill = Tkinter.BOTH)
        subframe.pack(side = Tkinter.TOP, anchor = Tkinter.E, expand = Tkinter.N, fill = Tkinter.BOTH)

        #frame 2
        subframe = Tkinter.Frame(self.frame2)
        Tkinter.Button(subframe, text = "Make Web-Page", background = 'grey', 
                       command = self.ToPage).pack(side = Tkinter.LEFT, expand = Tkinter.N, anchor = Tkinter.N)
        Tkinter.Button(subframe, text = "Make Block", background = 'grey', 
                       command = self.ToBlock).pack(side = Tkinter.LEFT, expand = Tkinter.N, anchor = Tkinter.W)
        Tkinter.Checkbutton(subframe, text = 'Preview in browser', variable = self.settings["browser"], 
                    font = ('times', 8, 'normal')).pack(side = Tkinter.LEFT, expand = Tkinter.N, anchor = Tkinter.W)
        subframe.pack(expand = Tkinter.N, fill = Tkinter.X)
        self.outtext = Tkinter.Label(self.frame2, textvariable = self.labeltext).pack(side = Tkinter.TOP, anchor = Tkinter.W, 
                                                                         expand = Tkinter.N)
        self.output = ScrolledText.ScrolledText(self.frame2, height = 10)
        self.output.config(bg = 'grey', fg = 'black', font = ('courier', 9, 'normal'))
        self.output.pack(expand = Tkinter.Y, fill = Tkinter.BOTH, anchor = Tkinter.N, side = Tkinter.TOP)

        subframe = Tkinter.Frame(self.frame2)
        Tkinter.Button(subframe, text = "Copy All to Clipboard", background = 'grey', 
                       command = self.copy).pack(side = Tkinter.LEFT, expand = Tkinter.Y)
        Tkinter.Button(subframe, text = "Save As ...", background = 'grey', 
                       command = self.savefile).pack(side = Tkinter.LEFT, expand = Tkinter.Y)
        subframe.pack(expand = Tkinter.N, fill = Tkinter.X)
        
        self.frame1.pack(expand = Tkinter.N, fill = Tkinter.X)
        self.frame2.pack(expand = Tkinter.Y, fill = Tkinter.BOTH, side = Tkinter.TOP, anchor = Tkinter.N)
        self.root.wait_window()

    def makemenu(self): 
        #Build the menu
        main = Tkinter.Menu(self.root)
        self.root.config(menu = main)

        file = Tkinter.Menu(main, tearoff = 0)
        file.add_command(label = "Open Source File ...", command = self.openfile, underline = 0)
        file.add_command(label = "Save Output As ...", command = self.savefile, underline = 0)
        file.add_command(label = "Quit", command = self.root.destroy, underline = 0)
        main.add_cascade(label = "File", menu = file, underline = 0)

        config = Tkinter.Menu(main, tearoff = 0)
        config.add_command(label = "Load Configuration ...", command = self.loadconfig, underline = 2)
        config.add_command(label = "Modify Configuration ...", command = self.GUIconfig, underline = 2)
        config.add_command(label = "Save Configuration ...", command = self.saveconfig, underline = 2)
        config.add_command(label = "Set current configuration as default.", command = self.setdefaultconfig, underline = 2)
        main.add_cascade(label = "Configuration", menu = config, underline = 0)

        help = Tkinter.Menu(main, tearoff = 0)
        help.add_command(label = "Help", command = self.help, underline = 0)
        help.add_command(label = "About", command = self.showabout, underline = 0)
        main.add_cascade(label = "Help", menu = help, underline = 0)
    
    def defaultconfig(self): 
        self.settings["name"].set("default")
        self.settings["browser"].set(1)
        self.settings["template"].set("<default>")
        self.settings["stylefile"].set("<default>")
        self.settings["formatstyle"].set(self.format_options[1])
        self.settings["entities"].set(self.entity_options[2])
        self.settings["replace"].set(0)
        self.settings["pysrccol"].set("black")
        self.settings["pysrccolbk"].set("white")
        self.settings["pysrcfont"].set("courier")
        self.settings["pysrcsize"].set("10")
        self.settings["pyoutcol"].set("black")
        self.settings["pyoutcolbk"].set("grey")
        self.settings["pyoutfont"].set("courier")
        self.settings["pyoutsize"].set("10")
        
    def initconfig(self): 
        for key, value in self.filedsettings.items(): 
            self.settings[key].set(value)
            
    def setdefaultconfig(self): 
        for key in self.settings.keys(): 
            self.filedsettings[key] = self.settings[key].get()
        self.filedsettings.save()
        
    def loadconfig(self): 
        filename = tkFileDialog.askopenfilename(filetypes = (("Configurations", "*.p2h"), ))
        if filename: 
            try: 
                filename = filename[: -4]
                self.filedsettings = pdict(filename)
                self.initconfig()
            except: 
                tkMessageBox.showerror("Configuration File", "Failed to read file \n'%s'"%filename)
                return
        
    def saveconfig(self): 
        filename = tkFileDialog.asksaveasfilename(filetypes = (("Configurations", "*.p2h"), ))
        if filename: 
            try: 
                filename = filename[: -4]
                temp = pdict(filename)
                for key in self.settings.keys(): 
                    temp[key] = self.settings[key].get()
                temp.save()
            except: 
                tkMessageBox.showerror("Configuration File", "Failed to save file \n'%s'"%filename)
                return
            
    def openfile(self): 
        filename = tkFileDialog.askopenfilename()
        if filename: 
            try: 
                text = file(filename, 'r').read()
            except: 
                tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'"%filename)
                return
            self.input.delete('1.0', Tkinter.END)
            self.input.see(Tkinter.END)
            self.input.insert('0.0', text)
            
    def savefile(self): 
        filename = tkFileDialog.asksaveasfilename()
        text = self.output.get('1.0', Tkinter.END)
        if filename: 
            try: 
                file(filename, 'w').write(text)
            except: 
                tkMessageBox.showerror("Save Output As", "Failed to write file \n'%s'"%filename)
            
    def showabout(self): 
        tkMessageBox.showinfo("About PY2HTML", """py2html version: %s\npy2htmlTk version: %s\nCopyright : %s 2004"""%
                              (py2html.__version__, __version__, __author__))

    def loadtemplate(self): 
        filename = tkFileDialog.askopenfilename()
        if filename: 
            try: 
                self.settings["template"].set(filename)
            except: 
                tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'"%filename)
                return

    def GUIconfig(self): 
        flist = glob.glob("*.style")
        win = Tkinter.Toplevel(self.root)
        win.title("PY2HTML Configuration")
        subframe = Tkinter.Frame(win, borderwidth = 1, relief = Tkinter.GROOVE)
        subframe.pack(expand = Tkinter.N, fill = Tkinter.X)
        Tkinter.Label(subframe, text = "Use this web-page template:").pack(pady = 5, side = Tkinter.LEFT, anchor = Tkinter.N)
        Tkinter.Entry(subframe, textvariable = self.settings["template"]).pack(pady = 5, fill = Tkinter.X, expand = Tkinter.Y, side = Tkinter.LEFT, anchor = Tkinter.N)
        Tkinter.Button(subframe, text = "View", command = self.viewtemplate, width = 10).pack(pady = 2, side = Tkinter.LEFT, anchor = Tkinter.N)
        Tkinter.Button(subframe, text = "Browse", command = self.loadtemplate, width = 10).pack(pady = 2, side = Tkinter.LEFT, anchor = Tkinter.N)
        subframe = Tkinter.Frame(win, borderwidth = 1, relief = Tkinter.GROOVE)
        subframe.pack(expand = Tkinter.N, fill = Tkinter.X)
        Tkinter.Label(subframe, text = "Use this style file:").pack(pady = 5, side = Tkinter.LEFT, anchor = Tkinter.N)
        eval('''Tkinter.OptionMenu(subframe,self.settings["stylefile"],"<default>",%s).pack(side=Tkinter.LEFT,fill=Tkinter.X,
                                                        expand=Tkinter.Y,anchor = Tkinter.N)'''%str(flist)[1: -1])
        Tkinter.Button(subframe, text = "View", command = self.viewstylefile, width = 10).pack(pady = 2, side = Tkinter.LEFT, anchor = Tkinter.N)
        subframe = Tkinter.Frame(win, borderwidth = 1, relief = Tkinter.GROOVE)
        subframe.pack(expand = Tkinter.N, fill = Tkinter.BOTH)
        Tkinter.Label(subframe, text = "How to modify layout:").pack(side = Tkinter.TOP, anchor = Tkinter.N, 
                                                                     fill = Tkinter.X, expand = Tkinter.N)
        eval('''Tkinter.OptionMenu(subframe,self.settings["formatstyle"],%s).pack(side = Tkinter.TOP,anchor=Tkinter.N,
                                                              fill = Tkinter.Y,expand = Tkinter.N)'''%str(self.format_options)[1: -1])
        Tkinter.Label(subframe, text = "Use entities for:").pack(side = Tkinter.TOP, anchor = Tkinter.N, 
                                                                     fill = Tkinter.X, expand = Tkinter.N)
        eval('''Tkinter.OptionMenu(subframe,self.settings["entities"],%s).pack(side = Tkinter.TOP,anchor=Tkinter.N,
                                                              fill = Tkinter.Y,expand = Tkinter.N)'''%str(self.entity_options)[1: -1])
        Tkinter.Checkbutton(subframe, text = 'Replace spaces and newlines', variable = self.settings["replace"], 
                            font = ('times', 8, 'normal')).pack(side = Tkinter.TOP, anchor = Tkinter.NW, 
                                                              fill = Tkinter.X, expand = Tkinter.N)
        Tkinter.Checkbutton(subframe, text = 'Preview in browser', variable = self.settings["browser"], 
                            font = ('times', 8, 'normal')).pack(side = Tkinter.TOP, anchor = Tkinter.NW, 
                                                              fill = Tkinter.X, expand = Tkinter.N)
        subframe = Tkinter.Frame(win, borderwidth = 0, relief = Tkinter.GROOVE)
        subframe.pack(expand = Tkinter.N, fill = Tkinter.X)
        Tkinter.Label(subframe, text = "On screen Source Colour,Background Colour, Font and Font Size").pack(side = Tkinter.LEFT)
        subframe = Tkinter.Frame(win, borderwidth = 0, relief = Tkinter.GROOVE)
        subframe.pack(expand = Tkinter.N, fill = Tkinter.X)
        Tkinter.Entry(subframe, textvariable = self.settings["pysrccol"]).pack(side = Tkinter.LEFT, anchor = Tkinter.N)
        Tkinter.Entry(subframe, textvariable = self.settings["pysrccolbk"]).pack(side = Tkinter.LEFT, anchor = Tkinter.N)
        Tkinter.Entry(subframe, textvariable = self.settings["pysrcfont"]).pack(side = Tkinter.LEFT, anchor = Tkinter.N)
        Tkinter.Entry(subframe, textvariable = self.settings["pysrcsize"], width = 2).pack(side = Tkinter.LEFT, anchor = Tkinter.N)
        subframe = Tkinter.Frame(win, borderwidth = 0, relief = Tkinter.GROOVE)
        subframe.pack(expand = Tkinter.N, fill = Tkinter.X)
        Tkinter.Label(subframe, text = "On screen Output Colour,Background Colour, Font and Font Size").pack(side = Tkinter.LEFT)
        subframe = Tkinter.Frame(win, borderwidth = 0, relief = Tkinter.GROOVE)
        subframe.pack(expand = Tkinter.N, fill = Tkinter.X)
        Tkinter.Entry(subframe, textvariable = self.settings["pyoutcol"]).pack(side = Tkinter.LEFT, anchor = Tkinter.N)
        Tkinter.Entry(subframe, textvariable = self.settings["pyoutcolbk"]).pack(side = Tkinter.LEFT, anchor = Tkinter.N)
        Tkinter.Entry(subframe, textvariable = self.settings["pyoutfont"]).pack(side = Tkinter.LEFT, anchor = Tkinter.N)
        Tkinter.Entry(subframe, textvariable = self.settings["pyoutsize"], width = 2).pack(side = Tkinter.LEFT, anchor = Tkinter.N)
        subframe = Tkinter.Frame(win, bg = 'blue', borderwidth = 4, relief = Tkinter.GROOVE)
        subframe.pack(expand = Tkinter.N, fill = Tkinter.X)
        Tkinter.Button(subframe, text = "OK", command = win.destroy, width = 10).pack(side = Tkinter.RIGHT, expand = Tkinter.N)
        Tkinter.Button(subframe, text = "Use as the default", 
                       command = self.setdefaultconfig, width = 20).pack(side = Tkinter.LEFT, expand = Tkinter.Y)
        
    def getpage(self): 
        page = self.settings["template"].get().strip()
        if not page or ("<" in page): 
            return py2html.py_page
        else: 
            try: 
                page = open(page, 'r').read()
            except: 
                return py2html.py_page
            else: 
                return page
        
    def makePage(self, html='', title="Python Code"): 
        from time import gmtime, strftime
        block = py2html.makeBlock(html)
        now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        try: 
            return self.getpage()%(title, title, block, "%s %s"%(__version__, now))
        except: 
            return self.getpage()%(bloc, )

    def ClearInput(self): 
        self.input.delete('1.0', Tkinter.END)
        self.input.see(Tkinter.END)
        
    def ToPage(self): 
        data = self._text2HTML()
        data = self.makePage(data)
        self._writeAndDisplay(data)

    def ToBlock(self): 
        data = self._text2HTML()
        data = py2html.makeBlock(data)
        self._writeAndDisplay(data)

    def copy(self): 
        if not self.output.tag_ranges(Tkinter.SEL): 
            self.output.tag_add(Tkinter.SEL, '1.0', Tkinter.END)
        text = self.output.get(Tkinter.SEL_FIRST, Tkinter.SEL_LAST)
        self.output.tag_remove(Tkinter.SEL, '1.0', Tkinter.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        
    def help(self): 
        self.output.delete('1.0', Tkinter.END)
        self.output.see(Tkinter.END)
        self.output.insert('0.0', __doc__)
        self.labeltext.set("How to Use this program:")
        
    def viewstylefile(self): 
        try: 
            name = self.settings["stylefile"].get()
            if name == "<default>": 
                text = "Py2html default style:\n"+str(py2html.py_style).replace("],", "\n")
            else: 
                text = file(name, "r").read()
        except: 
            self.root.bell()
            text = "There was an error reading the file!!"
        self.output.delete('1.0', Tkinter.END)
        self.output.see(Tkinter.END)
        self.output.insert('0.0', text)
        self.labeltext.set("Style File: %s"%(name, ))
    def viewtemplate(self): 
        try: 
            name = self.settings["template"].get().strip()
            if name == "<default>": 
                text = "Py2html default page template:\n"+py2html.py_page
            else: 
                text = file(name, "r").read()
        except: 
            self.root.bell()
            name = "There was an error reading the file!!"
        self.output.delete('1.0', Tkinter.END)
        self.output.see(Tkinter.END)
        self.output.insert('0.0', text)
        self.labeltext.set("Template: %s"%(name, ))
        
    def _text2HTML(self): 
        fname = r"py2html.tmp"
        text = self.input.get('1.0', Tkinter.END)
        if isinstance(text, unicode): 
            text = text.encode('iso-8859-1', 'ignore')
        f = open(fname, 'wb')
        f.write(text)
        f.close()
        style = self.settings["stylefile"].get()
        return py2html.file2HTML(fname, 
                                 str(self.format_options.index(self.settings["formatstyle"].get())), 
                                 py2html.readStyleFile(style), 
                                 self.settings['replace'].get(), 
                                 str(self.entity_options.index(self.settings["entities"].get())))
    
    def _writeAndDisplay(self, txt): 
        fname = r"py2html.tmp"
        open(fname+".html", 'w').write(txt)
        self.output.delete('1.0', Tkinter.END)
        self.output.see(Tkinter.END)
        self.output.insert('0.0', txt)
        self.labeltext.set("Output: %s"%(fname, ))
        if self.settings['browser'].get(): 
            import webbrowser
            webbrowser.open(fname+".html")
        




        
if __name__ == "__main__": 
    GUIconverter()

