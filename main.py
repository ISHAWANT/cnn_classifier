from CNNClassifer.pipeline.stage01_data_ingetion import DataIngestionTrainingPipeline

from CNNClassifer import logger 

STAGE_NAME = 'Data Ingetion stage' 

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} Started <<<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline() 
    data_ingestion.main() 
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========x") 
except Exception as e:
    logger.exception(e) 
    raise e 