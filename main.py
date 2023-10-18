from CNNClassifer.pipeline.stage01_data_ingetion import DataIngestionTrainingPipeline
from CNNClassifer.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline

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

STAGE_NAME = 'PREPARE BASE MODEL'
try:
    logger.info(f"****************************************************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed  <<<<<<<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e