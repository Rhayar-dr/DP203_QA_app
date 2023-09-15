
# Define questions, choices, and answers
# For demonstration, I'll use only 3 questions.

questions = [
        {
            'question': 'You need to trigger an Azure Data Factory pipeline when a file arrives in an Azure Data Lake Storage Gen2 container. Which resource provider should you enable?',
            'choices': ['Microsoft.Sql', 'Microsoft.Automation', 'Microsoft. EventGrid','Microsoft. EventHub'],
            'answer': 'Microsoft. EventGrid',
            'explanation': '''Event-driven architecture (EDA) is a common data integration pattern that involves production, detection, consumption, and reaction to events. 
            Data integration scenarios often require Data Factory customers to trigger pipelines based on events happening in storage account, such as the arrival or deletion of a file in Azure Blob Storage account. 
            Data Factory natively integrates with Azure Event Grid, which lets you trigger pipelines on such events.
            Reference:
            https://docs.microsoft.com/en-us/azure/data-factory/how-to-create-event-trigger
            https://docs.microsoft.com/en-us/azure/data-factory/concepts-pipeline-execution-triggers'''
        },
        {
            'question': 'You plan to perform batch processing in Azure Databricks once daily. Which type of Databricks cluster should you use?',
            'choices': ['High Concurrency', 'automated', 'interactive'],
            'answer': 'automated',
            'explanation': '''Azure Databricks has two types of clusters: interactive and automated. You use interactive clusters to analyze data collaboratively with interactive notebooks. You use automated clusters to run fast and robust automated jobs.
            Example: Scheduled batch workloads (data engineers running ETL jobs)
            This scenario involves running batch job JARs and notebooks on a regular cadence through the Databricks platform.
            The suggested best practice is to launch a new cluster for each run of critical jobs. This helps avoid any issues (failures, missing SLA, and so on) due to an existing workload (noisy neighbor) on a shared cluster.
            Reference:
            https://docs.databricks.com/administration-guide/cloud-configurations/aws/cmbp.htm'''
        },
        {
            'question': 'You have an Azure Data Factory that contains 10 pipelines. You need to label each pipeline with its main purpose of either ingest, transform, or load. The labels must be available for grouping and filtering when using the monitoring experience in Data Factory. What should you add to each pipeline?',
            'choices': ['a resource tag', 'a correlation ID', 'a run group ID', 'an annotation'],
            'answer': 'an annotation',
            'explanation': '''Annotations are additional, informative tags that you can add to specific factory resources: pipelines, datasets, linked services, and triggers. By adding annotations, you can easily filter and search for specific factory resources.
            Reference:
            https://www.cathrinewilhelmsen.net/annotations-user-properties-azure-data-factory/'''
        },
        {
            'question': 'You have an Azure Data Factory instance that contains two pipelines named Pipeline 1 and Pipeline2. You execute Pipeline2, and Stored procedure 1 in Pipeline1 fails. What is the status of the pipeline runs?',
            'choices': [
                'Pipeline1 and Pipeline2 succeeded.',
                'Pipeline1 and Pipeline2 failed.',
                'Pipeline1 succeeded and Pipeline2 failed.',
                'Pipeline1 failed and Pipeline2 succeeded.'
            ],
            'answer': 'Pipeline1 and Pipeline2 succeeded.',
            'explanation': '''Activities are linked together via dependencies. A dependency has a condition of one of the following: Succeeded, Failed, or Completed.
            Consider Pipeline1:
            If we have a pipeline with two activities where Activity2 has a failure dependency on Activity1, the pipeline will not fail just because Activity1 failed. If Activity1 fails and Activity2 succeeds, the pipeline will succeed. This scenario is treated as a try-catch block by Data Factory.
            The failure dependency means this pipeline reports success.
            Note:
            If we have a pipeline containing Activity1 and Activity2, and Activity2 has a success dependency on Activity1, it will only execute if Activity1 is successful. In this scenario, if Activity1 fails, the pipeline will fail.
            Reference:
            https://datasavvy.me/category/azure-data-factory/''',
            'image': 'static/images/image_question_4.jpg'  # Path to the image file
        },
        {
            'question': 'You need to schedule an Azure Data Factory pipeline to execute when a new file arrives in an Azure Data Lake Storage Gen2 container. Which type of trigger should you use?',
            'choices': ['on-demand', 'tumbling window', 'schedule', 'event'],
            'answer': 'event',
            'explanation': '''Event-driven architecture (EDA) is a common data integration pattern that involves production, detection, consumption, and reaction to events. Data integration scenarios often require Data Factory customers to trigger pipelines based on events happening in storage account, such as the arrival or deletion of a file in Azure Blob Storage account.
            Reference:
            https://docs.microsoft.com/en-us/azure/data-factory/how-to-create-event-trigger'''
        },
        {
            'question': 'You have two Azure Data Factory instances named ADFdev and ADFprod. ADFdev connects to an Azure DevOps Git repository. You publish changes from the main branch of the Git repository to ADFdev. You need to deploy the artifacts from ADFdev to ADFprod. What should you do first?',
            'choices': [
                'From ADFdev, modify the Git configuration.',
                'From ADFdev, create a linked service.',
                'From Azure DevOps, create a release pipeline.',
                'From Azure DevOps, update the main branch.'
            ],
            'answer': 'From Azure DevOps, create a release pipeline.',
            'explanation': '''In Azure Data Factory, continuous integration and delivery (CI/CD) means moving Data Factory pipelines from one environment (development, test, production) to another.
            Note: The following is a guide for setting up an Azure Pipelines release that automates the deployment of a data factory to multiple environments.
            1. In Azure DevOps, open the project that's configured with your data factory.
            2. On the left side of the page, select Pipelines, and then select Releases.
            3. Select New pipeline, or, if you have existing pipelines, select New and then New release pipeline.
            4. In the Stage name box, enter the name of your environment.
            5. Select Add artifact, and then select the git repository configured with your development data factory. Select the publish branch of the repository for the Default branch. By default, this publish branch is adf_publish.
            6. Select the Empty job template.
            Reference:
            https://docs.microsoft.com/en-us/azure/data-factory/continuous-integration-deployment'''
        },
        {
            'question': 'You are developing a solution that will stream to Azure Stream Analytics. The solution will have both streaming data and reference data. Which input type should you use for the reference data?',
            'choices': [
                'Azure Cosmos DB',
                'Azure Blob storage',
                'Azure loT Hub',
                'Azure Event Hubs'
            ],
            'answer': 'Azure Blob storage',
            'explanation': '''Stream Analytics supports Azure Blob storage and Azure SQL Database as the storage layer for Reference Data.
            Reference:
            https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-use-reference-data'''
        },
        {
            'question': 'You are designing an Azure Stream Analytics job to process incoming events from sensors in retail environments. You need to process the events to produce a running average of shopper counts during the previous 15 minutes, calculated at five-minute intervals. Which type of window should you use?',
            'choices': ['snapshot', 'tumbling', 'hopping', 'sliding'],
            'answer': 'hopping',
            'explanation': '''Hopping, as we need to calculate a running average, which means it will have overlapping.
            Reference:
            https://docs.microsoft.com/en-us/stream-analytics-query/hopping-window-azure-stream-analytics
            https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-window-functions'''
        },
        {
            'question': 'You are monitoring an Azure Stream Analytics job by using metrics in Azure. You discover that during the last 12 hours, the average watermark delay is consistently greater than the configured late arrival tolerance. What is a possible cause of this behavior?',
            'choices': [
                'Events whose application timestamp is earlier than their arrival time by more than five minutes arrive as inputs.',
                'There are errors in the input data.',
                'The late arrival policy causes events to be dropped.',
                'The job lacks the resources to process the volume of incoming data'
            ],
            'answer': 'The job lacks the resources to process the volume of incoming data',
            'explanation': '''Watermark Delay indicates the delay of the streaming data processing job.
        There are a number of resource constraints that can cause the streaming pipeline to slow down. The watermark delay metric can rise due to:
        1. Not enough processing resources in Stream Analytics to handle the volume of input events. To scale up resources, see Understand and adjust Streaming Units.
        2. Not enough throughput within the input event brokers, so they are throttled. For possible solutions, see Automatically scale up Azure Event Hubs throughput units.
        3. Output sinks are not provisioned with enough capacity, so they are throttled. The possible solutions vary widely based on the flavor of output service being used.
        Reference:
        https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-time-handling'''
        },
        {
            'question': 'You plan to build a structured streaming solution in Azure Databricks. The solution will count new events in five-minute intervals and report only events that arrive during the interval. The output will be sent to a Delta Lake table. Which output mode should you use?',
            'choices': ['update', 'complete', 'append'],
            'answer': 'append',
            'explanation': '''Append Mode: Only new rows appended in the result table since the last trigger are written to external storage. This is applicable only for the queries where existing rows in the Result Table are not expected to change.
        Incorrect Answers:
        B: Complete Mode: The entire updated result table is written to external storage. It is up to the storage connector to decide how to handle the writing of the entire table.
        A: Update Mode: Only the rows that were updated in the result table since the last trigger are written to external storage. This is different from Complete Mode in that Update Mode outputs only the rows that have changed since the last trigger. If the query doesn't contain aggregations, it is equivalent to Append mode.
        Reference:
        https://docs.databricks.com/getting-started/spark/streaming.html'''
        },
        {
            'question': 'You have an Azure Data Factory version 2 (V2) resource named Df1. Df1 contains a linked service. You have an Azure Key vault named vault that contains an encryption key named key1. You need to encrypt Df1 by using key1. What should you do first?',
            'choices': [
                'Add a private endpoint connection to vaul1.',
                'Enable Azure role-based access control on vault.',
                'Remove the linked service from Df1.',
                'Create a self-hosted integration runtime.'
            ],
            'answer': 'Remove the linked service from Df1.',
            'explanation': '''Linked services are much like connection strings, which define the connection information needed for Data Factory to connect to external resources.
        "Ensure the Data Factory is empty. The data factory can't contain any resources such as linked services, pipelines, and data flows. For now, deploying customer-managed key to a non-empty factory will result in an error."
        Incorrect Answers:
        D: A self-hosted integration runtime copies data between an on-premises store and cloud storage.
        Reference:
        https://docs.microsoft.com/en-us/azure/data-factory/enable-customer-managed-key'''
        },
        {
            'question': 'You are designing an Azure Synapse Analytics dedicated SQL pool. You need to ensure that you can audit access to Personally Identifiable Information (PII). What should you include in the solution?',
            'choices': [
                'column-level security',
                'dynamic data masking',
                'row-level security (RLS)',
                'sensitivity classifications'
            ],
            'answer': 'sensitivity classifications',
            'explanation': '''Data Discovery & Classification is built into Azure SQL Database, Azure SQL Managed Instance, and Azure Synapse Analytics. It provides basic capabilities for discovering, classifying, labeling, and reporting the sensitive data in your databases.
        Your most sensitive data might include business, financial, healthcare, or personal information. Discovering and classifying this data can play a pivotal role in your organization's information-protection approach. It can serve as infrastructure for:
        • Helping to meet standards for data privacy and requirements for regulatory compliance.
        • Various security scenarios, such as monitoring (auditing) access to sensitive data.
        • Controlling access to and hardening the security of databases that contain highly sensitive data.
        Reference:
        https://docs.microsoft.com/en-us/azure/azure-sql/database/data-discovery-and-classification-overview'''
        },
        {
            'question': 'You have a data warehouse in Azure Synapse Analytics. You need to ensure that the data in the data warehouse is encrypted at rest. What should you enable?',
            'choices': [
                'Advanced Data Security for this database',
                'Transparent Data Encryption (TDE)',
                'Secure transfer required',
                'Dynamic Data Masking'
            ],
            'answer': 'Transparent Data Encryption (TDE)',
            'explanation': '''Azure SQL Database currently supports encryption at rest for Microsoft-managed service side and client side encryption scenarios.
        • Support for server encryption is currently provided through the SQL feature called
        Transparent Data Encryption.
        Client-side encryption of Azure SQL Database data is supported through the
        Always Encrypted feature.
        Reference:
        https://docs.microsoft.com/en-us/azure/security/fundamentals/encryption-atrest'''
        },
        {
            'question': 'You have an Azure Synapse Analytics Apache Spark pool named Pool. You plan to load JSON files from an Azure Data Lake Storage Gen2 container into the tables in Pool1. The structure and data types vary by file. You need to load the files into the tables. The solution must maintain the source data types. What should you do?',
            'choices': [
                'Use a Conditional Split transformation in an Azure Synapse data flow.',
                'Use a Get Metadata activity in Azure Data Factory.',
                'Load the data by using the OPENROWSET Transact-SQL command in an Azure Synapse Analytics serverless SQL pool.',
                'Load the data by using PySpark.'
            ],
            'answer': 'Load the data by using PySpark.',
            'explanation': '''Load the data by using PySpark.
        when you create native parquet tables in spark they are automatically available in serverless sql pools as tables.
        Reference:
        https://docs.microsoft.com/en-us/azure/synapse-analvtics/spark/apache-spark-develo
        pment-using-notebooks?tabs=classical#set-a-primary-lanquage'''
        },
        {
            'question': 'You have an Azure Databricks workspace named workspace1 in the Standard pricing tier. Workspace1 contains an all-purpose cluster named cluster1. You need to reduce the time it takes for cluster1 to start and scale up. The solution must minimize costs. What should you do first?',
            'choices': [
                'Configure a global init script for workspace.',
                'Create a cluster policy in workspace1.',
                'Upgrade workspacel to the Premium pricing tier.',
                'Create a pool in workspace1.'
            ],
            'answer': 'Create a pool in workspace1.',
            'explanation': '''You can use Databricks Pools to Speed up your Data Pipelines and Scale Clusters Quickly. Databricks Pools, a managed cache of virtual machine instances that enables clusters to start and scale 4 times faster.'''
        },
        {
            'question': 'You have an Azure subscription that contains an Azure Blob Storage account named storage1 and an Azure Synapse Analytics dedicated SQL pool named Pooll. You need to store data in storage. The data will be read by Pool. The solution must meet the following requirements: Enable Pool1 to skip columns and rows that are unnecessary in a query. Automatically create column statistics. Minimize the size of files. Which type of file should you use?',
            'choices': ['JSON', 'Parquet', 'Avro', 'CSV'],
            'answer': 'Parquet',
            'explanation': '''Correct Answer: Parquet
            Automatic creation of statistics is turned on for Parquet files. For CSV files, you need to create statistics manually until automatic creation of CSV files statistics is supported.
            Reference:
            https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/develop-tables-statistic'''
        },
        {
            'question': 'You have an Azure Synapse Analytics dedicated SQL pool that contains a table named Table1. You have files that are ingested and loaded into an Azure Data Lake Storage Gen2 container named container1. You plan to insert data from the files in container1 into Table1 and transform the data. Each row of data in the files will produce one row in the serving layer of Table1. You need to ensure that when the source data files are loaded to container1, the DateTime is stored as an additional column in Table1. Solution: In an Azure Synapse Analytics pipeline, you use a Get Metadata activity that retrieves the DateTime of the files. Does this meet the goal?',
            'choices': ['Yes', 'No'],
            'answer': 'Yes',
            'explanation': '''Correct Answer: Yes
            Get Metadata can be used to retrieve the DateTime of the files and allow you to use this data. The question is to add it to Table1, not to an external table.
            Reference:
            https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/create-use-external-tables'''
        },
        {
            'question': 'You have an Azure Data Lake Storage account that contains a staging zone. You need to design a daily process to ingest incremental data from the staging zone, transform the data by executing an R script, and then insert the transformed data into a data warehouse in Azure Synapse Analytics. Solution: You use an Azure Data Factory schedule trigger to execute a pipeline that executes an Azure Databricks notebook, and then inserts the data into the data warehouse. Does this meet the goal?',
            'choices': ['Yes', 'No'],
            'answer': 'No',
            'explanation': '''Correct Answer: No
            If you need to transform data in a way that is not supported by Data Factory, you can create a custom activity, not an Azure Databricks notebook, with your own data processing logic and use the activity in the pipeline. You can create a custom activity to run R scripts on your HDInsight cluster with R installed.
            Reference:
            https://docs.microsoft.com/en-US/azure/data-factory/transform-data'''
        },
        {
            'question': 'You have an Azure Data Lake Storage account that contains a staging zone. You need to design a daily process to ingest incremental data from the staging zone, transform the data by executing an R script, and then insert the transformed data into a data warehouse in Azure Synapse Analytics. Solution: You use an Azure Data Factory schedule trigger to execute a pipeline that executes mapping data flow, and then inserts the data into the data warehouse. Does this meet the goal?',
            'choices': ['Yes', 'No'],
            'answer': 'No',
            'explanation': '''Correct Answer: No
            If you need to transform data in a way that is not supported by Data Factory, you can create a custom activity, not a mapping data flow, with your own data processing logic and use the activity in the pipeline. You can create a custom activity to run R scripts on your HDInsight cluster with R installed.
            Reference:
            https://docs.microsoft.com/en-US/azure/data-factory/transform-data'''
        },
        {
            'question': 'You have an Azure Data Lake Storage account that contains a staging zone. You need to design a daily process to ingest incremental data from the staging zone, transform the data by executing an R script, and then insert the transformed data into a data warehouse in Azure Synapse Analytics. Solution: You schedule an Azure Databricks job that executes an R notebook, and then inserts the data into the data warehouse. Does this meet the goal?',
            'choices': ['Yes', 'No'],
            'answer': 'Yes',
            'explanation': '''Correct Answer: Yes
            You can execute R code in a notebook, and then call it from a Databricks job.
            Reference:
            https://docs.microsoft.com/en-us/azure/databricks/jobs#--run-a-job'''
        },
        {
            'question': 'You plan to create an Azure Data Factory pipeline that will include a mapping data flow. You have JSON data containing objects that have nested arrays. You need to transform the JSON-formatted data into a tabular dataset. The dataset must have one row for each item in the arrays. Which transformation method should you use in the mapping data flow?',
            'choices': ['new branch', 'unpivot', 'alter row', 'flatten'],
            'answer': 'flatten',
            'explanation': '''Correct Answer: D
            Use the flatten transformation to take array values inside hierarchical structures such as JSON and unroll them into individual rows. This process is known as denormalization.
            Reference:
            https://docs.microsoft.com/en-us/azure/data-factory/data-flow-flatten'''
        },
        {
            'question': 'You have an Azure Data Lake Storage Gen2 account named ads2 that is protected by a virtual network. You are designing a SQL pool in Azure Synapse that will use ads2 as a source. What should you use to authenticate to adls2?',
            'choices': ['an Azure Active Directory (Azure AD) user', 'a shared key', 'a shared access signature (SAS)', 'a managed identity'],
            'answer': 'a managed identity',
            'explanation': '''Suggested Answer: D
            Managed Identity authentication is required when your storage account is attached to a VNet.
            Reference:
            https://docs.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/quickstart-bulk-load-copy-tsql-examples'''
        },
        {
            'question': "You have a table in an Azure Synapse Analytics dedicated SQL pool. The table was created by using the following Transact SQL statement. You need to alter the table to meet the following requirements: • Ensure that users can identify the current manager of employees. • Support creating an employee reporting hierarchy for your entire company. • Provide fast lookup of the managers' attributes such as name and job title. Which column should you add to the table?",
            'choices': ['[ManagerEmployee|D] [smallint] NULL', '[ManagerEmployeeKey] [smallint] NULL', '[ManagerEmployeeKey] [int] NULL', '[ManagerName] (varchar](200) NULL'],
            'answer': '[ManagerEmployeeKey] [int] NULL',
            'explanation': '''Correct Answer: C
            We need an extra column to identify the Manager. Use the data type as the EmployeeKey column, an int column.
            Reference:
            https://docs.microsoft.com/en-us/analysis-services/tabular-models/hierarchies-ssas-tabular''',
            'image': 'static/images/image_question_23.jpg'  # Path to the image file
        },
        {
            'question': "You are designing the folder structure for an Azure Data Lake Storage Gen2 container. Users will query data by using a variety of services including Azure Databricks and Azure Synapse Analytics serverless SQL pools. The data will be secured by subject area. Most queries will include data from the current year or current month. Which folder structure should you recommend to support fast queries and simplified folder security?",
            'choices': [
                '/SubjectArea/DataSource/DD/MM/YYYY/FileData_YYYY_MM_DD.c',
                '/DD/MM/YYYY/SubjectArea/DataSourcel/FileData-YYYY_MM_DD.c',
                '/YYYY/(MMY/DD/SubjectArea/DataSource/FileData_YYYY_MM_DD.C',
                '/SubjectArea/DataSource/YYYY/MM/DD/FileData-YYVY_MM_DD.c'
            ],
            'answer': '/SubjectArea/DataSource/YYYY/MM/DD/FileData-YYVY_MM_DD.c',
            'explanation': '''Correct Answer: D
            There's an important reason to put the date at the end of the directory structure. If you want to lock down certain regions or subject matters to users/groups, then you can easily do so with the POSIX permissions. Otherwise, if there was a need to restrict a certain security group to viewing just the UK data or certain planes, with the date structure in front a separate permission would be required for numerous directories under every hour directory. Additionally, having the date structure in front would exponentially increase the number of directories as time went on.
            Note: In IoT workloads, there can be a great deal of data being landed in the data store that spans across numerous products, devices, organizations, and customers. It's important to pre-plan the directory layout for organization, security, and efficient processing of the data for down-stream consumers.
            Reference: https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-best-practice#batch-jobs-structure'''
        },
        {
            'question': 'You have an Azure Data Lake Storage Gen2 container that contains 100 TB of data. You need to ensure that the data in the container is available for read workloads in a secondary region if an outage occurs in the primary region. The solution must minimize costs. Which type of data redundancy should you use?',
            'choices': [
                'geo-redundant storage (GRS)',
                'read-access geo-redundant storage (RA-GRS)',
                'zone-redundant storage (ZRS)',
                'locally-redundant storage (LRS)'
            ],
            'answer': 'geo-redundant storage (GRS)',
            'explanation': '''Correct Answer: A
            GRS is cheaper than RA-GRS. GRS read access is available ONLY once primary region failover occurs (therefore lower cost). The requirement is for read-access availability in the secondary region at lower cost WHEN a failover occurs in the primary.
            Reference:
            https://docs.microsoft.com/en-us/azure/storage/common/storage-redundancy
            https://azure.microsoft.com/en-gb/pricing/details/storage/blobs/'''
        },
        {
            'question': 'You have an Azure Storage account that contains 100 GB of files. The files contain rows of text and numerical values. 75% of the rows contain description data that has an average length of 1.1 MB. You plan to copy the data from the storage account to an enterprise data warehouse in Azure Synapse Analytics. You need to prepare the files to ensure that the data copies quickly. Solution: You copy the files to a table that has a columnstore index. Does this meet the goal?',
            'choices': ['Yes', 'No'],
            'answer': 'No',
            'explanation': '''Correct Answer: B
            Instead, convert the files to compressed delimited text files.
            Reference:
            https://docs.microsoft.com/en-us/azure/sql-data-warehouse/guidance-for-loading-data'''
        },
        {
            'question': 'You have an Azure Storage account that contains 100 GB of files. The files contain rows of text and numerical values. 75% of the rows contain description data that has an average length of 1.1 MB. You plan to copy the data from the storage account to an enterprise data warehouse in Azure Synapse Analytics. You need to prepare the files to ensure that the data copies quickly. Solution: You modify the files to ensure that each row is more than 1 MB. Does this meet the goal?',
            'choices': ['Yes', 'No'],
            'answer': 'No',
            'explanation': '''Correct Answer: B
            Instead, convert the files to compressed delimited text files.
            Reference:
            https://docs.microsoft.com/en-us/azure/sql-data-warehouse/guidance-for-loading-data'''
        },
        {
            'question': 'You build a data warehouse in an Azure Synapse Analytics dedicated SQL pool. Analysts write a complex SELECT query that contains multiple JOIN and CASE statements to transform data for use in inventory reports. The inventory reports will use the data and additional WHERE parameters depending on the report. The reports will be produced once daily. You need to implement a solution to make the dataset available for the reports. The solution must minimize query times.',
            'choices': [
                'an ordered clustered columnstore index',
                'a materialized view',
                'result set caching',
                'a replicated table'
            ],
            'answer': 'a materialized view',
            'explanation': '''Correct Answer: B
            Materialized views for dedicated SQL pools in Azure Synapse provide a low maintenance method for complex analytical queries to get fast performance without any query change.
            Incorrect Answers:
            C: One daily execution does not make use of result set caching.
            Note: When result set caching is enabled, dedicated SQL pool automatically caches query results in the user database for repetitive use. This allows subsequent query executions to get results directly from the persisted cache so recomputation is not needed. Result set caching improves query performance and reduces compute resource usage. In addition, queries using cached results set do not use any concurrency slots and thus do not count against existing concurrency limits.
            Reference:
            https://docs.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/performance-tuning-materialized-views
            https://docs.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/performance-tuning-result-set-caching'''
        },
        {
            'question': 'You are planning a solution to aggregate streaming data that originates in Apache Kafka and is output to Azure Data Lake Storage Gen2. The developers who will implement the stream processing solution use Java. Which service should you recommend using to process the streaming data?',
            'choices': [
                'Azure Event Hubs',
                'Azure Data Factory',
                'Azure Stream Analytics',
                'Azure Databricks'
            ],
            'answer': 'Azure Databricks',
            'explanation': '''Correct Answer: D
            Databricks has many capabilities for stream processing with Java solutions.'''
        },
        {
            'question': 'You plan to implement an Azure Data Lake Storage Gen2 container that will contain CSV files. The size of the files will vary based on the number of events that occur per hour. File sizes range from 4 KB to 5 GB. You need to ensure that the files stored in the container are optimized for batch processing.',
            'choices': [
                'Convert the files to JSON',
                'Convert the files to Avro',
                'Compress the files',
                'Merge the files'
            ],
            'answer': 'Merge the files',
            'explanation': '''Correct Answer: D
            If you store your data as many small files, this can negatively affect performance. In general, organize your data into larger sized files for better performance (256 MB to 100 GB in size).
            Reference:
            https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-best-practice#optimize-for-data-ingest
            https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-best-practices#file-size'''
        },
        {
            'question': 'You are designing a financial transactions table in an Azure Synapse Analytics dedicated SQL pool. The table will have a clustered columnstore index and will include the following columns: • TransactionType: 40 million rows per transaction type • CustomerSegment: 4 million per customer segment • TransactionMonth: 65 million rows per month AccountType: 500 million per account type You have the following query requirements: • Analysts will most commonly analyze transactions for a given month. • Transactions analysis will typically summarize transactions by transaction type, customer segment, and/or account type. You need to recommend a partition strategy for the table to minimize query times. On which column should you recommend partitioning the table?',
            'choices': [
                'CustomerSegment',
                'AccountType',
                'TransactionType',
                'TransactionMonth'
            ],
            'answer': 'TransactionMonth',
            'explanation': '''Correct Answer: D
            For optimal compression and performance of clustered columnstore tables, a minimum of 1 million rows per distribution and partition is needed. Before partitions are created, dedicated SQL pool already divides each table into 60 distributed databases.
            Example: Any partitioning added to a table is in addition to the distributions created behind the scenes. Using this example, if the sales fact table contained 36 monthly partitions, and given that a dedicated SQL pool has 60 distributions, then the sales fact table should contain 60 million rows per month, or 2.1 billion rows when all months are populated. If a table contains fewer than the recommended minimum number of rows per partition, consider using fewer partitions in order to increase the number of rows per partition.'''
        },
        {
            'question': 'You plan to ingest streaming social media data by using Azure Stream Analytics. The data will be stored in files in Azure Data Lake Storage, and then consumed by using Azure Databricks and PolyBase in Azure Synapse Analytics. You need to recommend a Stream Analytics data output format to ensure that the queries from Databricks and PolyBase against the files encounter the fewest possible errors. The solution must ensure that the files can be queried quickly and that the data type information is retained.',
            'choices': ['JSON', 'Parquet', 'CSV', 'Avro'],
            'answer': 'Parquet',
            'explanation': '''Correct Answer: B
            Need Parquet to support both Databricks and PolyBase.
            Reference:
            https://docs.microsoft.com/en-us/sql/t-sql/statements/create-external-file-format-transact-sql'''
        },
        {
            'question': 'You have an Azure Synapse Analytics dedicated SQL pool named Pool1. Pool1 contains a partitioned fact table named do. Sales and a staging table named st.Sales that has the matching table and partition definitions. You need to overwrite the content of the first partition in do.Sales with the content of the same partition in st.Sales. The solution must minimize load times.',
            'choices': [
                'Insert the data from st.Sales into do.Sales.',
                'Switch the first partition from do.Sales to stg.Sales.',
                'Switch the first partition from stg.Sales to dbo.Sales.',
                'Update do.Sales from stg.Sales.'
            ],
            'answer': 'Switch the first partition from stg.Sales to dbo.Sales.',
            'explanation': '''Correct Answer: C
            Stg.sales is a temp table which does not have any partition.
            Reference:
            https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/best-practices-dedicated-sql-pool'''
        },
        {
            'question': 'You are designing a partition strategy for a fact table in an Azure Synapse Analytics dedicated SQL pool. The table has the following specifications: • Contain sales data for 20,000 products. Use hash distribution on a column named ProductID. • Contain 2.4 billion records for the years 2019 and 2020. Which number of partition ranges provides optimal compression and performance for the clustered columnstore index?',
            'choices': ['40', '240', '400', '2,400'],
            'answer': '40',
            'explanation': '''Correct Answer: A
            Each partition should have around 1 million records. Dedicated SQL pools already have 60 partitions.
            We have the formula: Records/(Partitions*60= 1 million
            Partitions= Records/(1 million * 60)
            Partitions= 2.4 x 1,000,000,000/(1,000,000 * 60) = 40
            Note: Having too many partitions can reduce the effectiveness of clustered columnstore indexes if each partition has fewer than 1 million rows. Dedicated SQL pools automatically partition your data into 60 databases. So, if you create a table with 100 partitions, the result will be 6000 partitions.
            Reference:
            https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/best-practices-dedicated-sql-pool'''
        },
        {
            'question': 'You are implementing a batch dataset in the Parquet format. Data files will be produced by using Azure Data Factory and stored in Azure Data Lake Storage Gen2. The files will be consumed by an Azure Synapse Analytics serverless SQL pool. You need to minimize storage costs for the solution.',
            'choices': [
                'Use Snappy compression for files',
                'Use OPENROWSET to query the Parquet files.',
                'Create an external table that contains a subset of columns from the Parquet files.',
                'Store all data as a string in the Parquet files.'
            ],
            'answer': 'Use Snappy compression for files',
            'explanation': '''Correct Answer: A
            This talks about minimizing storage costs, not querying costs. Creating an external table with fewer columns than the file has no effect on the file itself and will actually fail, so in no way helps with storage costs.
            Reference:
            https://docs.microsoft.com/en-us/azure/data-factory/format-parquet#dataset-properties'''
        },
        {
            'question': 'You are designing a dimension table for a data warehouse. The table will track the value of the dimension attributes over time and preserve the history of the data by adding new rows as the data changes. Which type of slowly changing dimension (SCD) should you use?',
            'choices': ['Type 0', 'Type 1', 'Type 2', 'Type 3'],
            'answer': 'Type 2',
            'explanation': '''Correct Answer: C
            A Type 2 SCD supports versioning of dimension members. Often the source system doesn't store versions, so the data warehouse load process detects and manages changes in a dimension table. In this case, the dimension table must use a surrogate key to provide a unique reference to a version of the dimension member. It also includes columns that define the date range validity of the version (for example, StartDate and EndDate) and possibly a flag column (for example, IsCurrent) to easily filter by current dimension members.
            Reference:
            https://docs.microsoft.com/en-us/learn/modules/populate-slowly-changing-dimensions-azure-synapse-analytics-pipelines/3-choose-between-dimension-types'''
        },
        {
            'question': 'You plan to create an Azure Databricks workspace that has a tiered structure. The workspace will contain the following three workloads: • A workload for data engineers who will use Python and SQL. • A workload for jobs that will run notebooks that use Python, Scala, and SQL. • A workload that data scientists will use to perform ad hoc analysis in Scala and R. The enterprise architecture team at your company identifies the following standards for Databricks environments: • The data engineers must share a cluster. • The job cluster will be managed by using a request process whereby data scientists and data engineers provide packaged notebooks for deployment to the cluster. • All the data scientists must be assigned their own cluster that terminates automatically after 120 minutes of inactivity. Currently, there are three data scientists. You need to create the Databricks clusters for the workloads. Solution: You create a Standard cluster for each data scientist, a High Concurrency cluster for the data engineers, and a Standard cluster for the jobs. Does this meet the goal?',
            'choices': ['A. Yes', 'B. No'],
            'answer': 'A. Yes',
            'explanation': '''Explanation: This solution aligns with the specified requirements:
            - High Concurrency cluster for data engineers to enable sharing.
            - Standard clusters for each data scientist, set to automatically terminate after 120 minutes of inactivity.
            - A Standard cluster for jobs, managed through a request process for notebook deployment.
            Therefore, the correct answer is "A. Yes."
            '''
        },
        {
            'question': 'You plan to create an Azure Databricks workspace that has a tiered structure. The workspace will contain the following three workloads: • A workload for data engineers who will use Python and SQL. • A workload for jobs that will run notebooks that use Python, Scala, and SQL. A workload that data scientists will use to perform ad hoc analysis in Scala and R. The enterprise architecture team at your company identifies the following standards for Databricks environments: • The data engineers must share a cluster. • The job cluster will be managed by using a request process whereby data scientists and data engineers provide packaged notebooks for deployment to the cluster. • All the data scientists must be assigned their own cluster that terminates automatically after 120 minutes of inactivity. Currently, there are three data scientists. You need to create the Databricks clusters for the workloads. Solution: You create a Standard cluster for each data scientist, a High Concurrency cluster for the data engineers, and a High Concurrency cluster for the jobs. Does this meet the goal?',
            'choices': ['A. Yes', 'B. No'],
            'answer': 'B. No',
            'explanation': '''Explanation: The proposed solution does not meet the goal because high-concurrency clusters do not support Scala. Since the workload for jobs requires notebooks with Scala, Python, and SQL, high-concurrency clusters are not suitable for this purpose. Therefore, the correct answer is "B. No."
            Reference: https://docs.microsoft.com/en-us/azure/databricks/clusters/configure'''
        }

]