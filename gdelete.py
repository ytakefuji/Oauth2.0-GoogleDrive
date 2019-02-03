from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os

CLIENT_SECRET = 'client_secrets.json'
SCOPES = ['https://www.googleapis.com/auth/admin.datatransfer','https://www.googleapis.com/auth/drive.appfolder','https://www.googleapis.com/auth/drive']

store = file.Storage('tokenWrite.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
    flags = tools.argparser.parse_args(args=[])
    creds = tools.run_flow(flow, store, flags)
DRIVE = build('drive', 'v2', http=creds.authorize(Http()))
files = DRIVE.files().list().execute().get('items', [])

rinput = vars(__builtins__).get('raw_input',input)
fname=rinput('enter file name: ')
for f in files:
 if f['title']==fname:
  DRIVE.files().delete(fileId=f['id']).execute()
  break
 else:
  print(fname," is not found")
  break
os._exit(0)
