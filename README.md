# Hadoop multi-node cluster with Ansible
Multi-server deployment of Hadoop using Ansible

Inspired from: https://github.com/dwatrous/hadoop-multi-server-ansible


## Quick Start (Master)

sudo su hadoop
hdfs namenode -format
/usr/local/hadoop/sbin/start-dfs.sh
/usr/local/hadoop/sbin/start-yarn.sh

#### Run Test Job
hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar pi 10 30
