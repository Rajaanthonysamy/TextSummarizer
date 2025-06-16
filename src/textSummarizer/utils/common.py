import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): The path to the YAML file.
        
    Returns:
        ConfigBox: The content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error reading YAML file at {path_to_yaml}: {e}")
        raise e
    
@ensure_annotations
def create_directories(dirs: list,verbose= True) -> None:
    """
    Creates directories if they do not exist.
    
    Args:
        dirs (list): List of directory paths to create.
    """
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        logger.info(f"Created directory: {dir_path}")
        if verbose:
            logger.info(f"Directory already exists: {dir_path}")