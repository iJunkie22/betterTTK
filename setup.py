from distutils.core import setup


setup(name='betterTTK',
      version='1.0',
      author='Ethan Randall',
      author_email='iJunkie22@gmail.com',
      url='https://github.com/iJunkie22/betterTTK',
      packages=['betterTTK'],
      package_dir={'betterTTK': 'betterTTK'},
      install_requires=['Tkinter', 'ttk']
      )