import socket


def send_file(new_client_socket):
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print(f"要下载的文件名是{file_name}")
    content = None
    try:
        f = open(file_name, "rb")
        content = f.read()
        f.close()
    except Exception as ret:
        print("打开失败")
    # 回送一部分数据给客户端

    if content:
        new_client_socket.send(content)


def main():
    # 1. 买个手机(创建套接字 socket)
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 插入手机卡(绑定本地信息 bind)
    tcp_server_socket.bind(("222.205.62.224", 8080))

    # 3. 将手机设置为正常的 响铃模式(让默认的套接字由主动变为被动 listen)
    tcp_server_socket.listen(128)

    while True:

        # 4. 等待别人的电话到来(等待客户端的链接 accept)
        print("———waiting———")
        new_client_socket, client_addr = tcp_server_socket.accept()

        # 发送文件给客户端
        send_file(new_client_socket)

        # 关闭套接字
        new_client_socket.close()
        print("-----end-----")

    tcp_server_socket.close()


if __name__ == "__main__":
    main()
