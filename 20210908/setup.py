from distutils.core import setup
import py2exe

options = {"py2exe": {"excludes": ["arcpy"]}}
setup(windows=['Test.py'], options=options)
