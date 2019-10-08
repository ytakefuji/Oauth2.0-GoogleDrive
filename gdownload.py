from apiclient.http import MediaIoBaseDownload
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import io,os

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

def download_file(filename,file_id):
    #request = DRIVE.files().get(fileId=file_id)
    request = DRIVE.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request,chunksize=-1)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    fh.seek(0)
    f=open(filename,'wb')
    f.write(fh.read())
    f.close()

rinput = vars(__builtins__).get('raw_input',input)
fname=rinput('enter file name: ')
for f in files:
 if f['title'].encode('utf-8')==fname:
  print('downloading...',f['title'])
  download_file(f['title'],f['id'])
os._exit(0)
