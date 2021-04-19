import requests

def main():
    api_key = 'cacd7a9b996f7e83173be774c44501ac'
    r = requests.get(f'http://api.ipstack.com/check?access_key={api_key}')

    response = r.text
    response = response.split(",")

    city = None
    country = ""
    for item in response:
        splitted = item.split(":")
        if 'city' in splitted[0]:
            city = splitted[1].strip('""}}')
        elif 'country_name' in splitted[0]:
            country = splitted[1].strip('""}}')

    print(f"You are in {city}, {country}.")

if __name__ == "__main__":
    main()
