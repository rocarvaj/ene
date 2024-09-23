#!/usr/bin/env python


import requests
import itertools
import os

# Function to download a CSV file from the given URL and save it to the local system
def download_csv(url, save_path):
    try:
        response = requests.get(url)
        # If the request was successful, status_code will be 200
        if response.status_code == 200:
            # Save the content to the specified file path
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"File saved successfully: {save_path}")
        else:
            print(f"Failed to download {url}. HTTP Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Function to generate URLs and download files based on a range of years
def download_files_for_years(start_year, end_year):
    base_url = "https://www.ine.gob.cl/docs/default-source/ocupacion-y-desocupacion/bbdd"

    trimestres = ['02-efm', '05-amj', '08-jas', '11-ond']
    
    # Loop over the range of years and trimesters
    for year, trim in itertools.product(range(start_year, end_year + 1), trimestres):
        url = f"{base_url}/{year}/csv/ene-{year}-{trim}.csv?download=true"
        
        # Define where to save the downloaded file
        #save_dir = f"./{year}"  # Create a directory for each year
        #if not os.path.exists(save_dir):
        #    os.makedirs(save_dir)
        
        #save_path = f"{save_dir}/ene-{year}-{trim}.csv"
        save_path = f"./ene-{year}-{trim}.csv"
        
        # Download the CSV
        download_csv(url, save_path)

# Main function to prompt the user and run the download process
def main():
    # Get the range of years from the user
    start_year = int(input("Enter the start year: "))
    end_year = int(input("Enter the end year: "))
    
    # Download files for the specified year range
    download_files_for_years(start_year, end_year)

if __name__ == "__main__":
    main()
