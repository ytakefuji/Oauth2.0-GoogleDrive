from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload,MediaIoBaseDownload
import io,os

# Setup the Drive v3 API
SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
    creds = tools.run_flow(flow, store)
drive_service = build('drive', 'v3', http=creds.authorize(Http()))
rinput = vars(__builtins__).get('raw_input',input)
FILE=rinput('enter file name: ')
file_metadata = { 'name': FILE}
media = MediaFileUpload(FILE, resumable=True)
file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
os._exit(0)
