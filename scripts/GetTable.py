"""
Short Python script to download StatCan data tables using the Web Data Service. 
Last modified by Joseph Kuchar, Feb 11, 2020
"""

import requests

#helper function to clean the product id a bit (remove hyphens, cut trailing characters)
def PID_Cleaner(s):
    if type(s)==int:
        s=str(s)
    s=s.replace('-','')
    if len(s)==10:
        s=s[0:8]
    return s

def getFullTable(pid,path=''):
    
    pid = PID_Cleaner(pid)
    print('cleaning pid {}'.format(pid))
    url='https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/{}/en'.format(pid)
    
    R=requests.get(url, proxies=credentials.proxy)
    response=R.json()
    if response['status']!='SUCCESS':
        raise ValueError('Failed to retrieve valid response')
    url2=response['object']
    
    T=requests.get(url2, proxies=credentials.proxy)
    if path !='' and ~path.endswith('/'):
        path+='/'
    
    g=open(path+pid+'.zip','wb') 
    g.write(T.content)
    g.close()

#S=2510005501

#getFullTable(S)
