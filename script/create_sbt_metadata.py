import subprocess
import json
import sys
import os

make_metadata_num = sys.argv[1]


num_color_map = {0: "orange",1: "green", 2: "blue", 3:"pink", 4:"white"}
def create_json_dict(token_id, grade, icon_num):
    json_dict = {
    "name": f"ChainInsight #{token_id}",
    "description": "He/She is one of ChainInsight members.",
    # "external_url": "",
    "image": f"https://team-tissis.github.io/img/{icon_num}/{grade}.gif",
    "attributes" :[{"display_type": "number", "trait_type":"Grade", "value":f"{grade}"}, {"trait_type":"color", "value":f"{num_color_map[icon_num]}"}, {"trait_type":"Position", "value":"Member"}]
    }
    json_file = open(f"./sbt/metadata/{icon_num}/{grade}/{token_id}", mode="w")
    json.dump(json_dict, json_file)
    json_file.close()
    return

def git_push(make_metadata_num: int):
    for icon_num in range(5):
        for grade in range(1,6):
            dir_name = f"./sbt/metadata/{icon_num}/{grade}"
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
                print(f"make new directory {dir_name}")
            for token_id in range(1,make_metadata_num+1):
                create_json_dict(token_id, grade, icon_num)
    subprocess.run('git add ./sbt/metadata', shell=True)
    subprocess.run('git commit -m "add new sbt metadata"', shell=True)
    subprocess.run("git push origin main", shell=True)
    return

if __name__=="__main__":
    git_push(int(make_metadata_num))
    


