import json
from pathlib import Path
import logging


path = Path("ideas_for_test/work_with_json")

logging.basicConfig(filename="json_voloshyn.log",
                    filemode="w",
                    encoding="utf-8",
                    level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("json_validator")

for item in path.iterdir():
    if item.suffix == ".json":
        try:
            with open(item, "r", encoding="utf-8") as f:
                data = json.load(f)
                print(item.name)
        except json.JSONDecodeError:
             logger.error(f"Not valid: {item.name}")