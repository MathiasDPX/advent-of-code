from glob import glob
import requests
import os

SESSION = ""
YEAR = 2025

headers = {
    "Cookie": f"session={SESSION}"
}

for path in glob(f"{YEAR}/[0-2][0-9]"):
    day = path.split("\\")[-1]
    if not day.isdigit():
        continue
    
    day = int(day)
    
    r = requests.get(f"https://adventofcode.com/{YEAR}/day/{day}/input", headers=headers)
    
    if r.status_code != 200:
        print(f"{YEAR}/{day:02d} skipped (status code {r.status_code})")
        continue
    else:
        print(f"{YEAR}/{day:02d} downloaded")
        
    input_path = os.path.join(path, "input.txt")
    
    with open(input_path, 'wb+') as f:
        f.write(r.content)