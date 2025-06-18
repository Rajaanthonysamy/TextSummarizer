from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionPipeline


logger.info("Logging setup complete. Starting the application...")

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"Starting {STAGE_NAME}...")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(f"An error occurred during {STAGE_NAME}: {e}")
    raise e

