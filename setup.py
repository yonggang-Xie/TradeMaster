from setuptools import setup, find_packages

with open('TradeMaster/README.md', "r") as fh:
    long_description = fh.read()

setup(
    name='TradeMaster',
    version='0.0.1',
    description='TradeMaster - A platform for algorithmic trading',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='NTU_trademaster',
    author_email='TradeMaster.NTU@gmail.com',
    url='https://github.com/TradeMaster-NTU/TradeMaster',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires= ["Flask",   
     "Flask-Cors",  
      "mmcv",   
      # "git+https://github.com/optuna/optuna.git", 
      "prettytable",  
      "plotly",   
      "psutil",    
      "scipy",
      "spacy", 
      "sqlalchemy",  
      "pandas",    
      "iopath",   
      "yfinance",    
      "matplotlib",    
      "statsmodels",    
      "scikit_learn",    
      "tslearn",    
#       "gym",    
#       "gymnasium",    
#       "ray[rllib]==1.13.0",    
#       "tensorflow==2.11.0",    
#       "packaging",    
#       "kaleido==0.1.0",    
#       "h5py",    
#       "pydantic==1.10.2",    
      "jupyter",    
      "celery",    
      "pika"],
)
