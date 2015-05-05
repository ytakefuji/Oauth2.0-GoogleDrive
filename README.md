# delete-file function added for PyDrive
oauth2_delete.py for delete a file on Google Drive through oauth2
files.py for a new files.py of PyDrive which should be replaced with
Go to your pydrive folder
Download files.py file on pydrive folder
To compile files.py for generating files.pyc
use help.py
$ cat help.py 
import py_compile 
$ chmod 755 files.py
py_compile.compile("files.py")
$ python help.py
