from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from config.constants import MODEL_OPENAI

def get_model_client():
    openai_model_client = OpenAIChatCompletionClient(
        model=MODEL_OPENAI,
        api_key=os.getenv('OPENAI_API_KEY')
    )

    return openai_model_client