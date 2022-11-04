import subprocess
import json
import sys
import os

make_metadata_num = sys.argv[1]


def create_json_dict(token_id, grade):
    json_dict = {
    "name": f"ChainInsight #{token_id}",
    "description": "He/She is one of ChainInsight members.",
    # "external_url": "",
    "image": f"https://theChainInsight.github.io/sbt/img/hackathondemo/{grade}.gif",
    "attributes" :[{"trait_type":"Grade", "value":f"{grade}"}]
    }
    json_file = open(f"./sbt/metadata/{grade}/{token_id}", mode="w")
    json.dump(json_dict, json_file)
    json_file.close()
    return

def git_push(make_metadata_num: int):
    for grade in range(1,6):
        dir_name = f"./sbt/metadata/{grade}"
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            print(f"make new directory {dir_name}")
        for token_id in range(1,make_metadata_num+1):
            create_json_dict(token_id, grade)
    subprocess.run('git add ./sbt/metadata', shell=True)
    subprocess.run('git commit -m "add new sbt metadata"', shell=True)
    subprocess.run("git push origin main", shell=True)
    return

if __name__=="__main__":
    git_push(int(make_metadata_num))
    


