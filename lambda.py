import json
from collections import OrderedDict
def merge_json_files(file_paths):
    final_json = OrderedDict()

    for file_path in file_paths:
        with open(file_path, 'r', encoding="utf8") as file:
            data = json.load(file)

            for key, value in data.items():
                if key not in final_json:
                    final_json[key] = value
                elif isinstance(value, list):
                    final_json[key] = list(set(final_json[key] + value))
                elif isinstance(value, dict):
                    final_json[key].update(value)
                else:
                    final_json[key] = value

    return final_json

def write_final_json(final_json, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(final_json, output_file, indent=2)

if __name__ == "__main__":
    input_files = ["contact_cognism.json", "contact_zoominfo.json","contact_lusha.json","contact_linkedin.json","contact_apollo.json"]
    output_file = "output_final.json"

    final_json_data = merge_json_files(input_files)
    write_final_json(final_json_data, output_file)

    print(f"Final JSON written to {output_file}")
