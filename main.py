import json

def main():    
    # Open file
    file = open('random-iban-data.txt', 'r')
    lines = file.readlines()
    iban_list = []
    for line in lines:
        country_code = line[:2]
        iban_code = line[2:]
        iban_dict = {country_code: iban_code}
        # Control duplicateds codes
        if iban_dict not in iban_list:
            iban_list.append(iban_dict)
    # sort list by country code
    iban_list_sorted = sorted(iban_list, key=lambda d: list(d.keys()))
    iban_json_codes = {'codes' : iban_list_sorted}

    json_object = json.dumps(iban_json_codes, indent = 4)
  
    # Writing to sample.json
    with open("iban_codes.json", "w") as outfile:
        outfile.write(json_object)       
    
    #Uncomment this part of the code you will have time to join to the container and check whatever you want
    # import time
    # time.sleep(30000)
main()