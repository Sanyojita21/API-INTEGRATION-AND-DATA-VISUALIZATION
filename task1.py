import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Fixed city name instead of input()
city = "Mumbai"

# Build the API URL
url = f"https://wttr.in/{city}?format=j1"

try:
    # Send GET request to fetch weather data
    response = requests.get(url)
    data = response.json()

    # Extract current weather info
    current = data["current_condition"][0]
    temp = int(current["temp_C"])
    humidity = int(current["humidity"])
    desc = current["weatherDesc"][0]["value"].strip()

    # Get nearest area for validation
    nearest_area = data["nearest_area"][0]["areaName"][0]["value"]

    # Prepare bar chart labels and values
    labels = ['Temperature (°C)', 'Humidity (%)']
    values = [temp, humidity]
    colors = ['skyblue', 'lightcoral']

    # Plot using seaborn
    plt.figure(figsize=(6, 4))
    sns.barplot(x=labels, y=values, palette=colors)

    # Add titles and limits
    plt.title(f"Current Weather in {nearest_area}")
    plt.ylim(0, 100)
    plt.tight_layout()

    # Show the plot
    plt.show()

# Handle no internet
except requests.exceptions.RequestException:
    print("\n⚠️ Network error. Please check your internet connection.")

# Handle any other issues
except Exception as e:
    print(f"\n⚠️ Error: {e}")
    print("Something went wrong. Try a different city or check internet.")
