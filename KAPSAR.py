# Imports
from bs4 import BeautifulSoup
import requests

Codeurl = " http://www.eia.gov/dnav/pet/pet_pri_spt_s1_d.htm"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

try:
   
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Access the HTML content
        html_content = response.content

        # Process the HTML content as needed
        # ...

    else:
        print("Error: Failed to fetch the HTML content. Status code:", response.status_code)
        # Handle the error case appropriately

except requests.exceptions.RequestException as e:
    print("Error: Failed to fetch the HTML content.", e)
    # Handle the exception case appropriately