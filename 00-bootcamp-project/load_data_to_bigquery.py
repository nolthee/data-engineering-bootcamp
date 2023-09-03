import json
import os

from google.cloud import bigquery
from google.oauth2 import service_account


DATA_FOLDER = "data"

# ตัวอย่างการกำหนด Path ของ Keyfile ในแบบที่ใช้ Environment Variable มาช่วย
# จะทำให้เราไม่ต้อง Hardcode Path ของไฟล์ไว้ในโค้ดของเรา
# keyfile = os.environ.get("KEYFILE_PATH")

keyfile = "deb2-loading-data-to-biqquery.json"
service_account_info = json.load(open(keyfile))
credentials = service_account.Credentials.from_service_account_info(service_account_info)
project_id = "deb2-200014"
client = bigquery.Client(
    project=project_id,
    credentials=credentials,
)

# Addressess
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
)

data = "addresses"
file_path = f"{DATA_FOLDER}/{data}.csv"
with open(file_path, "rb") as f:
    table_id = f"{project_id}.my_deb_bootcamp_project.{data}"
    job = client.load_table_from_file(f, table_id, job_config=job_config)
    job.result()

table = client.get_table(table_id)
print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

# ----------

# Events
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    time_partitioning=bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.DAY,
        field="created_at",
    ),
)

dt = "2021-02-10"
partition = dt.replace("-", "")
data = "events"
file_path = f"{DATA_FOLDER}/{data}.csv"
with open(file_path, "rb") as f:
    table_id = f"{project_id}.my_deb_bootcamp_project.{data}${partition}"
    job = client.load_table_from_file(f, table_id, job_config=job_config)
    job.result()

table = client.get_table(table_id)
print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

#order
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
)

data = "order"
file_path = f"{DATA_FOLDER}/{data}.csv"
with open(file_path, "rb") as f:
    table_id = f"{project_id}.my_deb_bootcamp_project.{data}"
    job = client.load_table_from_file(f, table_id, job_config=job_config)
    job.result()

table = client.get_table(table_id)
print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

#orders
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    time_partitioning=bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.DAY,
        field="created_at",
    ),
)

dt = "2021-02-10"
partition = dt.replace("-", "")
data = "orders"
file_path = f"{DATA_FOLDER}/{data}.csv"
with open(file_path, "rb") as f:
    table_id = f"{project_id}.my_deb_bootcamp_project.{data}${partition}"
    job = client.load_table_from_file(f, table_id, job_config=job_config)
    job.result()

table = client.get_table(table_id)
print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

#products
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
)

data = "products"
file_path = f"{DATA_FOLDER}/{data}.csv"
with open(file_path, "rb") as f:
    table_id = f"{project_id}.my_deb_bootcamp_project.{data}"
    job = client.load_table_from_file(f, table_id, job_config=job_config)
    job.result()

table = client.get_table(table_id)
print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

#promos
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
)

data = "promos"
file_path = f"{DATA_FOLDER}/{data}.csv"
with open(file_path, "rb") as f:
    table_id = f"{project_id}.my_deb_bootcamp_project.{data}"
    job = client.load_table_from_file(f, table_id, job_config=job_config)
    job.result()

table = client.get_table(table_id)
print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

#users
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    time_partitioning=bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.DAY,
        field="created_at",
    ),
)

dt = "2020-10-23"
partition = dt.replace("-", "")
data = "users"
file_path = f"{DATA_FOLDER}/{data}.csv"
with open(file_path, "rb") as f:
    table_id = f"{project_id}.my_deb_bootcamp_project.{data}${partition}"
    job = client.load_table_from_file(f, table_id, job_config=job_config)
    job.result()

table = client.get_table(table_id)
print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")