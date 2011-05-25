from distutils.core import setup, Extension

#module1 = Extension('audioop',
#                    sources = ['audioop.c'],
#										define_macros = [('DEBUG',None)])

module1 = Extension('audioop',
                    sources = ['audioop.c'])

setup (name = 'audioop',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
