import pandas as pd
import numpy as np
import requests
import json
from bs4 import BeautifulSoup


cookies = {
    'GERRIT_UI': 'GWT',
    'GerritAccount': 'aPwfprsGjZMWmdcbCRTZaBFPDsONXDCOTa',
    'XSRF_TOKEN': 'aPwfprqZ35BA4O03ll1NFBTVgKRtzb3jEq',
    's_fid': '5F0E81DF2D0EB682-298895AFBB2C5218',
    's_cc': 'true',
    '_ga': 'GA1.2.1812694275.1646083890',
    'jnpr_vID': '3jvDtZE5FJopZAnNoxiHPg1GmXDBwZ62-1646083923',
    'coveo_visitorId': '097a8475-8e4a-4129-9d1b-eb263314d6d9',
    'AMCVS_D206123F524450F50A490D45%40AdobeOrg': '1',
    'at_check': 'true',
    'notice_behavior': 'implied,us',
    '_fbp': 'fb.1.1648494560605.639686633',
    '_gcl_au': '1.1.1132139401.1648494561',
    '_rdt_uuid': '1648494561581.9e4e2977-455a-4491-a6b3-3e1cd39399c3',
    'notice_preferences': '2:',
    'notice_gdpr_prefs': '0,1,2:',
    'cmapi_gtm_bl': '',
    'cmapi_cookie_privacy': 'permit 1,2,3',
    'mcxSurveyQuarantine': 'ok',
    'AMCV_D206123F524450F50A490D45%40AdobeOrg': '-2121179033%7CMCIDTS%7C19090%7CMCMID%7C21653766912852117423306258609791714079%7CMCAAMLH-1649955096%7C9%7CMCAAMB-1649955096%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1649357496s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.3.0',
    'BE_CLA3': 'p_id%3DALAR6N6J6264R6AR888L4PP4AAAAAAAAAH%26bf%3D3f2741e16f0ee7becc1d67c4b4d4b8a6%26bn%3D1%26bv%3D3.44%26s_expire%3D1649436697081%26s_id%3DALAR6N6J6264RRNNA86L4PP4AAAAAAAAAH',
    '_clck': '1sk6p4j|1|f0f|0',
    'mbox': 'PC#0e3c3ca19f9740a4a229cdac3c0204db.34_0#1712080615|session#dd7772ddfb2d4f4d940e276fa3d07f76#1649352191',
    '_uetvid': '92a55040aeca11ecb721fd4f39646fd9',
    '_gid': 'GA1.2.72943856.1649350556',
    's_sq': '%5B%5BB%5D%5D',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'Accept': 'application/json',
    'X-Gerrit-Auth': 'aPwfprqZ35BA4O03ll1NFBTVgKRtzb3jEq',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://svl-evogit-01.juniper.net/',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'GERRIT_UI=GWT; GerritAccount=aPwfprsGjZMWmdcbCRTZaBFPDsONXDCOTa; XSRF_TOKEN=aPwfprqZ35BA4O03ll1NFBTVgKRtzb3jEq; s_fid=5F0E81DF2D0EB682-298895AFBB2C5218; s_cc=true; _ga=GA1.2.1812694275.1646083890; jnpr_vID=3jvDtZE5FJopZAnNoxiHPg1GmXDBwZ62-1646083923; coveo_visitorId=097a8475-8e4a-4129-9d1b-eb263314d6d9; AMCVS_D206123F524450F50A490D45%40AdobeOrg=1; at_check=true; notice_behavior=implied,us; _fbp=fb.1.1648494560605.639686633; _gcl_au=1.1.1132139401.1648494561; _rdt_uuid=1648494561581.9e4e2977-455a-4491-a6b3-3e1cd39399c3; notice_preferences=2:; notice_gdpr_prefs=0,1,2:; cmapi_gtm_bl=; cmapi_cookie_privacy=permit 1,2,3; mcxSurveyQuarantine=ok; AMCV_D206123F524450F50A490D45%40AdobeOrg=-2121179033%7CMCIDTS%7C19090%7CMCMID%7C21653766912852117423306258609791714079%7CMCAAMLH-1649955096%7C9%7CMCAAMB-1649955096%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1649357496s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.3.0; BE_CLA3=p_id%3DALAR6N6J6264R6AR888L4PP4AAAAAAAAAH%26bf%3D3f2741e16f0ee7becc1d67c4b4d4b8a6%26bn%3D1%26bv%3D3.44%26s_expire%3D1649436697081%26s_id%3DALAR6N6J6264RRNNA86L4PP4AAAAAAAAAH; _clck=1sk6p4j|1|f0f|0; mbox=PC#0e3c3ca19f9740a4a229cdac3c0204db.34_0#1712080615|session#dd7772ddfb2d4f4d940e276fa3d07f76#1649352191; _uetvid=92a55040aeca11ecb721fd4f39646fd9; _gid=GA1.2.72943856.1649350556; s_sq=%5B%5BB%5D%5D',
}

#website = 'https://svl-evogit-01.juniper.net/changes/?q=status:merged+AND+owner:"Vivek+Dua+<vivekdua@juniper.net>"&n=25&O=81'
#website = 'https://svl-evogit-01.juniper.net/q/status:merged+AND+owner:"Vivek+Dua+<vivekdua@juniper.net>"&n=25&O=81'
website='https://svl-evogit-01.juniper.net/#/c/forwarding/exprplus/+/590379/'



class gerrit():

    def __init__(self):
        self.owner = 'vivekdua'
        self.numCommits = 100
        # Start the session
        self.session = requests.Session()
        # Create the payload
        payload = {'_username': 'vivekdua',
                   '_password': 'Juniper@2021'
                   }
        # Post the payload to the site to log in
        s = self.session.post("https://svl-evogit-01.juniper.net/login/%2F", data=payload)
        # Navigate to the next page and scrape the data
        s = self.session.get('https://svl-evogit-01.juniper.net/#/dashboard/self')

    def getGtestFiles(self, number):
        url = 'https://svl-evogit-01.juniper.net/{}'.format(number)
        response = self.session.get(url, verify=False, timeout=5)
        website_url = response.text
        soup = BeautifulSoup(website_url, 'lxml')
        my_body = soup.find('body')
        content_list = json.loads(my_body.find('p').contents[0].split('\n')[1])
        df = pd.DataFrame(content_list)

    def getCsetList(self):
        csetList = []
        response = self.session.get(website, verify=False, timeout=5)
        website_url = response.text
        soup = BeautifulSoup(website_url, 'lxml')
        my_body = soup.find('body')
        content_list = json.loads(my_body.find('p').contents[0].split('\n')[1])
        df = pd.DataFrame(content_list)
        print("Size before validation:", df.size)
        df = df[df['project'] != 'csets/evo-csets']
        print("Size after validation:", df.size)
        for row in df.rows():
            csetList.append(row['_number'])
        for cset in csetList:
            print("number of gtest files is:{}".format(self.getGtestFiles(cset)))





#website='https://svl-evogit-01.juniper.net/#/q/status:merged+AND+owner:%22Vivek+Dua+%253Cvivekdua%2540juniper.net%253E%22'
#response = requests.get(website, headers=headers, cookies=cookies)
#website_url=response.text
#soup = BeautifulSoup(website_url, 'lxml')

gr = gerrit()
gr.getCsetList()


"""""""""
Let us understand briefly, what does these terms mean —
<tbody> : It specifies the table on the web page.
<tr> : It points to the specific row in this table.
<td> : It points to the particular cell in this row.

"""""""""""

#table1 = soup.find('table', class="changeTable")



## Remove all entries with 'project' of 'csets/evo-csets'
## Get all the href of the entries in a separate list


#my_table = my_body.find('tbody')
#my_table = my_body.find('table', class="changeTable")

#table_data = []
#for row in my_table.findAll('tr'):
#    row_data = []
#    for cell in row.findAll('td'):
#        row_data.append(cell.text)
#    if(len(row_data) > 0):
#        data_item = {"Hidden0": row_data[0],
#                     "Hidden1": row_data[1],
#                     "Hidden2": row_data[2],
#                     "Subject": row_data[3],
#                     "Status": row_data[4],
#                     "Owner": row_data[5],
#                     "Hidden3": row_data[6],
#                     "Project": row_data[7],
#                     "Branch": row_data[8],
#                     "Updated": row_data[9],
#                     "Size": row_data[10],
#                     "Code-Review": row_data[11],
#                     "Cset-Ready": row_data[12],
#                     "NACR": row_data[13],
#                     "Verified": row_data[14],
#        }
 #       table_data.append(data_item)
#""""""""""""""""""""

## df = pd.DataFrame(table_data)
