# -*- coding: utf-8 -*-
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
for f in file_list:
  #print 'title: %s, id: %s mime: %s' % (f['title'], f['id'],f['mimeType'])
 print(f['title'].encode('utf-8'))
gauth.SaveCredentialsFile("mycreds.txt")
os._exit(0)
