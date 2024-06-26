# Databricks notebook source
# MAGIC %md The purpose of this notebook is to download and set up the data we will use for the solution accelerator. Before running this notebook, make sure you have entered your own credentials for Kaggle and have agreed to the Terms and Conditions of using this dataset.

# COMMAND ----------

# MAGIC %pip install kaggle

# COMMAND ----------

# MAGIC %md 
# MAGIC Set Kaggle credential configuration values in the block below: You can set up a [secret scope](https://docs.databricks.com/security/secrets/secret-scopes.html) to manage credentials used in notebooks. See the `./RUNME` notebook for guidance on how to set up a secret scope. 

# COMMAND ----------

import os
os.environ['kaggle_username'] = 'bhadreshs' # replace with your own credential here temporarily or set up a secret scope with your credential
os.environ['kaggle_username'] = dbutils.secrets.get("solution-accelerator-cicd", "kaggle_username")

os.environ['kaggle_key'] = '642240744e92eb3aecb23d1847af0cbe' # replace with your own credential here temporarily or set up a secret scope with your credential
os.environ['kaggle_key'] = dbutils.secrets.get("solution-accelerator-cicd", "kaggle_key")

# COMMAND ----------

# MAGIC %md Download the data from Kaggle using the credentials set above:

# COMMAND ----------

# MAGIC %sh 
# MAGIC cd /databricks/driver
# MAGIC export KAGGLE_USERNAME=$kaggle_username
# MAGIC export KAGGLE_KEY=$kaggle_key
# MAGIC kaggle datasets download -d frtgnn/dunnhumby-the-complete-journey
# MAGIC unzip dunnhumby-the-complete-journey.zip

# COMMAND ----------

# MAGIC %md Set config for the path to move data into. Also initialize the database we will use for the accelerator.

# COMMAND ----------

# MAGIC %run ./config

# COMMAND ----------

# MAGIC %md Move the downloaded data to the folder used throughout the accelerator:

# COMMAND ----------

dbutils.fs.mv("file:/databricks/driver/campaign_desc.csv", f"dbfs:{config['mount_point']}/bronze/campaign_desc.csv")
dbutils.fs.mv("file:/databricks/driver/campaign_table.csv", f"dbfs:{config['mount_point']}/bronze/campaign_table.csv")
dbutils.fs.mv("file:/databricks/driver/causal_data.csv", f"dbfs:{config['mount_point']}/bronze/causal_data.csv")
dbutils.fs.mv("file:/databricks/driver/coupon.csv", f"dbfs:{config['mount_point']}/bronze/coupon.csv")
dbutils.fs.mv("file:/databricks/driver/coupon_redempt.csv", f"dbfs:{config['mount_point']}/bronze/coupon_redempt.csv")
dbutils.fs.mv("file:/databricks/driver/hh_demographic.csv", f"dbfs:{config['mount_point']}/bronze/hh_demographic.csv")
dbutils.fs.mv("file:/databricks/driver/product.csv", f"dbfs:{config['mount_point']}/bronze/product.csv")
dbutils.fs.mv("file:/databricks/driver/transaction_data.csv", f"dbfs:{config['mount_point']}/bronze/transaction_data.csv")

# COMMAND ----------


