import os 
import urllib.request as request
import zipfile
from src.textSummarizer.logging import logger
from src.textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        logger.info("self.config.local_data_file: %s", self.config.local_data_file)
        destination = str(self.config.local_data_file)
        logger.info(f"Downloading file from {self.config.source_url} to {destination}")
        if not os.path.exists(destination):
            url=url = str(self.config.source_url)
            filename, headers = request.urlretrieve(
                url =url,
                filename = destination
            )
            logger.info(f"File is downloaded")
        else:
            logger.info(f"File already exits")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

    
