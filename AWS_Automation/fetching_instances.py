import boto3
aws_man_con = boto3.session.Session(profile_name="default")
iam_console_client = aws_man_con.client(service_name='ec2')


#--getiing instances--
instances = iam_console_client.describe_instances()['Reservations']
for each in instances:
    print(each)
