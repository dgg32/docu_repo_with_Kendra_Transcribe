import boto3
import uuid
import json
import os

def lambda_handler(event, context):

    record = event['Records'][0]
    
    s3bucket = record['s3']['bucket']['name']
    s3object = record['s3']['object']['key']

    OUTPUT_BUCKET_NAME = os.environ['OutputBucket']
    
    s3Path = "s3://" + s3bucket + "/" + s3object
    #jobName = s3object + '-' + str(uuid.uuid4())
    jobName = s3object.replace("/", "-") + '-' + str(uuid.uuid4())


    client = boto3.client('transcribe')

    response = client.start_transcription_job(
        TranscriptionJobName=jobName,
        LanguageCode='en-US',
        Media={
            'MediaFileUri': s3Path
        },
        #Bucket: process.env.OutputBucket,
        OutputBucketName = f"{OUTPUT_BUCKET_NAME}",
        OutputKey = f"audios/{jobName}.json.txt"
    )


    return {
        'TranscriptionJobName': response['TranscriptionJob']['TranscriptionJobName']
    }