# Hello World


## Create a Python 3.12+ Conda Envirnoment 

    conda create --name myenv3_11 python=3.11.5
    conda env list
    conda activate myenv3_11
    python --version


## Install Dependencies   

Read: 

https://note.nkmk.me/en/python-pip-install-requirements/

https://github.com/theskumar/python-dotenv

Install:

    pip install -r requirements.txt


## Envirnoment Variables

Rename .env_bak to .env and save your keys in this file

### Get Open API Keys:

https://platform.openai.com/account/api-keys 

Note: 

When you open a new API account you will get a one time free credit. A new account with a different phone number and email would be granted the current trial of $5 which will expire.

You will be able to make ~750 API calls with the $5 credit.

Also note, you only get free credits for the first account associated with your phone number. Subsequent accounts are not granted free credits.

### Get Pinecone API Keys

Signup for a Account on Pinecone and get API keys:

https://www.pinecone.io/ 

### Upgrade Offen

    pip install --upgrade openai


    