import requests
from bs4 import BeautifulSoup
import os


#start with initial url
initial_url = r"https://ccmc.gsfc.nasa.gov/results/run_files.php?runnumber=Erik_Mayer_032324_IT_1"
file_folder = r"G:/My Drive/Butler/Research/NASA project/SSUSI/Data/data_prep/Eflux/"

response = requests.get(initial_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Search for all <a> tags whose href contains "Eflux_e,all.txt"
links = soup.find_all('a', href=lambda href: href and "Eflux_e,all.txt" in href)

for link in links:
    file_url = link['href']
            
    # Fetch the file content
    file_response = requests.get(file_url)
    
    # Determine the file name from the URL
    file_name = os.path.basename(file_url)
    
    # Create a full path for the file to be saved
    file_path = os.path.join(file_folder, file_name)
    
    file_path
    # Save the file content to disk
    with open(file_path, 'wb') as file:
        file.write(file_response.content)
    print(f"{file_name} is saved")

print("File download is done!")
