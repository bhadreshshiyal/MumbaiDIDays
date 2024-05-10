# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC <img src="https://raw.githubusercontent.com/bhadreshshiyal/MumbaiDIDays/main/resources/Governance2.png?token=GHSAT0AAAAAACR5BAFESEE5WJ7POGRIMZXUZR23JVA"
# MAGIC  style="float: center; margin-right: 10px" width="1100px" />

# COMMAND ----------

# MAGIC %md
# MAGIC #### AI Generated Comments  ####
# MAGIC https://e2-demo-field-eng.cloud.databricks.com/explore/data/main/dbdemos_retail_c360_didaymumbai/spark_churn_users?o=1444828305810485

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC <img src="https://raw.githubusercontent.com/bhadreshshiyal/MumbaiDIDays/main/resources/LanguageBarrier.png?token=GHSAT0AAAAAACR5BAFEMETEJDRC74L37FNIZR25UOA" style="float: center; margin-right: 10px" width="1100px" />
# MAGIC  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/bhadreshshiyal/MumbaiDIDays/main/resources/Lakeview.png?token=GHSAT0AAAAAACR5BAFEFAJ3GZM6W4JDUGFKZR3BK2A" style="float: center; margin-right: 10px" width="1100px" />

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Text2Viz Demo ####
# MAGIC https://e2-demo-field-eng.cloud.databricks.com/sql/dashboardsv3/01ef0d95f86912f1b4b418efee94f894?o=1444828305810485
# MAGIC
# MAGIC show bar chart of count of userid by country
# MAGIC
# MAGIC Show % of user_id by gender in pie chart
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### AI Functions Demo ####
# MAGIC
# MAGIC https://adb-984752964297111.11.azuredatabricks.net/sql/editor/9fea626b-0f17-4e92-917e-6910e886f9c0?o=984752964297111
# MAGIC
# MAGIC SELECT ai_gen('Generate a concise, cheerful email title for a launch of new LED TV product');
# MAGIC
# MAGIC SELECT ai_translate("Your Product is so amazing!", "hi")
# MAGIC
# MAGIC SELECT ai_fix_grammar('This sentence have some mistake. Pleas made corection.');
# MAGIC
# MAGIC SELECT
# MAGIC   AI_QUERY(
# MAGIC     "databricks-dbrx-instruct",
# MAGIC     "Generate a short product descrioption for a new credit card named Platinum"
# MAGIC   ) as product_review
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/bhadreshshiyal/MumbaiDIDays/main/resources/Serverless.png?token=GHSAT0AAAAAACR5BAFFSTZLXJ6IXSX3CQRQZR3BIAQ" style="float: center; margin-right: 10px" width="1100px" />

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/bhadreshshiyal/MumbaiDIDays/main/resources/PredictiveIO.png?token=GHSAT0AAAAAACR5BAFFZGQ5CTULX2Z65L56ZR3BEWQ" style="float: center; margin-right: 10px" width="1100px" />
# MAGIC
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/bhadreshshiyal/MumbaiDIDays/main/resources/LakehouseFederation.png?token=GHSAT0AAAAAACR5BAFFK7ETNHSYLJ422IRUZR3BWYQ" style="float: center; margin-right: 10px" width="1100px" />

# COMMAND ----------

# MAGIC %md
# MAGIC #### Lakehouse Federation with PostgreSQL Demo ####
# MAGIC https://adb-984752964297111.11.azuredatabricks.net/sql/editor?o=984752964297111
# MAGIC
# MAGIC CREATE CONNECTION postgres_connection_didaymumbai TYPE postgresql
# MAGIC OPTIONS (
# MAGIC   host 'demo-pgsql.postgres.database.azure.com',
# MAGIC   port '5432',
# MAGIC   user 'dbadmin',
# MAGIC   password 'vgDB@16484!!'
# MAGIC );
# MAGIC
# MAGIC CREATE FOREIGN CATALOG IF NOT EXISTS postgres_didaymumbai USING CONNECTION postgres_connection_didaymumbai
# MAGIC OPTIONS (database 'postgres');
# MAGIC
# MAGIC select * from `postgres_didaymumbai`.`public`.`churn` limit 100;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/bhadreshshiyal/MumbaiDIDays/main/resources/DataSharing.png?token=GHSAT0AAAAAACR5BAFEPIXTSSUZYVBE3LPEZR3BX7Q" style="float: center; margin-right: 10px" width="1100px" />

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/bhadreshshiyal/MumbaiDIDays/main/resources/DemandForecasting1.png" style="float: center; margin-right: 10px" width="1100px" />

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/bhadreshshiyal/MumbaiDIDays/main/resources/CustomerPropensity1.png" style="float: center; margin-right: 10px" width="1100px" />

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/bhadreshshiyal/MumbaiDIDays/main/resources/DigitalTwins1.png" style="float: center; margin-right: 10px" width="1100px" />

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/bhadreshshiyal/MumbaiDIDays/main/resources/ThankYou.png?token=GHSAT0AAAAAACR5BAFFGWPNMKV55YE2FWUIZR3CIIA" style="float: center; margin-right: 10px" width="1100px" />
