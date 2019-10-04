from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

CLIENT_SECRET = 'client_secrets.json'
SCOPES = ['https://www.googleapis.com/auth/drive.readonly.metadata']

store = file.Storage('storage.json')
#creds = None  use for the first time
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
    flags = tools.argparser.parse_args(args=[])
    creds = tools.run_flow(flow, store, flags)
DRIVE = build('drive', 'v2', http=creds.authorize(Http()))

files = DRIVE.files().list().execute().get('items', [])
for f in files:
 print(f['title'].encode('utf-8'),f['id'].encode('utf-8'))
