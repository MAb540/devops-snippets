## Template.yml And event.json

template.yml is cloudformation template, it is needed in order to test lambda functions locally with AWS SAM (Serverless Application Model).


## Add Layer In Lambda Using SAM
https://docs.aws.amazon.com/lambda/latest/dg/layers-sam.html

## Example to test lambda functions locally with AWS SAM
```
sam local invoke ScrapFunction -e event.json
sam local invoke TrapFunction -e event.json
```
