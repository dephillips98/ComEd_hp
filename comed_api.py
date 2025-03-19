import requests 
import datetime
import pytz

url = "https://hourlypricing.comed.com/api?type="
all_fmp = "5minutefeed"
format = "&format=json"

def get_data():
    last_five = url + all_fmp + format
    req = requests.get(last_five)
    if req.status_code == 200:
        fm_data = req.json()
        price_list = []
        time_list = []
        for item in fm_data:
            time = item['millisUTC']
            price = item['price']
            price_list.append(price)
            time_list.append(time)
        return time_list, price_list
    else:
        print(f"Error: Received status code {req.status_code}")
        return None

def convert_time(time_list): 
    for time in time_list:
        seconds = int(time) / 1000
        utc_time = datetime.datetime.utcfromtimestamp(seconds)
        central_timezone = pytz.timezone('America/Chicago')
        central_time = utc_time.replace(tzinfo=pytz.utc).astimezone(central_timezone)
        formatted_time = central_time.strftime("%Y-%m-%d %I:%M:%S %p")
        return formatted_time




            
times, prices = get_data()
if __name__ == "__main__":
    convert_time(times)

#convert_time(get_data())

