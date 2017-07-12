tools = ['qt5', 'qwt', 'doxygen']
# tools we need for the build here, but do not get passed as dependencies
# to those loading *this* tool
local_tools = ['qtt_common']
env = Environment(tools = ['default'] + tools + local_tools)

qt5modules = ['QtCore', 'QtGui', 'QtDesigner']
env.EnableQt5Modules(qt5modules)

tooldir = env.Dir('.')

# uic knob form
env.Uic5('TwoKnobs.ui')

# build knob shared library
sources = Split("""
TwoKnobs.cpp
TwoKnobsPlugin.cpp
""")

headers = Split("""
TwoKnobs.h
TwoKnobsPlugin.h
""")

twoknobs = env.SharedLibrary('twoknobs', sources)

twoknobs_install = env.InstallLib(twoknobs)

Default(twoknobs)

env['DOXYFILE_DICT'].update({ "PROJECT_NAME" : "Qttoolbox Twoknobs" })
html = env.Apidocs(sources + headers)

def qtt_twoknobs(env):
    for t in tools:
        env.Tool(t)
    env.EnableQt5Modules(qt5modules)
    env.AppendUnique(CPPPATH = [tooldir])
    env.AppendUnique(LIBPATH = [tooldir])
    env.AppendUnique(RPATH=[tooldir])
    env.Append(LIBS = ['twoknobs'])
    
Export('qtt_twoknobs')


