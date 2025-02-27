from dotenv import load_dotenv
from pprint import pprint 
import requests 
import os 



load_dotenv()

def get_odds(group):
    api_key = os.getenv("API_KEY")
    sport = "upcoming"
    regions = "us"
    markets = "h2h"
    url = f"https://api.the-odds-api.com/v4/sports/{sport}/odds/?apiKey={api_key}&regions={regions}&markets={markets}"

    odds_data = requests.get(url).json()

    return odds_data

if __name__ == "__main__":
    print('\n*** ODDS ***\n')

    group = input("\nPlease enter a sport (ex Soccer): ")

    odds_data = get_odds(group)

    print("\n")
    pprint(odds_data)