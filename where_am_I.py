import requests


def main():
    api_key = 'cacd7a9b996f7e83173be774c44501ac'
    r = requests.get(f'http://api.ipstack.com/check?access_key={api_key}')

    response = r.json()

    city = response.get('city')
    country = response.get('country_name')
    ip = response.get('ip')

    print(f"You are in {city}, {country}.")
    print(f"Your IP: {ip}")


if __name__ == "__main__":
    main()
