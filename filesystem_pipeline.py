import os
import posixpath
from typing import Iterator

import dlt
from dlt.sources import TDataItems

try:
    from .filesystem import FileItemDict, filesystem, readers, read_csv  # type: ignore
except ImportError:
    from filesystem import (
        FileItemDict,
        filesystem,
        readers,
        read_csv,
    )
    
    
TESTS_BUCKET_URL = "s3://customerbehaviour0003/"
FILE_PATH = "customer_shopping_data.csv"

def read_csv_with_duckdb() -> None:
    # Set up the DLT pipeline
    pipeline = dlt.pipeline(
        pipeline_name="standard_filesystem2",
        destination='duckdb',
        dataset_name="customer_shopping_data",
        full_refresh=True
    )
    # Load the CSV data from the specified S3 bucket URL
    customer_data = readers(
        bucket_url=TESTS_BUCKET_URL, file_glob=FILE_PATH
    ).read_csv_duckdb(chunk_size=1000, header=True)

    # Run the pipeline to load the data into DuckDB
    load_info = pipeline.run(customer_data, table_name='Customer_data')
    

    # Print information about the data loading process
    print(load_info)
    print(pipeline.last_trace.last_normalize_info)

if __name__ == "__main__":
    read_csv_with_duckdb()