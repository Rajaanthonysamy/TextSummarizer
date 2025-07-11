from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    """
    Data Ingestion Configuration
    """
    root_dir: Path 
    source_url: Path
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path 
    data_path: Path 
    tokenizer_name: Path