import os 
from pathlib import Path

package_name = "mongodb_connect"

list_of_files=[

".github/workflows/ci.yaml",
"src/__inti__.py",
"src/components/__init__.py",
f"src/{package_name}/__init__.py",
f"src/{package_name}/mongodb_crud.py",
"src/components/data_ingestion.py",
"src/components/data_transformation.py",
"src/components/model_trainer.py",
"src/components/model_evaluation.py",
"src/pipeline/__init__.py",
"src/pipeline/training_pipeline.py",
"src/utils/__init__.py",
"src/utils/utils.py",
"src/logger/logging.py",
"src/exception/exceptions.py",
"tests/unit/__init__.py",
"tests/integration/__inti__.py",
"init_setup.sh",
"requirements.txt",
"requirements_dev.txt",
"setup.py",
"setup.cfg",
"pyproject.toml",
"tox.ini",
"experiment/experiments.ipynb"


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename= os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True )
       

    if(not os.path.exists(filepath))or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass