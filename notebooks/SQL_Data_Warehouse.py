# Databricks notebook source
AI Powered Data Warehousing with Databricks SQL - Bhadresh

P0 Key Challenges in harnessing Data-Driven Insights - Page 1
Unstructured / Semi-structured Data 
Data Privacy / Security concerns
Data Quality issues
Accessibility of Data 
Limited or Incomplete Interpretation
Query Language Barrier 
How Databricks helps to address those challenges
DB SQL Architecture overview
DB SQL Features at high level
SQL Serverless & Other flavors
Intelligent Workload management/Predictive I/O - two cells - one with predictive I/O and one without predictive I/O
Liquid Clustering 
Lakeview dashboards
Federation
Data Sharing / Clean Room 
Genie Data Room
SQL Editor + Databricks Assistant
AI Generated Table Descriptions and Column Comments  
P0 DB SQL integrations with Visualization layer - partner connect - visualization 
P0 DB SQL Governance


Industry specific use cases for DB SQL 
BFSI 
Regulatory Reporting / Compliance
Fraud Detection
Insurance Usage based pricing 
Hyper Personalization 
Sustainable Finance - ESG
Manufacturing
Digital Twins
IoT Analytics
Connected Vehicle
Retail
Demand Forecasting
Customer Lifetime Value 
Propensity to Buy 


# COMMAND ----------

# MAGIC %md
# MAGIC Key Challenges in Data Warehousing 
# MAGIC
# MAGIC 1. Unstructured and Semi Structured Data 
# MAGIC
# MAGIC 2. Data Governance 
# MAGIC
# MAGIC 3. Data Accessibility 
# MAGIC
# MAGIC 4. Query Language Barrier 
# MAGIC
# MAGIC 5. Cost and Performance 
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Unstructured and Semi Structured Data
# MAGIC
# MAGIC It is easy to deal with structured data. Databases are in place for last 50-60 years or so. However, due to explosion of social media and electronics devices, the growth of unstructured data has surpassed structured data a long ago. It is relatively easy to generate insights out of structured data but it is really complex and difficult to do so for unstructured and semi structured data like videos, images, text files, etc. 
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Data Governance
# MAGIC
# MAGIC Data Governance is a key challenge as you cannot allow everyone to have access to everything in your data warehouse. Traditional Data Warehouse may allow you to apply security on structured data but same is generally not possible with unstructured or semi-structured data. Lake of proper data governance also poses compliance risk as well as reputational risk if any unwanted situation arises.

# COMMAND ----------

# MAGIC %md
# MAGIC Data Accessibility 
# MAGIC
# MAGIC Most of us will agree that Data and AI democratization help an organization to grow faster. To make data easily accessible as and when it is required by anyone with the permissions to do so is a key challenge with which data professionals are dealing with for quite sometime now.

# COMMAND ----------

# MAGIC %md
# MAGIC Query Langauge Barrier 
# MAGIC
# MAGIC Many know SQL and Python but there are many Business Analysts, Functional people who may not know how to write a SQL query to interact with the data. Here, Query Lanageuge barrier becomes the biggest hurdle to generate insights out of the data already avaiable with you.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ### Governance ###
# MAGIC <img src="https://raw.githubusercontent.com/bhadreshshiyal/MumbaiDIDays/main/GovernanceChallenge.jpg?token=GHSAT0AAAAAACR5BAFFH5AH2NNSYUOQ3MLGZRY4WGA"
# MAGIC  style="float: center; margin-right: 10px" width="900px" />
# MAGIC
# MAGIC
# MAGIC
