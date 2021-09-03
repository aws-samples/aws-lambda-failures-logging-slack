## Monitor Lambda Failures via slack


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

### **Prerequisite**

1. **Workspace ID** - Run chatbot wizard for slack in AWS console to get workspace ID for your slack. e.g *T01UXHUCRMW*
2. **Slack Channel ID** - Right-click on your channel in slack and copy the link. Use last portion to get slack Channel ID. e.g. *C01U80K9KPD*

### Steps

* Use cloudformation template from here to deploy infra.
* Enter the parameters as needed. 

  * **AlarmEmail**: If you chose to get emails for Lambda failures, enter an email address here.
  * **LambdaFunctionNames**:  A comma-separated list of Lambda function names in the Region. This parameter becomes optional if you provide value for *LambdaFunctionTags *and *LambdaFunctionTagsValue *parameters.
  * **LambdaFunctionTags**: The name of the tag that will be evaluated to find and add Lambda functions for monitoring in your account. This parameter becomes optional along with *LambdaFunctionTagsValue *if you provide names of the functions in *LambdaFunctionNames*.
  * **LambdaFunctionTagsValue**: The value of the tag that will be matched to find and add Lambda function for monitoring. This parameter is needed if you have provided tag key at*LambdaFunctionTags*.
  * **SlackWorkspaceId**: Enter the Slack workspace ID.
  * **SlackChannelId**: Enter the channel ID.
