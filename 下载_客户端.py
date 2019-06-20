import socket


def main():
    # 1. 创建tcp的套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 链接服务器
    # tcp_socket.connect(("192.168.33.11", 7890))
    server_ip = input("请输入要链接的服务器的ip:")
    server_port = int(input("请输入要链接的服务器的port:"))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)

    # 3. 发送数据/接收数据
    file_name = input("请输入你要下载的文件:")
    tcp_socket.send(file_name.encode("utf-8"))
    recv_data = tcp_socket.recv(1024)
    if recv_data:
        with open("[接收]"+file_name, "wb") as f:
            f.write(recv_data)

    # 4. 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()
