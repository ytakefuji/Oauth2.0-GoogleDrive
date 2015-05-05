#delete-file function added for PyDrive

oauth2_delete.py for deleting a file on Google Drive through oauth2

You should install pydrive.

You should download your .json file from google developer console and rename it to client_secrets.json.

files.py for a new files.py of PyDrive which should be replaced with

Go to your pydrive folder
Download files.py file on pydrive folder
To compile files.py for generating files.pyc
use help.py

$ cat help.py 
import py_compile 
py_compile.compile("files.py")

$ chmod 755 files.py
$ python help.py
