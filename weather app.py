import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_weather():
    print("--- Real-Time Live Weather App --- \n")
    city = input("City ka naam dalo (e.g., Jaipur, Delhi, Mandawar, Dausa, Hindon, All Rajasthan, All India): ").strip()
    
    # 🔴 YAHAN APNI NAYI COPY KI HUI API KEY PASTE KAREIN
    api_key = "a6caaca0ed50973eed960bb84b0480eb" 
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url, verify=False)
        
        if response.status_code == 401:
            print("\nError: API Key abhi active nahi hui hai ya galat hai! (Bane ke baad 15-20 min lagte hain active hone mein)")
            return
            
        data = response.json()
        
        if data.get("cod") == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            desc = data["weather"][0]["description"]
            country = data["sys"]["country"]
            
            print(f"\n====== Weather in {city.capitalize()}, {country} ======")
            print(f"Temperature : {temp}°C")
            print(f"Condition   : {desc.capitalize()}")
            print(f"Humidity    : {humidity}%")
            print("========================================")
        else:
            print(f"\nError: {data.get('message', 'City nahi mili!')}")
            
    except requests.ConnectionError:
        print("\nNetwork Error: Internet connection check karein!")
    except Exception as e:
        print(f"\nKuch gadbad hui: {e}")

# Run karein
get_weather()