import subprocess
import json
import sys
import web3 as Web3

address = sys.argv[1]


def create_json_dict(id, grade, admin):
    if admin:
        json_dict = {
        "name": f"ChainInsight {id}",
        "description": "He/She is one of ChainInsight members.",
        # "external_url": "",
        "image": f"https://theChainInsight.github.io/sbt/img/orange/{grade}.gif",
        "attributes" :[{"trait_type":"Grade", "value":f"{grade}"}, {"trait_type":"Position", "value":""}]
        }

    else:
        json_dict = {
        "name": f"ChainInsight {id}",
        "description": "He/She is one of ChainInsight members.",
        # "external_url": "",
        "image": f"https://theChainInsight.github.io/sbt/img/white/{grade}.gif",
        "attributes" :[{"trait_type":"Grade", "value":f"{grade}"}, {"trait_type":"Position", "value":"Admin"}]
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

def get_contract():
    address = '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F988'
    abi = '[{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"minter_","type":"address"},...'
    contract_instance = w3.eth.contract(address=address, abi=abi)

# read state:
contract_instance.functions.storedValue().call()


if __name__=="__main__":
    git_push(address)
