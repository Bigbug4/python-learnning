#-*- coding:utf-8 -*-
__author__ = "Bigbug4"
 
import paramiko
 
ssh = paramiko.SSHClient()#创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())#允许连接不在know_hosts文件中的主机
pkey = paramiko.RSAKey.from_private_key_file('C:/Users/Administrator/.ssh/id_rsa')
ssh.connect(hostname='192.168.1.106', port=22, username='dcl', pkey=pkey)#连接服务器
 
stdin, stdout, stderr = ssh.exec_command('ls python')#执行命令并获取命令结果
#stdin为输入的命令
#stdout为命令返回的结果
#stderr为命令错误时返回的结果
res,err = stdout.read(),stderr.read()
result = res if res else err
print(result)
ssh.close()#关闭连接
