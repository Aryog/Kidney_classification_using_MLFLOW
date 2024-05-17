from kidneyClassifier import logger
from kidneyClassifier.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline
from kidneyClassifier.pipeline.Stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from kidneyClassifier.pipeline.Stage_03_train_model import TrainingPipeline
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\n x==========x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Base Model Preparation Stage"
try:
    logger.info(f'******************')
    logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<')
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\n x==========x')
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Training Stage"

try:
    logger.info(f'******************')
    logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<')
    prepare_base_model = TrainingPipeline()
    prepare_base_model.main()
    logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\n x==========x')
except Exception as e:
    logger.exception(e)
    raise e