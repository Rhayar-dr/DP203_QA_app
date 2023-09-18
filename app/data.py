
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
        },
        {
            'question': 'You are designing a statistical analysis solution that will use custom proprietary Python functions on near real-time data from Azure Event Hubs. You need to recommend which Azure service to use to perform the statistical analysis. The solution must minimize latency. What should you recommend?',
            'choices': ['A. Azure Synapse Analytics', 'B. Azure Databricks', 'C. Azure Stream Analytics', 'D. Azure SQL Database'],
            'answer': 'B. Azure Databricks',
            'explanation': '''Explanation: Azure Databricks is the recommended Azure service for performing statistical analysis on near real-time data from Azure Event Hubs while minimizing latency. Azure Databricks provides support for custom proprietary Python functions and is designed to handle real-time and big data workloads.
            Reference: https://stackoverflow.com/questions/58097539/execute-azure-streaming-analytics-queries-from-a-python-script'''
        },
            {
            'question': 'You are designing an Azure Stream Analytics solution that will analyze Twitter data. You need to count the tweets in each 10-second window. The solution must ensure that each tweet is counted only once. Solution: You use a hopping window that uses a hop size of 10 seconds and a window size of 10 seconds. Does this meet the goal?',
            'choices': ['A. Yes', 'B. No'],
            'answer': 'A. Yes',
            'explanation': '''Explanation: Correct Answer: A
    To make a Hopping window the same as a Tumbling window, specify the hop size to be the same as the window size.
    a hop size of 10 seconds and a window size of 10 seconds.
    Reference: https://docs.microsoft.com/en-us/azure/stream-analvtics/stream-analytics-window-fun
    ctions#hopping-window'''
        },
        {
            'question': 'You are designing an Azure Stream Analytics solution that will analyze Twitter data. You need to count the tweets in each 10-second window. The solution must ensure that each tweet is counted only once. Solution: You use a hopping window that uses a hop size of 5 seconds and a window size 10 seconds. Does this meet the goal?',
            'choices': ['A. Yes', 'B. No'],
            'answer': 'B. No',
            'explanation': '''Explanation: Correct Answer: B
    Instead use a tumbling window. Tumbling windows are a series of fixed-sized, non-overlapping and contiguous time intervals.
    Reference: https://docs.microsoft.com/en-us/stream-analytics-query/tumbling-window-azure-strea
    m-analvtics'''
        },
        {
            'question': 'You are designing an Azure Databricks table. The table will ingest an average of 20 million streaming events per day. You need to persist the events in the table for use in incremental load pipeline jobs in Azure Databricks. The solution must minimize storage costs and incremental load times. What should you include in the solution?',
            'choices': [
                'A. Partition by DateTime fields.', 
                'B. Sink to Azure Queue storage.', 
                'C. Include a watermark column.', 
                'D. Use a JSON format for physical data storage.'
            ],
            'answer': 'B. Sink to Azure Queue storage.',
            'explanation': '''Explanation: Correct Answer: B
    The Databricks ABS-AQS connector uses Azure Queue Storage (AQS) to provide an optimized file source that lets you find new files written to an Azure Blob storage (ABS) container without repeatedly listing all of the files. This provides two major advantages:
    • Lower latency: no need to list nested directory structures on ABS, which is slow and resource intensive.
    • Lower costs: no more costly LIST API requests made to ABS.
    Reference: https://docs.microsoft.com/en-us/azure/databricks/spark/latest/structured-streaming/ads'''
        },
        {
            'question': 'You have an Azure Databricks workspace named workspace1 in the Standard pricing tier. You need to configure workspace1 to support autoscaling all-purpose clusters. The solution must meet the following requirements:\n• Automatically scale down workers when the cluster is underutilized for three minutes.\n• Minimize the time it takes to scale to the maximum number of workers.\n• Minimize costs.\nWhat should you do first?',
            'choices': [
                'A. Enable container services for workspace1.', 
                'B. Upgrade workspace1 to the Premium pricing tier.', 
                'C. Set Cluster Mode to High Concurrency', 
                'D. Create a cluster policy in workspace1.'
            ],
            'answer': 'B. Upgrade workspace1 to the Premium pricing tier.',
            'explanation': '''Explanation: Correct Answer: B
    Automated (job) clusters always use optimized autoscaling. The type of autoscaling performed on all-purpose clusters depends on the workspace configuration.
    Standard autoscaling is used by all-purpose clusters in workspaces in the Standard pricing tier. Optimized autoscaling is used by all-purpose clusters in the Azure Databricks Premium Plan.
    Reference: https://docs.databricks.com/clusters/cluster-config-best-practices.html'''
        },
        {
            'question': 'You are designing an Azure Stream Analytics solution that will analyze Twitter data. You need to count the tweets in each 10-second window. The solution must ensure that each tweet is counted only once. Solution: You use a session window that uses a timeout size of 10 seconds. Does this meet the goal?',
            'choices': ['A. Yes', 'B. No'],
            'answer': 'B. No',
            'explanation': '''Explanation: Correct Answer: B
    Instead use a tumbling window. Tumbling windows are a series of fixed-sized, non-overlapping and contiguous time intervals.
    Reference: https://docs.microsoft.com/en-us/stream-analytics-query/tumbling-window-azure-strea
    m-analytics'''
        },
        {
            'question': 'You use Azure Stream Analytics to receive data from Azure Event Hubs and to output the data to an Azure Blob Storage account. You need to output the count of records received from the last five minutes every minute. Which windowing function should you use?',
            'choices': [
                'A. Session', 
                'B. Tumbling', 
                'C. Sliding', 
                'D. Hopping'
            ],
            'answer': 'D. Hopping',
            'explanation': '''Explanation: Correct Answer: D
    Hopping window functions hop forward in time by a fixed period. It may be easy to think of them as Tumbling windows that can overlap and be emitted more often than the window size. Events can belong to more than one Hopping window result set. To make a Hopping window the same as a Tumbling window, specify the hop size to be the same as the window size.'''
        },
        {
            'question': 'You plan to create an Azure Databricks workspace that has a tiered structure. The workspace will contain the following three workloads:\n• A workload for data engineers who will use Python and SQL\n• A workload for jobs that will run notebooks that use Python, Scala, and SQL.\n• A workload that data scientists will use to perform ad hoc analysis in Scala and R.\nThe enterprise architecture team at your company identifies the following standards for Databricks environments:\n• The data engineers must share a cluster.\n• The job cluster will be managed by using a request process whereby data scientists and data engineers provide packaged notebooks for deployment to the cluster.\n• All the data scientists must be assigned their own cluster that terminates automatically after 120 minutes of inactivity. Currently, there are three data scientists.\nYou need to create the Databricks clusters for the workloads.\nSolution: You create a Standard cluster for each data scientist, a Standard cluster for the data engineers, and a High Concurrency cluster for the jobs.\nDoes this meet the goal?',
            'choices': ['A. Yes', 'B. No'],
            'answer': 'B. No',
            'explanation': '''Explanation: Correct Answer: B
    • A workload for data engineers who will use Python and SQL should use a high concurrency cluster.
    • A workload for jobs that will run notebooks that use Python, Scala, and SQL should use a standard cluster.
    • A workload that data scientists will use to perform ad hoc analysis in Scala and R should use a standard cluster because high concurrency does not support Scala.
    Reference: https://stackoverflow.com/questions/65869399/high-concurrency-clusters-in-databricks'''
        },
        {
            'question': 'You have the following Azure Data Factory pipelines:\n• Ingest Data from System1\n• Ingest Data from System2\n• Populate Dimensions\n• Populate Facts\nIngest Data from System1 and Ingest Data from System2 have no dependencies. Populate Dimensions must execute after Ingest Data from System1 and Ingest Data from System2. Populate Facts must execute after Populate Dimensions pipeline. All the pipelines must execute every eight hours.\nWhat should you do to schedule the pipelines for execution?',
            'choices': [
                'A. Add an event trigger to all four pipelines.', 
                'B. Add a schedule trigger to all four pipelines.', 
                'C. Create a parent pipeline that contains the four pipelines and use a schedule trigger.', 
                'D. Create a parent pipeline that contains the four pipelines and use an event trigger.'
            ],
            'answer': 'C. Create a parent pipeline that contains the four pipelines and use a schedule trigger.',
            'explanation': '''Explanation: Correct Answer: C
    The parent pipeline has 4 execute pipeline activities. Ingest 1 and Ingest 2 have no dependencies. Dimension pipeline has two dependencies from 'on completion' outputs of both Ingest 1 and Ingest 2 pipelines. Fact pipeline has one 'on completion' dependency on the Dimension pipeline. Absolutely nothing to do with a tumbling window trigger.
    Reference: https://docs.microsoft.com/en-us/azure/data-factory/concepts-pipeline-execution-trigger'''
        },
        {
            'question': 'You have an Azure Data Lake Storage account that contains a staging zone. You need to design a daily process to ingest incremental data from the staging zone, transform the data by executing an R script, and then insert the transformed data into a data warehouse in Azure Synapse Analytics. Solution: You use an Azure Data Factory schedule trigger to execute a pipeline that copies the data to a staging table in the data warehouse, and then uses a stored procedure to execute the R script. Does this meet the goal?',
            'choices': ['A. Yes', 'B. No'],
            'answer': 'B. No',
            'explanation': '''Explanation: Correct Answer: B
    you cannot execute the R script using a stored procedure activity in Azure Synapse Analytics. The sp_execute_external_script function can only be applied to SQL Server 2016 (13.x) and later, Azure SQL Managed Instance. R scripts cannot be run in Azure Synapse Analytics.
    Reference: https://docs.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/r-developers-guide'''
        },
        {
            'question': 'You plan to create an Azure Databricks workspace that has a tiered structure. The workspace will contain the following three workloads:\n• A workload for data engineers who will use Python and SQL.\n• A workload for jobs that will run notebooks that use Python, Scala, and SQL.\n• A workload that data scientists will use to perform ad hoc analysis in Scala and R. The enterprise architecture team at your company identifies the following standards for Databricks environments:\n• The data engineers must share a cluster.\n• The job cluster will be managed by using a request process whereby data scientists and data engineers provide packaged notebooks for deployment to the cluster.\n• All the data scientists must be assigned their own cluster that terminates automatically after 120 minutes of inactivity. Currently, there are three data scientists. You need to create the Databricks clusters for the workloads. Solution: You create a High Concurrency cluster for each data scientist, a High Concurrency cluster for the data engineers, and a Standard cluster for the jobs. Does this meet the goal?',
            'choices': ['A. Yes', 'B. No'],
            'answer': 'B. No',
            'explanation': '''Explanation: Correct Answer: B
    - Data Engineers: Correct, they are working together, so they need a High-Concurrency cluster.
    - Jobs: Correct, Standard Cluster since it supports SCALA.
    HOWEVER:
    - Data Scientists need a cluster that terminates after 120 minutes automatically. ONLY STANDARD AND SINGLE NODE CLUSTERS CAN SUPPORT THAT.
    SO, the correct answer is NO.
    Reference: https://docs.azuredatabricks.net/clusters/configure.html'''
        },
        {
            'question': 'You are designing an Azure Databricks cluster that runs user-defined local processes. You need to recommend a cluster configuration that meets the following requirements:\n• Minimize query latency.\n• Maximize the number of users that can run queries on the cluster at the same time.\n• Reduce overall costs without compromising other requirements. Which cluster type should you recommend?',
            'choices': [
                'A. Standard with Auto Termination',
                'B. High Concurrency with Autoscaling',
                'C. High Concurrency with Auto Termination',
                'D. Standard with Autoscaling'
            ],
            'answer': 'B. High Concurrency with Autoscaling',
            'explanation': '''Explanation: Correct Answer: B
    A High Concurrency cluster is a managed cloud resource. The key benefits of High Concurrency clusters are that they provide fine-grained sharing for maximum resource utilization and minimum query latencies.
    Databricks chooses the appropriate number of workers required to run your job. This is referred to as autoscaling. Autoscaling makes it easier to achieve high cluster utilization, because you don't need to provision the cluster to match a workload.
    Incorrect Answers:
    C: The cluster configuration includes an auto terminate setting whose default value depends on cluster mode:
    Standard and Single Node clusters terminate automatically after 120 minutes by default.
    High Concurrency clusters do not terminate automatically by default.
    Reference: https://docs.microsoft.com/en-us/azure/databricks/clusters/configure'''
        },
        {
            'question': 'You are creating a new notebook in Azure Databricks that will support R as the primary language but will also support Scala and SQL. Which switch should you use to switch between languages?',
            'choices': [
                'A. %<language>',
                'B. @<Language>',
                'C. I<language>',
                'D. IN(<language>'
            ],
            'answer': 'A. %<language>',
            'explanation': '''Explanation: Correct Answer: A
    To change the language in Databricks cells to either Scala, SQL, Python or R, prefix the cell with followed by the language.
    %python //or r, scala, sql
    Reference: https://www.theta.co.nz/news-blogs/tech-blog/enhancing-digital-twins-part-3-predictive-maintenance-with-azure-databricks'''
        },
        {
            'question': 'You have an Azure Data Factory pipeline that performs an incremental load of source data to an Azure Data Lake Storage Gen2 account. Data to be loaded is identified by a column named LastUpdatedDate in the source table. You plan to execute the pipeline every four hours. You need to ensure that the pipeline execution meets the following requirements:\n• Automatically retries the execution when the pipeline run fails due to concurrency or throttling limits.\n• Supports backfilling existing data in the table. Which type of trigger should you use?',
            'choices': [
                'A. event',
                'B. on-demand',
                'C. schedule',
                'D. tumbling window'
            ],
            'answer': 'D. tumbling window',
            'explanation': '''Explanation: Correct Answer: D
    In case of pipeline failures, tumbling window trigger can retry the execution of the referenced pipeline automatically, using the same input parameters, without the user intervention. This can be specified using the property "retryPolicy" in the trigger definition.
    Reference: https://docs.microsoft.com/en-us/azure/data-factory/how-to-create-tumbling-window-trigger'''
        },
        {
            'question': 'You have an Azure Synapse Analytics dedicated SQL pool that contains a table named Table1. You have files that are ingested and loaded into an Azure Data Lake Storage Gen2 container named container1. You plan to insert data from the files in container1 into Table1 and transform the data. Each row of data in the files will produce one row in the serving layer of Table1. You need to ensure that when the source data files are loaded to container1, the DateTime is stored as an additional column in Table1. Solution: In an Azure Synapse Analytics pipeline, you use a data flow that contains a Derived Column transformation. Does this meet the goal?',
            'choices': [
                'A. Yes',
                'B. No'
            ],
            'answer': 'A. Yes',
            'explanation': '''Explanation: Correct Answer: A
    "Data flows are available both in Azure Data Factory and Azure Synapse Pipelines"
    "Use the derived column transformation to generate new columns in your data flow or to modify existing fields.
    Reference: https://docs.microsoft.com/en-us/azure/data-factory/data-flow-derived-column'''
        },
        {
            'question': 'You have an Azure Synapse Analytics dedicated SQL pool that contains a table named Table1. You have files that are ingested and loaded into an Azure Data Lake Storage Gen2 container named container1. You plan to insert data from the files in container1 into Table1 and transform the data. Each row of data in the files will produce one row in the serving layer of Table1. You need to ensure that when the source data files are loaded to container1, the DateTime is stored as an additional column in Table1. Solution: You use a dedicated SQL pool to create an external table that has an additional DateTime column. Does this meet the goal?',
            'choices': [
                'A. Yes',
                'B. No'
            ],
            'answer': 'B. No',
            'explanation': '''Explanation: Correct Answer: B
    An external table is based on a source flat file structure. It seems to make no sense to add additional date time columns to such a table.
    Reference: https://docs.microsoft.com/en-us/azure/data-factory/data-flow-derived-column'''
        },
        {
            'question': 'You have an Azure Synapse Analytics dedicated SQL pool that contains a table named Table1. You have files that are ingested and loaded into an Azure Data Lake Storage Gen2 container named container1. You plan to insert data from the files in container1 into Table1 and transform the data. Each row of data in the files will produce one row in the serving layer of Table1. You need to ensure that when the source data files are loaded to container1, the DateTime is stored as an additional column in Table1. Solution: You use an Azure Synapse Analytics serverless SQL pool to create an external table that has an additional DateTime column. Does this meet the goal?',
            'choices': [
                'A. Yes',
                'B. No'
            ],
            'answer': 'B. No',
            'explanation': '''Explanation: Correct Answer: B
    Instead use the derived column transformation to generate new columns in your data flow or to modify existing fields.
    Reference: https://docs.microsoft.com/en-us/azure/data-factory/data-flow-derived-column'''
        },
        {
            'question': 'You are designing an enterprise data warehouse in Azure Synapse Analytics that will contain a table named Customers. Customers will contain credit card information. You need to recommend a solution to provide salespeople with the ability to view all the entries in Customers. The solution must prevent all the salespeople from viewing or inferring the credit card information. What should you include in the recommendation?',
            'choices': [
                'A. data masking',
                'B. Always Encrypted',
                'C. column-level security',
                'D. row-level security'
            ],
            'answer': 'C. column-level security',
            'explanation': '''Explanation: Correct Answer: C
    Data masking does not protect against inferring with the data.
    Reference: https://docs.microsoft.com/nl-nl/sql/relational-databases/security/dynamic-data-masking?view=sql-server-ver15'''
        },
        {
            'question': 'You are designing a streaming data solution that will ingest variable volumes of data. You need to ensure that you can change the partition count after creation. Which service should you use to ingest the data?',
            'choices': [
                'A. Azure Event Hubs Dedicated',
                'B. Azure Stream Analytics',
                'C. Azure Data Factory',
                'D. Azure Synapse Analytics'
            ],
            'answer': 'A. Azure Event Hubs Dedicated',
            'explanation': '''Explanation: Correct Answer: A
    You can't change the partition count for an event hub after its creation except for the event hub in a dedicated cluster.
    Reference: https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-features'''
        },
        {
            'question': 'You are designing a date dimension table in an Azure Synapse Analytics dedicated SQL pool. The date dimension table will be used by all the fact tables. Which distribution type should you recommend to minimize data movement?',
            'choices': [
                'A. HASH',
                'B. REPLICATE',
                'C. ROUND_ROBIN'
            ],
            'answer': 'B. REPLICATE',
            'explanation': '''Explanation: Correct Answer: B
    A replicated table has a full copy of the table available on every Compute node. Queries run fast on replicated tables since joins on replicated tables don't require data movement. Replication requires extra storage, though, and isn't practical for large tables.
    Incorrect Answers:
    A: A hash distributed table is designed to achieve high performance for queries on large tables.'''
        },
        {
            'question': 'You have a SQL pool in Azure Synapse that contains a table named do.Customers. The table contains a column name Email. You need to prevent nonadministrative users from seeing the full email addresses in the Email column. The users must see values in a format of a XXX@XXXX.com instead. What should you do?',
            'choices': [
                'A. From Microsoft SQL Server Management Studio, set an email mask on the Email column.',
                'B. From the Azure portal, set a mask on the Email column.',
                'C. From Microsoft SQL Server Management Studio, grant the SELECT permission to the users for all the columns in the do. Customers table except Email.',
                'D. From the Azure portal, set a sensitivity classification of Confidential for the Email column.'
            ],
            'answer': 'A. From Microsoft SQL Server Management Studio, set an email mask on the Email column.',
            'explanation': '''Explanation: Correct Answer: A
    The Email masking method, which exposes the first letter and replaces the domain with XXX.com using a constant string prefix in the form of an email address.
    axX@XXXX.com
    Reference: https://docs.microsoft.com/en-us/azure/azure-sql/database/dynamic-data-masking-ov
    erview'''
        },
        {
            'question': 'You are designing an Azure Synapse solution that will provide a query interface for the data stored in an Azure Storage account. The storage account is only accessible from a virtual network. You need to recommend an authentication mechanism to ensure that the solution can access the source data. What should you recommend?',
            'choices': [
                'A. a managed identity',
                'B. anonymous public read access',
                'C. a shared key'
            ],
            'answer': 'A. a managed identity',
            'explanation': '''Explanation: Correct Answer: A
    Managed Identity authentication is required when your storage account is attached to a VNet.
    Reference: https://docs.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/quicks
    tart-bulk-load-copy-tsql-examples'''
        },
        {
            'question': 'You are developing an application that uses Azure Data Lake Storage Gen2. You need to recommend a solution to grant permissions to a specific application for a limited time period. What should you include in the recommendation?',
            'choices': [
                'A. role assignments',
                'B. shared access signatures (SAS)',
                'C. Azure Active Directory (Azure AD) identities',
                'D. account keys'
            ],
            'answer': 'B. shared access signatures (SAS)',
            'explanation': '''Explanation: Correct Answer: B
    A shared access signature (SAS) provides secure delegated access to resources in your storage account. With a SAS, you have granular control over how a client can access your data. For example:
    What resources the client may access.
    What permissions they have to those resources.
    How long the SAS is valid.
    Reference: https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview'''
        },
        {
            'question': 'You have an Azure Synapse Analytics dedicated SQL pool that contains a table named Contacts. Contacts contains a column named Phone. You need to ensure that users in a specific role only see the last four digits of a phone number when querying the Phone column. What should you include in the solution?',
            'choices': [
                'A. table partitions',
                'B. a default value',
                'C. row-level security (RLS)',
                'D. column encryption',
                'E. dynamic data masking'
            ],
            'answer': 'E. dynamic data masking',
            'explanation': '''Explanation: Correct Answer: E
    Dynamic data masking helps prevent unauthorized access to sensitive data by enabling customers to designate how much of the sensitive data to reveal with minimal impact on the application layer. It’s a policy-based security feature that hides the sensitive data in the result set of a query over designated database fields, while the data in the database is not changed.
    Reference: https://docs.microsoft.com/en-us/azure/azure-sql/database/dynamic-data-masking-overview'''
        },
        {
            'question': 'A company purchases loT devices to monitor manufacturing machinery. The company uses an Azure loT Hub to communicate with the loT devices. The company must be able to monitor the devices in real-time. You need to design the solution. What should you recommend?',
            'choices': [
                'A. Azure Data Factory instance using Azure Portal',
                'B. Azure Data Factory instance using Azure PowerShell',
                'C. Azure Stream Analytics cloud job using Azure Portal',
                'D. Azure Data Factory instance using Microsoft Visual Studio'
            ],
            'answer': 'C. Azure Stream Analytics cloud job using Azure Portal',
            'explanation': '''Explanation: Correct Answer: C
    In a real-world scenario, you could have hundreds of these sensors generating events as a stream. Ideally, a gateway device would run code to push these events to Azure Event Hubs or Azure loT Hubs. Your Stream Analytics job would ingest these events from Event Hubs and run real-time analytics queries against the streams.
    Create a Stream Analytics job:
    In the Azure portal, select + Create a resource from the left navigation menu. Then, select Stream Analytics job from Analytics.
    Reference: https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-get-started-with-azure-stream-analytics-to-process-data-from-iot-devices'''
        },
        {
            'question': 'You have a partitioned table in an Azure Synapse Analytics dedicated SQL pool. You need to design queries to maximize the benefits of partition elimination. What should you include in the Transact-SQL queries?',
            'choices': [
                'A. JOIN',
                'B. WHERE',
                'C. DISTINCT',
                'D. GROUP BY'
            ],
            'answer': 'B. WHERE',
            'explanation': '''Explanation: Correct Answer: B
    Data partition elimination refers to the database server's ability to determine, based on query predicates. When you add the "WHERE" clause to your T-SQL query it allows the query optimizer accesses only the relevant partitions to satisfy the filter criteria of the query - which is what partition elimination is all about.
    Reference: https://stackoverflow.com/questions/51677471/what-is-a-difference-between-table-distribution-and-table-partition-in-sql/51677595'''
        },
        {
            'question': 'You have an Azure Synapse Analytics dedicated SQL pool that contains a large fact table. The table contains 50 columns and 5 billion rows and is a heap. Most queries against the table aggregate values from approximately 100 million rows and return only two columns. You discover that the queries against the fact table are very slow. Which type of index should you add to provide the fastest query times?',
            'choices': [
                'A. nonclustered columnstore',
                'B. clustered columnstore',
                'C. nonclustered',
                'D. clustered'
            ],
            'answer': 'B. clustered columnstore',
            'explanation': '''Explanation: Correct Answer: B
    Clustered columnstore indexes are one of the most efficient ways you can store your data in dedicated SQL pool. Columnstore tables won't benefit a query unless the table has more than 60 million rows.'''
        },
        {
            'question': 'You create an Azure Databricks cluster and specify an additional library to install. When you attempt to load the library to a notebook, the library is not found. You need to identify the cause of the issue. What should you review?',
            'choices': [
                'A. notebook logs',
                'B. cluster event logs',
                'C. global init scripts logs',
                'D. workspace logs'
            ],
            'answer': 'B. cluster event logs',
            'explanation': '''Explanation: Correct Answer: B
    Azure Databricks provides three kinds of logging of cluster-related activity: 
    - Cluster event logs, which capture cluster lifecycle events, like creation, termination, configuration edits, and so on. 
    - Apache Spark driver and worker logs, which you can use for debugging. 
    - Cluster init-script logs, valuable for debugging init scripts.
    Reference: 
    https://docs.microsoft.com/en-us/azure/databricks/clusters/clusters-manage#event-lo
    g'''
        },
        {
            'question': 'You have an Azure data factory. You need to examine the pipeline failures from the last 60 days. What should you use?',
            'choices': [
                'A. the Activity log blade for the Data Factory resource',
                'B. the Monitor & Manage app in Data Factory',
                'C. the Resource health blade for the Data Factory resource',
                'D. Azure Monitor'
            ],
            'answer': 'D. Azure Monitor',
            'explanation': '''Explanation: Correct Answer: D
    Data Factory stores pipeline-run data for only 45 days. Use Azure Monitor if you want to keep that data for a longer time.
    Reference: 
    https://docs.microsoft.com/en-us/azure/data-factory/monitor-using-azure-monitor'''
        },
        {
            'question': 'You are monitoring an Azure Stream Analytics job. The Backlogged Input Events count has been 20 for the last hour. You need to reduce the Backlogged Input Events count. What should you do?',
            'choices': [
                'A. Drop late arriving events from the job.',
                'B. Add an Azure Storage account to the job.',
                'C. Increase the streaming units for the job.',
                'D. Stop the job.'
            ],
            'answer': 'C. Increase the streaming units for the job.',
            'explanation': '''Explanation: Correct Answer: C
    General symptoms of the job hitting system resource limits include:
    • If the backlog event metric keeps increasing, it's an indicator that the system resource is constrained (either because of output sink throttling, or high CPU).
    Note: Backlogged Input Events: Number of input events that are backlogged. A non-zero value for this metric implies that your job isn't able to keep up with the number of incoming events. If this value is slowly increasing or consistently non-zero, you should scale out your job: adjust Streaming Units.
    Reference: 
    https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-scale-jobs
    https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-monitoring'''
        },
        {
            'question': 'You are designing an Azure Databricks interactive cluster. The cluster will be used infrequently and will be configured for auto-termination. You need to use that the cluster configuration is retained indefinitely after the cluster is terminated. The solution must minimize costs. What should you do?',
            'choices': [
                'A. Pin the cluster.',
                'B. Create an Azure runbook that starts the cluster every 90 days.',
                'C. Terminate the cluster manually when processing completes.',
                'D. Clone the cluster after it is terminated.'
            ],
            'answer': 'A. Pin the cluster.',
            'explanation': '''Explanation: Correct Answer: A
    30 days after a cluster is terminated, it is permanently deleted. To keep an interactive cluster configuration even after a cluster has been terminated for more than 30 days, an administrator can pin the cluster. Up to 20 clusters can be pinned.
    Reference:
    https://docs.databricks.com/clusters/clusters-manage.html#pin-a-cluster
    https://docs.azuredatabricks.net/user-guide/clusters/terminate.html'''
        },
        {
            'question': 'You have an Azure data solution that contains an enterprise data warehouse in Azure Synapse Analytics named DW1. Several users execute ad hoc queries to DW1 concurrently. You regularly perform automated data loads to DW1. You need to ensure that the automated data loads have enough memory available to complete quickly and successfully when the ad hoc queries run. What should you do?',
            'choices': [
                'A. Hash distribute the large fact tables in DW1 before performing the automated data loads.',
                'B. Assign a smaller resource class to the automated data load queries.',
                'C. Assign a larger resource class to the automated data load queries.',
                'D. Create sampled statistics for every column in each table of DW1.'
            ],
            'answer': 'C. Assign a larger resource class to the automated data load queries.',
            'explanation': '''Explanation: Correct Answer: C
    The performance capacity of a query is determined by the user's resource class.
    Resource classes are pre-determined resource limits in Synapse SQL pool that govern compute resources and concurrency for query execution.
    Resource classes can help you configure resources for your queries by setting limits on the number of queries that run concurrently and on the compute-resources assigned to each query. There's a trade-off between memory and concurrency.
    Smaller resource classes reduce the maximum memory per query, but increase concurrency.
    Larger resource classes increase the maximum memory per query, but reduce concurrency.
    Reference:
    https://docs.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/resource-classes-for-workload-management'''
        },
        {
            'question': 'You have an Azure Synapse Analytics dedicated SQL pool named Pool and a database named DB1. DB1 contains a fact table named Table1. You need to identify the extent of the data skew in Table. What should you do in Synapse Studio?',
            'choices': [
                'A. Connect to the built-in pool and run DBCC PDW_SHOWSPACEUSED.',
                'B. Connect to the built-in pool and run DBCC CHECKALLOC.',
                'C. Connect to Pool1 and query sys.dm_pdw_node_status.',
                'D. Connect to Pool1 and query sys.dm_pdw_nodes_db_partition_stats.'
            ],
            'answer': 'D. Connect to Pool1 and query sys.dm_pdw_nodes_db_partition_stats.',
            'explanation': '''Explanation: Correct Answer: D
    Microsoft recommends the use of sys.dm_pdw_nodes_db_partition_stats to analyze any skewness in the data.
    Reference:
    https://docs.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/cheat-sheet'''
        },
        {
            'question': 'You have a SQL pool in Azure Synapse. You discover that some queries fail or take a long time to complete. You need to monitor for transactions that have rolled back. Which dynamic management view should you query?',
            'choices': [
                'A. sys.dm_pdw_request_steps',
                'B. sys.dm_pdw_nodes_tran_database_transactions',
                'C. sys.dm_pdw_waits',
                'D. sys.dm_pdw_exec_sessions'
            ],
            'answer': 'B. sys.dm_pdw_nodes_tran_database_transactions',
            'explanation': '''Explanation: Correct Answer: B
    You can use Dynamic Management Views (DMVs) to monitor your workload including investigating query execution in SQL pool. If your queries are failing or taking a long time to proceed, you can check and monitor if you have any transactions rolling back.
    Reference:
    https://docs.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-manage-monitor#monitor-transaction-log-rollback'''
        },
        {
            'question': 'You are monitoring an Azure Stream Analytics job. You discover that the Backlogged Input Events metric is increasing slowly and is consistently non-zero. You need to ensure that the job can handle all the events. What should you do?',
            'choices': [
                'A. Change the compatibility level of the Stream Analytics job.',
                'B. Increase the number of streaming units (SUs).',
                'C. Remove any named consumer groups from the connection and use default.',
                'D. Create an additional output stream for the existing input stream.'
            ],
            'answer': 'B. Increase the number of streaming units (SUs).',
            'explanation': '''Explanation: Correct Answer: B
    Backlogged Input Events: Number of input events that are backlogged. A non-zero value for this metric implies that your job isn't able to keep up with the number of incoming events. If this value is slowly increasing or consistently non-zero, you should scale out your job. You should increase the Streaming Units.
    Note: Streaming Units (SUs) represents the computing resources that are allocated to execute a Stream Analytics job. The higher the number of SUs, the more CPU and memory resources are allocated for your job.
    Reference: https://docs.microsoft.com/bs-cyrl-ba/azure/stream-analytics/stream-analytics-monitoring'''
        },
            {
            'question': 'You are designing an inventory updates table in an Azure Synapse Analytics dedicated SQL pool. The table will have a clustered columnstore index and will include the following columns: You identify the following usage patterns: Analysts will most commonly analyze transactions for a warehouse. Queries will summarize by product category type, date, and or inventory event type. You need to recommend a partition strategy for the table to minimize query times. On which column should you partition the table?',
            'choices': [
                'A. EventTypelD',
                'B. ProductCategoryTypelD',
                'C. EventDate',
                'D. WarehouselD'
            ],
            'answer': 'D. WarehouselD',
            'explanation': '''Explanation: Correct Answer: D
    The number of records for each warehouse is big enough for a good partitioning.
    Note: Table partitions enable you to divide your data into smaller groups of data. In most cases, table partitions are created on a date column. When creating partitions on clustered columnstore tables, it is important to consider how many rows belong to each partition. For optimal compression and performance of clustered column-store tables, a minimum of 1 million rows per distribution and partition is needed. Before partitions are created, dedicated SQL pool already divides each table into 60 distributed databases.
    Reference: https://docs.microsoft.com/en-us/azure/synapse-analvtics/sql-data-warehouse/sql-dat a-warehouse-tables-partition''',
            'image': 'static/images/image_question_25.jpg'  # Path to the image file
        },
        {
            'question': 'A company purchases loT devices to monitor manufacturing machinery. The company uses an Azure loT Hub to communicate with the loT devices. The company must be able to monitor the devices in real-time. You need to design the solution. What should you recommend?',
            'choices': [
                'A. Azure Analysis Services using Azure Portal',
                'B. Azure Analysis Services using Azure PowerShell',
                'C. Azure Stream Analytics cloud job using Azure Portal',
                'D. Azure Data Factory instance using Microsoft Visual Studio'
            ],
            'answer': 'C. Azure Stream Analytics cloud job using Azure Portal',
            'explanation': '''Explanation: Correct Answer: C
    In a real-world scenario, you could have hundreds of these sensors generating events as a stream. Ideally, a gateway device would run code to push these events to Azure Event Hubs or Azure loT Hubs. Your Stream Analytics job would ingest these events from Event Hubs and run real-time analytics queries against the streams. To create a Stream Analytics job, in the Azure portal, select + Create a resource from the left navigation menu. Then, select Stream Analytics job from Analytics.
    Reference: https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-get-started-with-azure-stream-analytics-to-process-data-from-iot-devices'''
        },
        {
            'question': 'You have an Azure Databricks resource. You need to log actions that relate to changes in compute for the Databricks resource. Which Databricks services should you log?',
            'choices': [
                'A. clusters',
                'B. workspace',
                'C. DBFS',
                'D. SSH',
                'E. jobs'
            ],
            'answer': 'A. clusters',
            'explanation': '''Explanation: Correct Answer: A
    Clusters, workspace logs do not have any cluster related resource change.
    Reference: https://docs.databricks.com/administration-guide/account-settings/audit-logs.html#workspace-level-audit-log-events'''
        },
        {
            'question': 'You are designing a highly available Azure Data Lake Storage solution that will include geo-zone-redundant storage (GZRS). You need to monitor for replication delays that can affect the recovery point objective (RPO). What should you include in the monitoring solution?',
            'choices': [
                'A. 5xx: Server Error errors',
                'B. Average Success E2E Latency',
                'C. availability',
                'D. Last Sync Time'
            ],
            'answer': 'D. Last Sync Time',
            'explanation': '''Explanation: Correct Answer: D
    Because geo-replication is asynchronous, it is possible that data written to the primary region has not yet been written to the secondary region at the time an outage occurs.
    The Last Sync Time property indicates the last time that data from the primary region was written successfully to the secondary region. All writes made to the primary region before the last sync time are available to be read from the secondary location. Writes made to the primary region after the last sync time property may or may not be available for reads yet.
    Reference: https://docs.microsoft.com/en-us/azure/storage/common/last-sync-time-get
    https://docs.microsoft.com/en-us/azure/storage/common/storage-redundancy?toc=/azure/storage/blobs/toc.son#check-the-last-sync-time-property'''
        }
]