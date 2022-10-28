import requests
import threading

url = "https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE4w"

letter = []

for i in range(ord("A"),ord("Z")+1):
    letter.append(chr(i))
for i in range(ord("a"),ord("z")+1):
    letter.append(chr(i))
for i in range(1,9):
    letter.append(str(i))

linkafter = []

for a in letter:
    for b in letter:
        for c in letter:
            linkafter.append(a+b+c)


def test_down(link, filename):
    filename = 'img/' + filename
    a = requests.get(link)
    if a.status_code == 200 and int(a.headers['X-Source-Length']) >= 300000 and int(a.headers['X-Source-Length']) <= 1000000 :
        with open(filename,"wb") as code:
            code.write(a.content)
            print('Download Succeed! Filename: ' + filename)

for i in linkafter:
    url = "https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE4w"
    url = url + i
    filename = 'RE4w' + i + ".jpg"
    t = threading.Thread(target=test_down,name="Thread"+i,args=(url,filename))
    t.start()