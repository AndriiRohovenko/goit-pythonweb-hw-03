from pathlib import Path
import json
from datetime import datetime
import os

storage_path = os.path.join(os.path.dirname(__file__), "data.json")


def write_data_to_file(new_data: dict) -> None:
    file = Path(storage_path)
    if file.exists():
        with open(file, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}

    timestamp = str(datetime.now())
    data[timestamp] = new_data

    with open(file, "w") as f:
        json.dump(data, f, indent=4)
