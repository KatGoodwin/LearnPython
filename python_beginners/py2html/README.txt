py2html is intended as a small but useful command line utility
to webify your code.
 
	c:\python23\python py2html.py -h
or 
(within IDLE)
	import py2html
	help(py2html)

will list the details.

py2htmlTk.pyw is a GUI front end to py2html that is for cutting and pasting code
fragments into web-pages. 

py2html.style and other style files are examples of tag substitution.
They can be passed as command line options to change the look of the code.
Copy these files and edit as you need. 

"setup.py install" will only copy py2html.py to your site library directory.
The GUI app can be anywhere on execution path. The style files need 
to be in the current working directory to be found by the GUI.

A very simple example:
c:\python23\python py2html.py -i py2html.py
the default file py2html.html is produced showing the py2html code:)

An example that replaces the default format with a new style and forces substitution
of spaces and line feeds and outputs to a specified file:

c:\python23\python py2html.py -i py2html.py -s py2html_div.style -R -o my_webpage.htm


Comments and suggestions: paul@peck.org.uk