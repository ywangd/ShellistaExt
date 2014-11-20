'''Open a file in the Pythonista text editor, or vi
if not on iPad
'''

HAS_EDITOR = False

import os
try:
    import editor
    HAS_EDITOR = True
    import console
except:
    pass

from ... tools.toolbox import bash

def main(self, line):
    args = bash(line)

    if len(args) == 1:
        if HAS_EDITOR:
            f = os.path.join(os.getcwd(), args[0])
            print 'Opening %s' % f
            editor.open_file(f)
            console.hide_output()
        else:
            import platform
            if platform.system() == 'Linux':
                os.system('vi {0}'.format(args[0]))
            else:
                print 'Unsupported platform'
    else:
        print 'Usage: editor <filename>'
