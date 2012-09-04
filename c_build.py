from distutils.core import setup, Extension

module1 = Extension('extended-audioop',
#										extra_compile_args = ['-E'],
                    sources = ['extended-audioop.c'],
										define_macros = [('DEBUG',None)])

#module1 = Extension('audioop',
#                    sources = ['audioop.c'])

setup (name = 'extended-audioop',
       version = '0.5',
       description = 'Extended audiooop. Add Handling of 24Bit PCM.',
       ext_modules = [module1])
