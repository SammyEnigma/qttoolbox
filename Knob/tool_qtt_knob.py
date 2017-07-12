tools = ['qwt', 'qt5', 'doxygen']
# tools we need for the build here, but do not get passed as dependencies
# to those loading *this* tool
local_tools = ['default', 'qtt_common', 'doxygen']
env = Environment(tools = local_tools + tools)

qt5modules = ['QtCore', 'QtGui', 'QtOpenGL', 'QtXml', 'QtDesigner']
env.EnableQt5Modules(qt5modules)

tooldir = env.Dir('.').srcnode().abspath

# uic knob form
env.Uic5('Knob.ui')

# build knob shared library
sources = Split("""
Knob.cpp
KnobPlugin.cpp
""")

headers = Split("""
Knob.h
KnobPlugin.h
""")

knob = env.SharedLibrary('knob', sources)
knob_install = env.InstallLib(knob)

Default(knob)

env['DOXYFILE_DICT'].update({ "PROJECT_NAME" : "Qttoolbox Knob" })
html = env.Apidocs(sources + headers)


# Actually define and export the qtt_knob tool
def qtt_knob(env):
    for t in tools:
        env.Tool(t)
    env.EnableQt5Modules(qt5modules)
    env.AppendUnique(CPPPATH = [tooldir])
    env.AppendUnique(LIBPATH = [tooldir])
    env.AppendUnique(RPATH=[tooldir])
    env.Append(LIBS = ['knob'])
    
Export('qtt_knob')

