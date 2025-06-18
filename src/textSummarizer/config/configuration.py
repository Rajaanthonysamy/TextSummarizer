from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.entity import DataIngestionConfig, DataTransformationConfig
from src.textSummarizer.logging import logger


class ConfigurationManager:
    def __init__(self,
                 config_path=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
        logger.info(f"Configuration file loaded: {config_path}")
        logger.info(f"Parameters file loaded: {params_filepath}")
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        logger.info(f"Data Ingestion Config: {data_ingestion_config}")
        
        return data_ingestion_config 
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config=self.config.data_trasnformation
        create_directories([config.root_dir])
        logger.info(f"Data Transformation config: {config}")
        logger.info(f"Data Transformation params: {config.data_path}")
        logger.info(f"{config.tokenizer_name}")
        logger.info(f"Data Transformation root dir: {config.root_dir}")
        return DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )