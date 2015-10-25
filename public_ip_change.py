#!/bin/python
import argparse, boto3

def parse_args():
    parser = argparse.ArgumentParser(description='Updates DNS for an instance id entered.')
    parser.add_argument('-id','--id', help='Instance ID that should be found', required=True)
    parser.add_argument('-hostzone','--hostzone', help='Route53 zone being updated', required=True)
    parser.add_argument('-hostname','--hostname', help='Route53 hostname being updated', required=True)
    args = vars(parser.parse_args())
    return args

def update_host(args):
    instance_id = args['id']
    hosted_zone = args['hostzone']
    instance_hostname = args['hostname']
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    instance_publicip = instance.public_ip_address
    route53 = boto3.client('route53')
    recordValue={'Value': instance_publicip}
    ResourceRecord=[recordValue]
    recordSet={'Name':instance_hostname,'Type':'A','ResourceRecords': ResourceRecord, 'TTL': 60}
    changes={'Action':'UPSERT','ResourceRecordSet':recordSet}
    changeBatch={'Changes':[changes]}
    route53.change_resource_record_sets(HostedZoneId=hosted_zone, ChangeBatch=changeBatch)
    print('Setting %s to %s' % (instance_publicip, instance_hostname))

if __name__ == '__main__':
    args = parse_args()
    update_host(args)