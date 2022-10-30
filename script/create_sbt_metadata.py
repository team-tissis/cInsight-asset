import subprocess
import json
import sys

address = sys.argv[1]


def create_json_dict(id, grade):
    json_dict = {
    "name": f"ChainInsight {id}",
    "description": "He/She is one of ChainInsight members.",
    # "external_url": "",
    "image": "https://github.com/theChainInsight/theChainInsight.github.io/sbt/img/orange/{grade}.gif",
    "attributes" :[{"trait_type":"Grade", "value":f"{grade}"}]
    }
    json_file = open(f"./sbt/{id}.json", mode="w")
    json.dump(json_dict, json_file)
    json_file.close()
    return

def git_push(address: str = ""):
    create_json_dict(address, 1)
    subprocess.run('git add ./sbt', shell=True)
    subprocess.run('git commit -m "add new sbt metadata"', shell=True)
    subprocess.run("git push origin main", shell=True)
    return

if __name__=="__main__":
    git_push(address)


