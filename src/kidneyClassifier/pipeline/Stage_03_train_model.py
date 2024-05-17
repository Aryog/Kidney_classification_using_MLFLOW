from kidneyClassifier.config.configuration import ConfigurationManager
from kidneyClassifier import logger
from kidneyClassifier.components.train_model import Training

STAGE_NAME = "Model Training Stage"

class TrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
            config = ConfigurationManager()
            training_config = config.get_training_config()
            training = Training(config = training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
       
if __name__ == '__main__':
    try:
        logger.info(f'******************')
        logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<')
        prepare_base_model = TrainingPipeline()
        prepare_base_model.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\n x==========x')
    except Exception as e:
        logger.exception(e)
        raise e