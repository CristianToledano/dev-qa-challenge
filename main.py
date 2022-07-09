import json

def get_all_country_codes(items):
    list_of_country_codes = []
    for line in items:
        country_code = line[:2]
        if country_code not in list_of_country_codes:
            list_of_country_codes.append(country_code)
    return list_of_country_codes

def generate_dict_with_list(list_of_country_codes):
    country_dict = {}
    for country in list_of_country_codes:
        country_dict[country] = []
    return country_dict

def build_dict(items, country_dict):
    for line in items:
        country_code = line[:2]
        country_dict[country_code].append(line.rstrip('\n'))
    return country_dict

def main():    
    # Open file
    file = open('random-iban-data.txt', 'r')
    lines = file.readlines()
    country_codes = get_all_country_codes(lines)
    dict_list_country = generate_dict_with_list(country_codes)
    final_dict = build_dict(lines, dict_list_country)

    sort_dictionary = dict(sorted(final_dict.items(), key=lambda item: item[1])) 
    json_object = json.dumps(sort_dictionary, indent = 4)
  
    # Writing to sample.json
    with open("iban_codes.json", "w") as outfile:
        outfile.write(json_object)       
    
    #Uncomment this part of the code you will have time to join to the container and check whatever you want
    # import time
    # time.sleep(30000)
main()

