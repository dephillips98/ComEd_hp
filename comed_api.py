import requests 

url = "https://hourlypricing.comed.com/api?type="
all_fmp = "5minutefeed"

def five_min():
 last_five = url + all_fmp
 req = requests.get(last_five)