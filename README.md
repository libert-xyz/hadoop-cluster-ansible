# Hadoop multi-node cluster with Ansible
Multi-server deployment of Hadoop using Ansible / AWS

## Version and Tools

Ubuntu 16.04 LTS
Ansible 2.3
Hadoop 2.7.3

## Role Variables

### hadoop user, group
hadoop_user: hadoop
hadoop_group: hadoop

### hadoop version
hadoop_download_url: http://apache.claz.org/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz

### Cluster memory
#### helper: https://hortonworks.com/blog/how-to-plan-and-configure-yarn-in-hdp-2-0/

yarn_memory_mb: 4000

###MapReduce mapred-site.xml
map_memory_mb: 1024
reduce_memory_mb: 2048

## Quick Start (Master)


1. Edit host file with the Public ip address of the instances and PEM key
2. Edit nodes-ip with the private ip address of the instances
   Ex.
   - hostname: hadoop-data-0
     ip: x.x.x.x
   - hostname: hadoop-data-1
     ip: x.x.x.x

3. run: ansible-playbook -i hosts playbook.yml

4. ssh into the master and run:

  sudo su hadoop
  hdfs namenode -format
  /usr/local/hadoop/sbin/start-dfs.sh
  /usr/local/hadoop/sbin/start-yarn.sh

5. Run test job:

  hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar pi 10 30


## Ports

8088 UI http
50070 UI master

### Daemon Ports
50075
50020
50090
54310
54311
8030
8032
8088
8031
8033
8040
8042
