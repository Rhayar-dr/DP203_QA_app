
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
        }
]