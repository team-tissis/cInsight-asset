import subprocess
import json
import sys

num_color_map = {1: "green", 2: "blue", 3:"pink", 4:"white"}
def create_json_dict(token_id):
    img_id = token_id % 4
    if img_id ==0:
        img_id = 4
    json_dict = {
    "name": f"ChainInsight SkinNFT #{token_id}",
    "description": "The ChainInsight Skin NFT.",
    # "external_url": "",
    "image": f"https://team-tissis.github.io/cInsightAsset/img/{img_id}/1.gif",
    "attributes" :[{"trait_type":"color", "value":f"{num_color_map[img_id]}"}]
    }
    json_file = open(f"./skinnft/{token_id}", mode="w")
    json.dump(json_dict, json_file)
    json_file.close()
    return

def main():
    for i in range(1,9):
        create_json_dict(i)
    subprocess.run('git add ./skinnft', shell=True)
    subprocess.run('git commit -m "update skinnft"', shell=True)
    subprocess.run("git push origin main", shell=True)
    return

if __name__=="__main__":
    main()


