import boto3
aws_man_con = boto3.session.Session(profile_name="default")
iam_console = aws_man_con.resource('iam')
iam_console_client = aws_man_con.client('iam')

#--using resource
for x in iam_console.users.all():
    print(x.name)

#--using client
for y in iam_console_client.list_users()['Users']:
    print(y['UserName'])

