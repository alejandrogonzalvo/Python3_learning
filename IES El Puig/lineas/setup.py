from distutils.core import setup 
import py2exe 
 
setup(
    name="lineas", 
    version="1.0", 
    description="represenador de equaciones en 2d", 
    author="Alejandro Gonzalvo", 
    author_email="alejandrogonhid@gmail.com", 
    url="", 
    license="", 
    scripts=["main.py"], 
    console=["main.py"], 
    options={"py2exe": {"bundle_files": 1}}, 
    zipfile=None
)