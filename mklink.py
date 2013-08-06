"""
A wrapper script for ln.exe to make it look like the MKLINK utility
found from Windows Vista onwards. To fully utilise this, you should
also have a batch script that should look something like this:

    @ECHO OFF
    python %~dp0mklink.py %*

Name the file "mklink.cmd" and put it in PATH. Now you can use the
fake mklink utility like you would use the real.

You can find instruction for installing ln.exe from

    http://schinagl.priv.at/nt/hardlinkshellext/hardlinkshellext.html#symboliclinksforwindowsxp

"""
import argparse
import subprocess
import sys

def MyFormatter(raw):
    """Make the help output look a little bit more like the real deal
    (i.e., this omits the "usage: " part in the beginning of the help).

    """
    class MyFormatter_(argparse.HelpFormatter):
        def format_help(self):
            return raw
    return MyFormatter_

usage_str = """Creates a symbolic link.

MKLINK [[/D] | [/H] | [/J]] Link Target

        /D      Creates a directory symbolic link.  Default is a file
                symbolic link.
        /H      Creates a hard link instead of a symbolic link.
        /J      Creates a Directory Junction.
        Link    specifies the new symbolic link name.
        Target  specifies the path (relative or absolute) that the new link
                refers to.

"""

parser = argparse.ArgumentParser(prog='MKLINK', prefix_chars='/',
    usage=usage_str, add_help=False,
    formatter_class=MyFormatter(raw=usage_str))
parser.add_argument('/?', dest='help', action='help')
group = parser.add_mutually_exclusive_group()
group.add_argument('/D', dest='symlink', default=False, action='store_true')
group.add_argument('/d', dest='symlink', default=False, action='store_true')
group.add_argument('/H', dest='hardlink', default=False, action='store_true')
group.add_argument('/h', dest='hardlink', default=False, action='store_true')
group.add_argument('/J', dest='junction', default=False, action='store_true')
group.add_argument('/j', dest='junction', default=False, action='store_true')
parser.add_argument('link')
parser.add_argument('target')

args = parser.parse_args()

if (not args.symlink) and (not args.hardlink) and (not args.junction):
    args.symlink = True

if args.symlink:
    sys.exit(subprocess.call(['ln.exe', '-s', args.target, args.link]))
elif args.hardlink:
    sys.exit(subprocess.call(['ln.exe', args.target, args.link]))
elif args.junction:
    sys.exit(subprocess.call(['ln.exe', '-j', args.target, args.link]))
else:
    print("invalid options!")
    sys.exit(1)
