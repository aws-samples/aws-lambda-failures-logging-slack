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
* Enter the parameters such as ****AlarmEmail**, LambdaFunctionNames**, **LambdaFunctionTags**, **LambdaFunctionTagsValue**, **SlackWorkspaceId** and **SlackChannelId**
*
