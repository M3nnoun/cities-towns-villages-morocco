import pandas as pd
import json

data=pd.read_excel('data_banks.xlsx')
df=data.iloc[5:,:2]
df.columns=['region','ville']
print(df.head(20))


def create_json_from_dataframe(df):
    # Create a dictionary to hold the JSON structure
    region_dict = {}

    # Populate the dictionary with regions and villes
    for idx, row in df.iterrows():
        region = row['region']
        ville = row['ville']
        
        if region not in region_dict:
            region_dict[region] = {'id': len(region_dict) + 1, 'region': region, 'villes': []}
        
        # Check if the ville already exists in the list of villes for the region
        if not any(ville_dict['ville'] == ville for ville_dict in region_dict[region]['villes']):
            region_dict[region]['villes'].append({'id': len(region_dict[region]['villes']) + 1, 'ville': ville})

    # Convert the dictionary to a list
    regions_list = list(region_dict.values())

    return regions_list

def save_json_to_file(json_data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

# Create JSON data from dataframe
json_data = create_json_from_dataframe(df)

# Save JSON data to a file
save_json_to_file(json_data, 'regions_villes.json')
