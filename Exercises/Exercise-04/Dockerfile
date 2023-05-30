FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install plotly_express dash dash_bootstrap_components pandas requests

ENTRYPOINT ["sh", "-c", "python ./Lec3-ETL_pipeline/scripts/main.py && python ./Lec3-ETL_pipeline/scripts/dashboard.py"]

#CMD ["python", "./Lec3-ETL_pipeline/scripts/main.py ./Lec3-ETL_pipeline/scripts/dashboard.py"]