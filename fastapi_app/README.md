We create an environment within our working directory
python3 -m venv env

we install the necessary dependencies

pip3 install fastapi

pip install pydantic

pip3 install uvicorn

To run our application we use
uvicorn main:app --reload --host 0.0.0.0 --port 9090
