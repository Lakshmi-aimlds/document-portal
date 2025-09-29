import os
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from langchain.output_parsers import OutputFixinfParser
from langchain_core.output_parsers import JsonOutputParser

class DataAnalyzer:
    """
    Analyzes and processes document data using language models.
    Automatically logs all the actions and supports session-based organization.
    """
    
    def __init__(self):
        pass
    
    def analyze_metadata(self):
        pass