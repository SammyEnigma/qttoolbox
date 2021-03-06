# -*- python -*-

import os
import re

tools = [
    'prefixoptions',
    'qtcore',
    'qtprintsupport',
    'qtwidgets',
    'qtt_qtconfig'
]
# tools we need for the build here, but do not get passed as dependencies
# to those loading *this* tool
local_tools = ['qtt_common', 'doxygen']
env = Environment(tools = ['default'] + tools + local_tools)
env.AppendUnique(CPPFLAGS = ['-g', '-O0'])

# The directory where shared files (e.g., color tables) for QtBscan will be
# installed
bscanShareDir = env.subst(os.path.join(env['INSTALL_SHAREDIR'], 'qtt_qtbscan'))

# Create BscanShareDir.h, which holds a string with the path to installed 
# shared files for QtBscan.
f = open('BscanShareDir.h', 'w')
f.write('#include <string>\n')
f.write('// directory where shared files (e.g., color tables) are stored\n')
# Make sure we replace backslashes with slashes for ANSI C path syntax, which
# should work with C system calls under all OSes.
f.write('static const std::string BscanShareDir = "' + 
        bscanShareDir.replace('\\','/') + '";\n')
f.close()

# This will create the ui_*.h files
uifiles = Split("""
Bscan.ui
DisplayLimitDialog.ui
GateLimitDialog.ui
TimeSpanDialog.ui
""")
env.Uic(uifiles)

sources = Split("""
BscanMainWindow.cpp
BscanGraphicsScene.cpp
BscanGraphicsView.cpp
BscanRay.cpp
BscanWidget.cpp
ColorTable.cpp
DisplayLimitDialog.cpp
GateLimitDialog.cpp
RayGraphicsItem.cpp
TimeSpanDialog.cpp
""")

headers = Split("""
BscanGraphicsScene.h
BscanGraphicsView.h
BscanMainWindow.h
BscanRay.h
BscanWidget.h
ColorTable.h
DisplayLimitDialog.h
GateLimitDialog.h
RayGraphicsItem.h
TimeSpanDialog.h
""")

env['DOXYFILE_DICT'].update({ "PROJECT_NAME" : "Qttoolbox Bscan" })
html = env.Apidocs(sources + headers)

qtbscanlib = env.Library('qtbscan', sources)
Default(qtbscanlib)

# Build a list of all colortables/*.ct files
colortables = []
for file in os.listdir('colortables'):
    if (re.compile('.*\.ct').match(file)):
        colortables.append(os.path.join('colortables', file))

# Make install targets to put our color table files into
# INSTALL_DIR/share/bscan
ct_targets = []
for file in colortables:
    ct_targets += env.InstallShare('qtt_qtbscan', file)
Install(ct_targets)

# Finally, the tool section...
tooldir = env.Dir('.').srcnode().abspath    # this directory

def qtt_qtbscan(env):
    env.AppendUnique(CPPPATH = [tooldir])
    env.AppendLibrary('qtbscan')
    env.AppendDoxref('qttoolbox_QtBscan')
    env.Require(tools)

Export('qtt_qtbscan')
