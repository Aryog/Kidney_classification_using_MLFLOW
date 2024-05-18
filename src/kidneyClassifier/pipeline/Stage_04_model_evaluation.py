from kidneyClassifier.config.configuration import ConfigurationManager
from kidneyClassifier import logger
from kidneyClassifier.components.model_evaluation import Evaluation

STAGE_NAME = "Model Evaluation"

class EvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.log_into_mlflow()
       
if __name__ == '__main__':
    try:
        logger.info(f'******************')
        logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<')
        prepare_base_model = EvaluationPipeline()
        prepare_base_model.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\n x==========x')
    except Exception as e:
        logger.exception(e)
        raise e