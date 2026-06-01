import logging
from dotenv import load_dotenv

import dagshub

# Load environment variables from .env file
load_dotenv()

dagshub.init(  # Initialize DagsHub integration
    repo_owner='aldovitch',
    repo_name='mlops_project'    
)

# Configure the logging strategy
logging.basicConfig(
    level=logging.INFO, # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler()
    ]
)
