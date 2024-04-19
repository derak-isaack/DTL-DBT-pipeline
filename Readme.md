## <div style="padding: 35px;color:white;margin:10;font-size:200%;text-align:center;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://images.pexels.com/photos/7078619/pexels-photo-7078619.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)"><b><span style='color:black'><strong> MALL SHOPPING DATA ANALYSIS DATA PIPELINE </strong></span></b> </div> 

![dbt](https://img.shields.io/badge/dbt-FF694B?logo=dbt&logoColor=fff&style=for-the-badge)
![aws](https://img.shields.io/badge/Amazon%20AWS-232F3E?logo=amazonaws&logoColor=fff&style=for-the-badge)
![awsS3](https://img.shields.io/badge/Amazon%20S3-569A31?logo=amazons3&logoColor=fff&style=for-the-badge)
![streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=fff&style=for-the-badge)
![Duckdb](https://img.shields.io/badge/DuckDB-FFF000?logo=duckdb&logoColor=000&style=for-the-badge)
![sql](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=fff&style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff&style=for-the-badge)


### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Project Overview</span></b> </div>

ETL and ELT data pipelines offer simplicity and automation for organizations that use cloud storage where data scales exponentially. The data pipelines enables data for analysts and modelling is readily available. Automation of data pipelines also ensures real-time tracking of important `Key Perfomance Indicators` for a business. Exponentially growing data may sometimes bring the challenge of storage constraints and embedded databases solve this efficiently.

### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Objectives</span></b> </div>

1. Develop and deploy an efficient `ETL Data Pipeline` extracting data from `AWS S3 bucket` using [data load tool](https://dlthub.com/) using [DuckDB](https://duckdb.org/docs/index) database, `transforming` it and finally `loading` it in an `DuckDB` embedded database. 

2. Prepare data for analysis using queries which can be found `[here](customersales/models)'. The queries seek to find:

* `Average age of all shoppers across various shopping malls.`

* `Average expenditure of each category of items by gender.`

* `Most profitable shopping malls by year and month.`

* `Shopping patterns across various malls.`

The extracted data from the queries can be found [here](customersales/seeds).

### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Data Extraction</span></b> </div>

The `Data Load Tool` open source library offers very efficient data pipelines offering consumption from various data sources including `Google Sheets, Cloud Storage services, APIs` and `scraping scripts`. This tool comes in handy for `e-commerce` organizations as it has the ability to track streaming data in real-time. It offers more scalability and customization depending on the needs at hand. 

Data for this project was ingested from `AWS S3` bucket. To get started with setting up the credentials to allow access by third oarty applications to your data, reading [dlt documentation](https://dlthub.com/docs/dlt-ecosystem/destinations/filesystem#aws-s3) provides a clear step by step process for the setup. 

After setting up everything, run the following commands in order to get started with `dlt`:

1. `pip install requirements.txt`

2. `dlt init filesystem duckdb`

3. To run your pipeline, run `python filesystem.py` in the terminal. This downloads a duckdb file in the working directory which contains information about the data source. 

4. To have an interaction with the data, run `dlt pipeline filesystem show` which opens streamlit on the local browser. 

For a more conclusive and extensive approach, reading [data sources](https://dlthub.com/docs/dlt-ecosystem/verified-sources/) provides more information on how to connect to several data sources. 


### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Data Transformation</span></b> </div>

Transformation of data is necessary because it needs to be error free for use by the data team to extract meaningful insights more fast than the old traditional formarts. Transformation is done using the `Data Build Tool` which is an open source platform that offers more flexibility for transformation of data in data pipelines. 

To open up the `Streamlit dashboard` to get a sneak peak of data and run simple queries, run the line `dlt pipeline filesystem show`.

This tool leverages on using `Jinja` to simplify the process of creating sql queries to handle various data objectives. It implements `DRY`-`Dont Repeat Yourself` approach which allows inheritance of `sql tables and queries`.

### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Data Loading</span></b> </div>

`DuckDb` is an embedded database which has better computational power at handling big datasets and also creates them on the fly without necessarilly loading it in `RDBMs`. It also offers compression of big files therefore coming in handy in the event of storage inefficiencies. 

It can also be connected to visualization and dashboarding tools after installation of required drivers connections. 
