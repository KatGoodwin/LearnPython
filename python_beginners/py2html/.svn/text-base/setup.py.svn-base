from distutils.core import setup
import py2html
doc = py2html.__doc__
sum = doc.split("\n")
classifiers = """\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: Freely Distributable
Programming Language :: Python
Topic :: Text Processing :: Markup :: HTML
Topic :: Software Development :: Documentation
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: Microsoft :: Windows
Operating System :: Unix
"""

setup(name="py2html",
      version = py2html.__version__,
      maintainer = "Paul Hardwick",
      maintainer_email = "paul@peck.org.uk",
      url = "http://www.peck.org.uk/p/python",
      platforms = ["any"],
      description = sum[0],
      classifiers = filter(None, classifiers.split("\n")),
      long_description = doc,
      license = "GNU GPL",
      py_modules = ["py2html",]
      )
      
      
      
      
