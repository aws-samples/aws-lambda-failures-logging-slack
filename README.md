## Monitor Lambda Failures via slack

TODO: Fill this README out!

Be sure to:

* Change the title in this README
* Edit your repository description on GitHub

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.


### **Prerequisite**

* Please run chatbot wizard for slack and get workspace ID for your slack

Steps**

* Use cloudformation template here to deploy infra.
* CF template has default values for slack channel that is used for testing. Please change it to what is appropriate for you.
* Add New Lambda to the topic:

aws cloudwatch put-metric-alarm --alarm-name cpu-mon --alarm-description "Alarm if queue depth grows beyond 10 messages" --metric-name Errors --namespace AWS/Lambda --statistic Average --period 300 --threshold 0 --comparison-operator GreaterThanThreshold  --dimensions "Name=FunctionName,Value=SimulateError2" --evaluation-periods 1 --alarm-actions arn:aws:sns:us-west-2:889468317612:SimulateError-AlarmTopic-1HWQFL2AYCYQ2 --region us-west-2
