from kidneyClassifier import logger
from kidneyClassifier.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\n x==========x')
except Exception as e:
    logger.exception(e)
    raise e