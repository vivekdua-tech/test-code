''' Old, true, and sordid tale of Python
    featuring raisins, pushy relatives,
    business cards, web pages, checkboards and
    getting must needed rest api.
'''

from urllib.request import urlopen
from urllib.parse import urlencode

def make_vcard(fname, lname, title, phone, email):
    'Create an electronic business card in a VCard 2.1 format'
    return vcard_template.format(fname=fname, lname=lname, title=title,
                                 phone=phone, email=email)

vcard_template = '''\
BEGIN:VCARD
VERSION:2.1
N:{lname};{fname}
FN:{fname} {lname}
ORG:Raisins R Us, Inc.
TITLE:{title}
TEL;WORK;VOICE:{phone}
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:{email}
REV:20190214T195243Z
END:VCARD
'''

html_template = '''\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> {fname} {lname} </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> {fname} {lname} </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> {fname} {lname}  </dd>
    <dt> Job title  </dt>  <dd> {title} </dd>
    <dt> Work phone  </dt>  <dd> {phone}  </dd>
</dl>
</body>
</html>
'''

with open('notes/raisin_team.csv') as f:
    for line in f:
        line = line.rstrip()
        lname, fname, title, email, phone = line.split(',')
        basename = email.replace('@', '_at_').replace('.', '_dot_')
        
        vcard = make_vcard(fname, lname, title, phone, email)
        filename = f'{basename}.vcf'
        with open(filename, 'w') as vcard_file:
            vcard_file.write(vcard)
        print(f'Wrote: {filename!r}')

        # https://validator.w3.org/nu/#textarea
        html = html_template.format(fname=fname, lname=lname, title=title,
                                    phone=phone, email=email)
        filename = f'{basename}.html'
        with open(filename, 'w') as html_file:
            html_file.write(html)
        print(f'Wrote: {filename!r}')

        # QR from the Google Chart REST API documented at:
        # https://developers.google.com/chart/infographics/docs/qr_codes

        root_url = 'https://chart.googleapis.com/chart?'
        query = dict(cht='qr', chs='300x300', chl=vcard)
        url = root_url + urlencode(query)
        with urlopen(url) as u:
            image = u.read()

        filename = f'{basename}.png'
        with open(filename, 'wb') as image_file:
            image_file.write(image)
        print(f'Wrote: {filename!r}')
