import subprocess
from glob import glob
import os
import json

import argparse
parser = argparse.ArgumentParser(
    prog='magically create deploy json',
    description="inefficient but work")
parser.add_argument('-o', '--outfile', default="deploy.json")
args = parser.parse_args()

tmp_deploy = {}

components = [p.replace(".sol", "")
              for p in os.listdir("src/components/") if ".sol" in p]

tmp_deploy['components'] = components
tmp_deploy["systems"] = []

for f in glob("src/systems/*.sol"):
    print(f"processing {f}")
    tmp_system = {'name': f.split(
        "/")[-1].replace(".sol", ""), "writeAccess": []}
    bashCommand = f"forge flatten {f}"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    for c in components:
        if c in str(output):
            tmp_system['writeAccess'].append(c)
    tmp_deploy["systems"].append(tmp_system)

result = json.dumps(tmp_deploy, indent=4)
with open(args.outfile, 'w') as fp:
    fp.write(result)
print(f"write to deploy conf to {args.outfile}")