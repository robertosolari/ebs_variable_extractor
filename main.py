import boto3

def get_environment_variables(application_name, environment_name):
    try:
        # Create an Elastic Beanstalk client
        eb_client = boto3.client('elasticbeanstalk')

        # Describe configuration settings for the environment
        response = eb_client.describe_configuration_settings(
            ApplicationName=application_name,
            EnvironmentName=environment_name
        )

        # Extract the "EnvironmentVariables" option
        for option in response['ConfigurationSettings'][0]['OptionSettings']:
            if option['OptionName'] == 'EnvironmentVariables':
                environment_variables = option['Value']

        environment_variables = environment_variables.replace(',', ';')

        return environment_variables
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    application_name = input("Enter your Elastic Beanstalk application name: ")
    environment_name = application_name #input("Enter the environment name: ")

    environment_variables = get_environment_variables(application_name, environment_name)

    if environment_variables:
        print("Environment Variables:")
        print(environment_variables)
    else:
        print(f"Environment variables not found for {environment_name} in application {application_name}.")
