# ebs_variable_extractor
Extract environments variables from Elastic Beanstalk

Installation:

`python -m pip install -r requirements.txt`

Running:
`python main.py`

_Enter your Elastic Beanstalk application name:_

The name of the environment displayed on Beanstalk, for example **xFarm-API-DEV**

cheers


ps:

you can achieve the same thing with AWS CLI

```
aws elasticbeanstalk describe-configuration-settings \
 --application-name your-application-name \
 --environment-name your-environment-name \
 --query 'ConfigurationSettings[0].OptionSettings[?OptionName==`EnvironmentVariables`].Value' \
 --output text
```
