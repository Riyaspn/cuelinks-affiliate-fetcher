import requests

API_KEY = "YOUR_CUELINKS_API_KEY"

def fetch_campaigns():
    url = "https://api.cuelinks.com/v2/campaigns"
    headers = {"Authorization": f"Token token={API_KEY}"}
    params = {"status": "approved", "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        campaigns = response.json()
        for c in campaigns.get("campaigns", []):
            print(f"🔗 {c['name']} — {c['tracking_link']} — {c['seven_day_epc']}")
    except Exception as e:
        print(f"❌ Error fetching campaigns: {e}")

if __name__ == "__main__":
    fetch_campaigns()
