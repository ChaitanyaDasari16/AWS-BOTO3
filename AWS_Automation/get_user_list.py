import boto3
aws_man_con = boto3.session.Session(profile_name="default")
iam_console = aws_man_con.resource('iam')
for x in iam_console.users.all():
    print(x.name)
