import os
import sys 
import logging

log_dir="logs"
logging_str="%(asctime)s - %(levelname)s - %(message)s"

log_filepath=os.path.join(log_dir,"textSummarizer.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")