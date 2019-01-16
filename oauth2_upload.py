from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
file=drive.CreateFile()
name=raw_input('file name? ')
file.SetContentFile(name)
file.Upload()
gauth.SaveCredentialsFile("mycreds.txt")
os._exit(0)
