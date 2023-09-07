from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion,DataIngestionConfig
import sys

if __name__ == '__main__':
    logging.info('Starting Execution')
    
    
    try:
        
       # Data_Ingestion_config = DataIngestionConfig()
       Data_Ingestion = DataIngestion()
       Data_Ingestion.Initiate_Data_Ingestion()
       
    except Exception as e:
        logging.info('Custom Exception')
        raise CustomException(e,sys)