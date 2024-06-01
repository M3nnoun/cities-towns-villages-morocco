import pandas as pd
import json

data=pd.read_excel('data_banks.xlsx')
df=data.iloc[5:,:2]
df.columns=['region','ville']
print(df.head(20))
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

# Convert the list to a JSON formatted string
json_output = json.dumps(regions_list, indent=4, ensure_ascii=False)

# Print the JSON output
print(json_output)


## saving the data as json format:

def save_json_to_file(json_data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

# Save JSON data to a file
save_json_to_file(json_output, 'regions_villes.json')