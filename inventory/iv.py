#! /usr/bin/env python

import argparse
import boto.ec2.autoscale
import json
import os
import sys

def get_tag(tags, key):
    for tag in tags:
        if tag.key == key:
            return tag.value

    return None

region = os.environ.get('AWS_REGION', None)
if region is None:
    print "$AWS_REGION must be set"
    sys.exit(1)

parser = argparse.ArgumentParser(description='Dynamic inventory for autoscaling groups')
parser.add_argument('--list', help="list hosts", action="store_true")
parser.add_argument('--host', help="list host vars")
args = parser.parse_args()

if args.host:
  print "{}"

if not args.list:
  sys.exit(1)

autoscale = boto.ec2.autoscale.connect_to_region(region)
ec2 = boto.ec2.connect_to_region(region)

inventory = {"_meta": {"hostvars": {}}}
# for autoscaling_group in autoscale.get_all_groups():
#   instance_ids = [i.instance_id for i in autoscaling_group.instances]
#   instance_dns_names = [i.public_dns_name for r in ec2.get_all_instances(instance_ids) for i in r.instances]
#   name = get_tag(autoscaling_group.tags, 'Name')
#   if name not in inventory:
#       inventory[name] = { "hosts": [] }
#   inventory[name]['hosts'] += instance_dns_names

 for instances in get_all_instances():
   instance_ids = [i.instance_id for i in autoscaling_group.instances]
   instance_dns_names = [i.public_dns_name for r in ec2.get_all_instances(instance_ids) for i in r.instances]
   name = get_tag(autoscaling_group.tags, 'Name')
   if name not in inventory:
       inventory[name] = { "hosts": [] }
   inventory[name]['hosts'] += instance_dns_names

print json.dumps(inventory)
