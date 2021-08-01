from setuptools import setup
setup(
   name='elliptec',
   version='1.1.3',
   description='TL-rotation-control',
   author='cdbaird',
   author_email='foomail@foo.com',
   packages=['elliptec'],  #same as name
   install_requires=['pyserial', 'pyqt5'], #external packages as dependencies
)
