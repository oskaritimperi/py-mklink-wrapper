# py-mklink-wrapper

A wrapper script for `ln.exe` to make it look like the `MKLINK` utility
found from Windows Vista onwards. `ln.exe` allows Windows XP to use
symbolic links. More recent versions of Windows come with the MKLINK
utility which can do the same.

To fully utilise this, you should also have a batch script that
should look something like this:

```
@ECHO OFF
python %~dp0mklink.py %*
```

Name the file `mklink.cmd` and put it in `PATH`. Now you can use the
fake mklink utility like you would use the real.

You can find instruction for installing ln.exe from
[here](http://schinagl.priv.at/nt/hardlinkshellext/hardlinkshellext.html#symboliclinksforwindowsxp)
