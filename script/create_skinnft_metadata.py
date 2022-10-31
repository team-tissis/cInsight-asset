import subprocess
import json
import sys
import cv2
import numpy as np


def create_image(token_id, red, green, blue):
    height = 200
    width = 200
    blank = np.zeros((height, width, 3))
    blank += [red, green, blue][::-1]
    cv2.imwrite(f'./skinnft/img/{token_id}.png',blank)

def create_json_dict(token_id, red, green, blue):
    json_dict = {
    "name": f"ChainInsight SkinNFT #{token_id}",
    "description": "The Skin NFT of ChainInsight.",
    # "external_url": "",
    "image": f"https://theChainInsight.github.io/skinnft/img/{token_id}.png",
    "attributes" :[{"trait_type":"red", "value":f"{red}"}, {"trait_type":"green", "value":f"{green}"}, {"trait_type":"blue", "value":f"{blue}"}]
    }
    json_file = open(f"./skinnft/{token_id}.json", mode="w")
    json.dump(json_dict, json_file)
    json_file.close()
    return

def create_bulk_metadata(num):
    for i in range(1,num+1):
        token_id = format(i, "05")
        red = (i%4) * 60
        green = (i%16//4) * 60
        blue = (i//16) * 60
        create_image(token_id, red, green, blue)
        create_json_dict(token_id, red, green, blue)



def main():
    create_bulk_metadata(50)
    subprocess.run('git add ./skinnft', shell=True)
    subprocess.run('git commit -m "add new sbt metadata"', shell=True)
    subprocess.run("git push origin main", shell=True)
    return

if __name__=="__main__":
    main()


