import os
import logging
from pathlib import Path

list_of_files =[
    "app/__init__.py",
    "app/transcript_data.py",
    "app/vectorize.py",
    "app/store.py",
    "app/RAGChain.py",
    "main.py",
    ".env"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
