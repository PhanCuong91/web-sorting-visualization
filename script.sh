#!/usr/bin/env bash
# prerequiste :
# 1. Install aws cli : https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
# 2. create a role AmazonEC2RoleforSSM: https://aws.amazon.com/vi/getting-started/hands-on/remotely-run-commands-ec2-instance-systems-manager/
# 3. create a profile in local with iam user  (AWS Access Key ID and AWS Secret Access Key  appear once create IAM user 
# https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
# aws configure --profile produser
# AWS Access Key ID [None]: AKIAI44QH8DHBEXAMPLE
# AWS Secret Access Key [None]: je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
# Default region name [None]: us-east-1
# Default output format [None]: text


echo "Start EC2 instance"

aws ec2 run-instances --cli-input-json file://ec2_deploy.json --output json

INSTANCE_ID=$(aws ec2 describe-instances --filters "Name=instance-state-name,Values=pending" --query "Reservations[].Instances[].InstanceId" --profile iamuser)

if [ "$INSTANCE_ID" == "" ]; then
	echo "ERROR - AWS reports that EC2 Instance was not created"
fi

PUBLIC_DNS=$(aws ec2 describe-instances --filters "Name=instance-id,Values=$INSTANCE_ID" --query "Reservations[].Instances[].PublicDnsName" --profile iamuser | xargs)
echo "public DNS is $PUBLIC_DNS"

echo "Wait until EC2 instance $INSTANCE_ID to report 'running' state"

RESPONSE=$(aws ec2 wait instance-status-ok --instance-ids "$INSTANCE_ID" )
if [[ ${?} -ne 0 ]]; then
	echo "ERROR - AWS reports that Wait command failed.\n$RESPONSE"
fi

echo "EC2 instance $INSTANCE_ID 's status was okay"

echo "Run docker command to create django application"

aws ssm send-command \
	--profile iamuser \
    --document-name "AWS-RunShellScript" \
    --parameters 'commands=["docker run -d -p 8000:8000 phancuong91/websortingvisualization
"]' \
    --targets "Key=instanceids,Values=${INSTANCE_ID}" \
    --comment "run django app" 
	
echo "finish docker command"
echo "please go to this link http://$PUBLIC_DNS:8000 to access django app"