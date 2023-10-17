import boto3 

def get_volume_id_from_arn(volume_arn):
    #split ARN using the colon separator
    arn_parts = volume_arn.split(':')
    # the volume id is the last part of the ARN after the 'Volume/' prefix
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id
    
    volume_arn = event[resources][0]
    volume_id = get_volume_id_from_arn(volume_arn)
    
    
    ec2_client = boto3.client('ec2')
    
    response = ec2_client.modify_volume(
        volumeID = volume_id, 
        volumeType = 'gp3',
        )
    
    
    print(event)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
