from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()

def start(event: dict, context: LambdaContext) -> None:
    logger.info("Starting stop watch ....")
