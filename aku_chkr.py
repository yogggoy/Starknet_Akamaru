import requests

url = "https://akamaruapi.uk/getAmount?adrs="

def main():
    with open('wallets.txt', 'r') as file:
        addresses = file.read().splitlines()

    for address in addresses:
        response = requests.get(url+address)
        print(f"{address} {response.text}")

if __name__ == "__main__":
    main()
