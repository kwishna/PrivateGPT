### Steps to execute:-
- Download the repo.
- run `pip install -r requirements.txt` to install all dependencies.
- put you own custom document in `source_documents` directory.
- create `models` folder in the directory. This is the place where the model will be downloaded. Model might be a huge file in GB.
- run `python ingest.py` to create indexing for your documents.
- run `python privateGPT.py` to query. It takes long time to answer.

This project has been cloned from another repo for learning purpose and has been modified sightly. It is done for hands-on practice.