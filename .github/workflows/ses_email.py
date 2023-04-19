# import boto3
# import os
# from botocore.exceptions import ClientError

# # Set up the AWS SES client
# client = boto3.client('ses', region_name='us-east-1')

# # Set up the attachment files
# attachment_file_paths = ['gzipfile.txt.gz', '2gzipfile.txt.gz']

# # Create a new email message
# message = {
#     'Subject': {
#         'Data': 'Test Email'
#     },
#     'Body': {
#         'Text': {
#             'Data': 'This is a test email sent using the AWS SES API'
#         }
#     }
# }

# # Add the attachments to the email message
# for file_path in attachment_file_paths:
#     with open(file_path, 'rb') as f:
#         file_name = os.path.basename(file_path)
#         file_content = f.read()
#         message['Attachments'] = [
#             {
#                 'FileName': file_name,
#                 'ContentType': 'application/octet-stream',
#                 'Data': file_content
#             }
#         ]

# # Send the email using the AWS SES API
# try:
#     response = client.send_email(
#         Source='davron.n@yahoo.com',
#         Destination={
#             'ToAddresses': ['davronbekn@gmail.com',]
#         },
#         Message=message
#     )
# except ClientError as e:
#     print(e.response['Error']['Message'])
# else:
#     print("Email sent! Message ID:", response['MessageId'])
