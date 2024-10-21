import json

dic = {}
i = 1

with open('points-dapport-volontaire-dechets-et-moyens-techniques.json', 'r') as json_file:
    datas = json.load(json_file)
    """ print(json.dumps(datas, indent=4, sort_keys=True)) """
    for data in datas:
        if data['type_flux'] == 'verre':
        

            dic[i] = {
                'lon' : data['geo_point_2d']['lon'],
                'lat' : data['geo_point_2d']['lat'],
                'stockage' : 5
            }
            
            i += 1
            
print(dic)

with open('geoloc_datas.json', 'w') as f:
    json.dump(dic, f, indent=2)


