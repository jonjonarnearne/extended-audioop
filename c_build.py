from distutils.core import setup, Extension

module1 = Extension('extended_audioop',
#										extra_compile_args = ['-E'],
                    sources = ['extended_audioop.c']
#										define_macros = [('DEBUG',None)]
										)

#module1 = Extension('audioop',
#                    sources = ['audioop.c'])

setup (name = 'extended_audioop',
       version = '0.5',
       description = 'Extended audiooop. Add Handling of 24Bit PCM.',
       ext_modules = [module1])
