import requests,json,math,csv,datetime,os,sys

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

hostname = "https://10.150.236.156:3780"
url = str(hostname)+"/data/user/login"

payload = "nexposeccusername=cyberapi&nexposeccpassword=DF489DsA12fdLS09!"
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'X-Requested-With': 'XMLHttpRequest',
  'Origin': str(hostname),
  'Connection': 'keep-alive',
  'Referer': str(hostname)+'/login.jsp',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
nexposeCCSessionID = json.loads(response.text).get("sessionID")
#print(response.text)

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'nexposeCCSessionID': nexposeCCSessionID,
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'Accept': '*/*',
    'Origin': str(hostname),
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': str(hostname)+'/vulnerability/listing.jsp',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'nexposeCCSessionID='+nexposeCCSessionID+'; time-zone-offset=240; i18next=en'
    }

def get_report_details(length,displaystart):

  url = str(hostname)+"/data/report/configs?sEcho=4&iColumns=4&sColumns=id%2C%2C%2C&iDisplayStart="+str(displaystart)+"&iDisplayLength="+str(length)+"&mDataProp_0=id.configID&mDataProp_1=&mDataProp_2=name&mDataProp_3=mostRecentReportSummary&sSearch=&bRegex=false&sSearch_0=&bRegex_0=false&bSearchable_0=true&sSearch_1=&bRegex_1=false&bSearchable_1=true&sSearch_2=&bRegex_2=false&bSearchable_2=true&sSearch_3=&bRegex_3=false&bSearchable_3=true&iSortCol_0=3&sSortDir_0=desc&iSortingCols=1&bSortable_0=false&bSortable_1=false&bSortable_2=true&bSortable_3=true&sort=mostRecentReport"

  payload={}

  response = requests.request("GET", url, headers=headers, data=payload, verify=False)

  temp = json.loads(response.text)

  return temp

def get_report_total():
  length = 5
  displaystart = 0

  url = str(hostname)+"/data/report/configs?sEcho=4&iColumns=4&sColumns=id%2C%2C%2C&iDisplayStart="+str(displaystart)+"&iDisplayLength="+str(length)+"&mDataProp_0=id.configID&mDataProp_1=&mDataProp_2=name&mDataProp_3=mostRecentReportSummary&sSearch=&bRegex=false&sSearch_0=&bRegex_0=false&bSearchable_0=true&sSearch_1=&bRegex_1=false&bSearchable_1=true&sSearch_2=&bRegex_2=false&bSearchable_2=true&sSearch_3=&bRegex_3=false&bSearchable_3=true&iSortCol_0=3&sSortDir_0=desc&iSortingCols=1&bSortable_0=false&bSortable_1=false&bSortable_2=true&bSortable_3=true&sort=mostRecentReport"

  payload={}

  response = requests.request("GET", url, headers=headers, data=payload, verify=False)

  temp = json.loads(response.text)
  total = temp.get("iTotalDisplayRecords")
  return(total)

def start_report(num):
  url = str(hostname)+"/data/report/configs/"+str(num)+"/reports"

  payload={}

  response = requests.request("POST", url, headers=headers, data=payload, verify=False)
  #return report ID
  print(response.text)

def get_latest_scans(num):
  url = str(hostname)+"/data/scan/site/"+str(num)

  payload = "sort=startTime&dir=DESC&startIndex=0&results=10&table-id=site-completed-scans"

  response = requests.request("GET", url, headers=headers, data=payload, verify=False)
  temp = json.loads(response.text)
  return(temp)


def scan_to_site(num):
  url = str(hostname)+"/data/site/id/scan/"+str(num)
  payload={}
  response = requests.request("GET", url, headers=headers, data=payload, verify=False)
  return(str(response.text))


def get_report_config(num):
  headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json; charset=UTF-8',
  'Cookie': 'nexposeCCSessionID='+str(nexposeCCSessionID)+'; time-zone-offset=240; i18next=en',
  'Origin': str(hostname),
  'Referer': str(hostname)+'/report/reports.jsp',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'nexposeCCSessionID': str(nexposeCCSessionID),
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
  }

  url = str(hostname)+"/data/report/configs/"+str(num)
 
  response = requests.request("GET", url, headers=headers, verify=False)
  temp = json.loads(response.text)
  return(temp)


def download_report(name,link):
  url = str(hostname)+str(link)

  headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'Cookie': 'nexposeCCSessionID='+str(nexposeCCSessionID)+'; time-zone-offset=240; i18next=en',
    'Origin': str(hostname),
    'Referer': str(hostname)+'/report/reports.jsp',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'nexposeCCSessionID': str(nexposeCCSessionID),
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
  }
  response = requests.request("GET", url, headers=headers,  verify=False)
  ext = str(link).split(".")

  path = os.getcwd()+"/output/"
  if not os.path.isdir(path):
      os.mkdir(path)
  else:
      pass
  #print(response.text)
  f = open(str(path)+str(name)+"."+str(ext[1]), "wb")
  f.write(response.content)
  f.close()

def generate():
  show = 500
  total = int(get_report_total())
  pages = math.ceil(total/show)
  #print(pages)

  for i in range(pages):
    temp = get_report_details(show,show*i).get('records')
    for i in temp:
      #print(i)
      try:
        name = i.get('name')
      except:
        name = 0

      try:
        configid = i.get('id').get('configID')
      except:
        configid = 0

      try:
        status = i.get('mostRecentReportSummary').get('reportStatus')
      except:
        status = 0

      try:
        generatedon = i.get('mostRecentReportSummary').get('generatedOn')
      except:
        generatedOn = 0

      try:
        covert_to = str(datetime.datetime.fromtimestamp(int(generatedon)/1000)).split(" ")
      except:
        covert_to = 0
      
      try:
        reportfile = i.get('mostRecentReportSummary').get('reportFile')
      except:
        reportfile = 0
      #print('"%s","%s","%s","%s","%s"' % (name,configid,status,covert_to[0],reportfile))
      f = open("reports.csv","a")
      f.write('"%s","%s","%s","%s","%s"\n' % (name,configid,status,covert_to[0],reportfile))
      f.close()

def scanid_to_latest(num):
  search_site = scan_to_site(num)
  #print(search_site)
  temp = (get_latest_scans(search_site).get('records'))
  #print(temp)

  box = []
  for i in temp:
    liveHosts = i.get('liveHosts')
    box.append(liveHosts)
  total = sum(box)
  length = len(box)
  avg = int(total/length/2)

  latest_scanID = 0

  for i in temp:
    #endtime = i.get('endTime')
    scanID = i.get('scanID')
    liveHosts = i.get('liveHosts')
    
    if int(liveHosts) < int(avg):
      pass
    else:
      #print(endtime,scanID,liveHosts)
      latest_scanID = scanID
      break

  return latest_scanID


def save_report_config(report_num):
  url = str(hostname)+"/data/report/configs/"+str(report_num)
  
  load = get_report_config(report_num)
  #print(load)
  try:
    load['scans'] = [int(scanid_to_latest(load['scans'][0]))]
  except:
    pass
  new_payload = {"name":load['name'],"id":load['id'],"owner":load['owner'],"reportFrequency":load['reportFrequency'],"reportTemplateID":load['reportTemplateID'],"exporterConfig":load['exporterConfig'],"storeOnServer":load['storeOnServer'],"storeCopyOnServer":load['storeCopyOnServer'],"baseline":load['baseline'],"timezone":load['timezone'],"assetGroups":load['assetGroups'],"sites":load['sites'],"assets":load['assets'],"tags":load['tags'],"scans":load['scans'],"filters":load['filters'],"users":load['users'],"globalSMTPDistribution":load['globalSMTPDistribution'],"recipients":load['recipients'],"language":load['language'],"parameters":load['parameters'],"riskTrendProperties":load['riskTrendProperties']}
  #print(new_payload)
  payload = json.dumps(new_payload)
  headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'Cookie': 'nexposeCCSessionID='+str(nexposeCCSessionID)+'; time-zone-offset=240; i18next=en',
    'Origin': str(hostname),
    'Referer': str(hostname)+'/report/reports.jsp',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'nexposeCCSessionID': str(nexposeCCSessionID),
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
  }
  response = requests.request("PUT", url, headers=headers, data=payload, verify=False)
  print(response.text,load['name'])


def start_one(num):
  save_report_config(num)
  start_report(num)

def start_all():
  box = []
  with open('start.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for i in csv_reader:
      if i[1] is not '':
        box.append(i[1])
  #print(box)
  for i in box:
    start_one(i)

def download_all():
  box = []
  with open('download.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for i in csv_reader:
      if i[4] is not '':
        box.append([i[0],i[4]])
  #print(box)
  for i in box:
    download_report(i[0],i[1])


#generate()
#start_all()
#download_all()

try:
  if sys.argv[1] == "generate":
    try:
      os.remove("reports.csv")
    except:
      pass
    generate()
    print("Generated")

  if sys.argv[1] == "download":
    download_all()
    print("Downloaded")

  if sys.argv[1] == "start":
    start_all()
    print("Started")
except:
  print("Try these")
  print("python a.py generate")
  print("python a.py start")
  print("python a.py download")

#Need to create start.csv after pulling data from reports.csv
#Once reports are done generating, run python a.py generate once more and then do the download 

