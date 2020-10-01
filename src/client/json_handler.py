import json


class JsonHandler:

    @staticmethod
    def write_json(phone_entry, first_entry, last_entry, number_entry, street_entry, city_entry, state_entry):
        data = {'info': []}
        data['info'].append({
            'first': first_entry,
            'last': last_entry,
            'phone': phone_entry,
            'houseNum': number_entry,
            'street': street_entry,
            'city': city_entry,
            'state': state_entry
        })

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)
