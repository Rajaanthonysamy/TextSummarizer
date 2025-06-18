from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationPipeline

logger.info("Logging setup complete. Starting the application...")

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"Starting {STAGE_NAME}...")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed successfully.")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
except Exception as e:
    logger.exception(f"An error occurred during {STAGE_NAME}: {e}")
    raise e


STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f"Starting {STAGE_NAME}...")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(f"An error occurred during {STAGE_NAME}: {e}")
    raise e

