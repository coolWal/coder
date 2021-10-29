import os


def linux_link_server_cmd(cmd):
    try:
        stdout = os.popen(cmd)
        content = stdout.readlines()
        # print("content", content, type(content))
        connect = int(content[0].rstrip('\n'))
        return connect
    except Exception as error:
        pass

if __name__ == "__main__":
    # cmd = 'netstat -pnt | grep 8500 | wc -l'  # 查看连接人数命令
    cmd = 'ps -ef'  # 查看连接人数命令
    connect = linux_link_server_cmd(cmd)
    print("connect======", connect)

