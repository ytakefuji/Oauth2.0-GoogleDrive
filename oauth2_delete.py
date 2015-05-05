from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os,re
gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()
gauth.SaveCredentialsFile("mycreds.txt")
file=drive.CreateFile()
name=raw_input('file name? ')
file['title']=name
file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
for i in file_list:
  m=re.search(name,i['title'])
  if m:
   id=i['id']
file.DeleteFile(id)
os._exit(0)
