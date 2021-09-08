from distutils.core import setup
import py2exe

options = {"py2exe": {"excludes": ["arcpy"]}}
setup(console=['Test.py'], options=options)
