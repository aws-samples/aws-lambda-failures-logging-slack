from botocore.vendored import requests
import urllib3
import json
import boto3
import botocore
import traceback
import os
import os.path
from botocore.exceptions import ClientError

def sendResponse(event, context, responseStatus, responseData):
              http = urllib3.PoolManager()
              responseBody = {'Status': responseStatus,
                              'Reason': 'See the details in CloudWatch Log Stream: ' + context.log_stream_name,
                              'PhysicalResourceId': context.log_stream_name,
                              'StackId': event['StackId'],
                              'RequestId': event['RequestId'],
                              'LogicalResourceId': event['LogicalResourceId'],
                              'Data': responseData}
              print("RESPONSE BODY:\n" + json.dumps(responseBody))
              try:
                  req = requests.put(event['ResponseURL'], data=json.dumps(responseBody))
                  # r = http.request('PUT', event['ResponseURL'],
                  #                                       body=json.dumps(responseBody).encode('utf-8'))
                  # req = r.data.decode('utf-8')
                  if req.status_code != 200:
                      print(req.text)
                      raise Exception('Recieved non 200 response while sending response to CFN.')
                  return
              except requests.exceptions.RequestException as e:
                  print(e)
                  raise

def lambda_handler(event, context):
    # TODO implement
    
    # This assumes both ~/.aws/credentials and ~/.aws/config (for region are present)
    session = boto3.Session()
    lambda_client = session.client('lambda')
    cloudwatch = session.client('cloudwatch')
    
    # Remove permissions / policies from specific lambda function
    paginator = lambda_client.get_paginator('list_functions')
    response_iterator = paginator.paginate()
    
    count = 0
    
    for response in response_iterator:
      functions = response["Functions"]
    
      for function in functions:
          function_name = function["FunctionName"]
        
          function_name = str(function_name)
          try:
            # client_policy = lambda_client.get_policy(FunctionName=function_name)
            print("+++", function_name)
            
            # Add Cloudwatch Metric Alarm
            cloudwatch.put_metric_alarm(
                AlarmName='Lambda_CPU_Utilization_%s' % function_name,
                ComparisonOperator='GreaterThanThreshold',
                EvaluationPeriods=1,
                MetricName='Errors',
                Namespace='AWS/Lambda',
                Period=300,
                Statistic='Average',
                Threshold=0,
                ActionsEnabled=False,
                AlarmDescription='Alarm when error queue depth is more than 10',
                Dimensions=[
                    {
                      'Name': 'FunctionName',
                      'Value': function_name
                    },
                ],
                Unit='Seconds'
            )

            # Signal CFN stack on execution completion
            sendResponse(event, context, 'SUCCESS', {})
        
          except ClientError as e:
            print(e.response['Error']['Message'] + ' ' + function_name)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
