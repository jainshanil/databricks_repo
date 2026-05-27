# Databricks notebook source
dbutils.widgets.text("catalog", "dbx_demo_wrkspace_dev")
dbutils.widgets.text("schema", "finance_data_smith")
catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

spark.sql(f"USE CATALOG {catalog}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {schema}")
spark.sql(f"USE SCHEMA {schema}")


# COMMAND ----------

# MAGIC %run ../utils/run_utils

# COMMAND ----------

spark.sql(f"""
create table {catalog}.{schema}.gender_stats
as 
select country,count_if(upper(gender) = 'FEMALE') as female_count,count_if(upper(gender) = 'MALE') as male_count 
from samples.bakehouse.sales_customers 
group by country
""")

# COMMAND ----------

