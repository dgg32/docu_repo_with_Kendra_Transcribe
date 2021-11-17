# S3-to-Elasticsearch - The Serverless Document Repository

This repo contains an AWS SAM template that deploys a serverless application. This application uses Amazon ML services like Comprehend and Textract to index documents and images, Transcribe for audios and videos, and then sends the results to Elasticsearch for fast indexing. Later, Kendra and Glue were also added to provide more search options.

This architecture is designed for large numbers of documents by using queuing. For full details on how this works, read the article at: https://aws.plainenglish.io/make-an-ai-powered-enterprise-document-repository-on-aws-8a25fad48fd2 (inspired mainly by [this](https://aws.amazon.com/blogs/compute/creating-a-searchable-enterprise-document-repository/)).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

```bash
.
├── README.MD                   <-- This instructions file
├── addToQueueFunction          <-- Source code for a lambda function
│   └── app.js                  <-- Main Lambda handler
│   └── package.json            <-- NodeJS dependencies and scripts
├── batchingFunction            <-- Source code for a lambda function
│   └── app.js                  <-- Main Lambda handler
│   └── package.json            <-- NodeJS dependencies and scripts
├── addToESindex                <-- Source code for a lambda function
│   └── app.js                  <-- Main Lambda handler
│   └── package.json            <-- NodeJS dependencies and scripts
├── processDOCX                 <-- Source code for a lambda function
│   └── app.js                  <-- Main Lambda handler
│   └── package.json            <-- NodeJS dependencies and scripts
├── processGraph                <-- Source code for a lambda function
│   └── app.js                  <-- Main Lambda handler
│   └── package.json            <-- NodeJS dependencies and scripts
├── processPDF                  <-- Source code for a lambda function
│   └── app.js                  <-- Main Lambda handler
│   └── package.json            <-- NodeJS dependencies and scripts
├── processAudio                <-- Source code for a lambda function
│   └── app.py                  <-- Main Lambda handler
├── template.yaml               <-- SAM template
```

The rest of yaml are sub-CloudFormation templates that you can use to set up a part of the pipeline.

## Requirements

* AWS CLI already configured with Administrator permission
* AWS SAM CLI
* [NodeJS 12.x installed](https://nodejs.org/en/download/)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. Clone the repo onto your local development machine using `git clone`.

1. From the command line, change directory into v1 or v2 depending on the version required, then run:
```
sam build
sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
```
Follow the prompts in the deploy process to set the stack name, AWS Region, unique bucket names, and other parameters.

## How it works

* Upload the files to the target Documents bucket folders.
* After a few seconds you will see the index in Elasticsearch has been updated with labels and entities for the object.
* Manually kick-start Kendra and Glue

==============================================

Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.

Modified and extended by Sixing Huang, 2021

SPDX-License-Identifier: MIT-0
