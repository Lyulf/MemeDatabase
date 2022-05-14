from SCons.Environment import Environment
import os
path = [R'C:\cygwin64\bin']
env = Environment(platform='cygwin', ENV={'PATH' : path})
env.Program('main.cpp')