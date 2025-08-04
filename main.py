from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.textSummarizer.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


# STAGE_NAME = "Data Ingestion Stage"

# try:
#     logger.info(f"Stage: {STAGE_NAME} initiated")
#     data_ingestion_pipeline = DataIngestionTrainingPipeline()
#     data_ingestion_pipeline.initiate_data_ingestion()
#     logger.info(f"Stage: {STAGE_NAME} is completed successfully.")
# except Exception as e:
#     logger.exception(e)
#     raise e


# STAGE_NAME = "Data Transformation Stage"
# try:
#     logger.info(f"Stage: {STAGE_NAME} initiated")
#     data_transformation_pipeline = DataTransformationTrainingPipeline()
#     data_transformation_pipeline.initiate_data_transformation()
#     logger.info(f"Stage: {STAGE_NAME} is completed successfully.")
# except Exception as e:
#     logger.exception(e)
#     raise e


# STAGE_NAME = "Model Training Stage"
# try:
#     logger.info(f"Stage: {STAGE_NAME} initiated")
#     model_trainer_pipeline = ModelTrainerPipeline()
#     model_trainer_pipeline.initiate_model_trainer()
#     logger.info(f"Stage: {STAGE_NAME} is completed successfully.")
# except Exception as e:
#     logger.exception(e)
#     raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.initiate_model_evaluator()
    logger.info(f"Stage: {STAGE_NAME} is completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e