import socket


def main():
    # 1. 买个手机(创建套接字 socket)
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 插入手机卡(绑定本地信息 bind)
    tcp_server_socket.bind(("10.12.45.209", 8080))

    # 3. 将手机设置为正常的 响铃模式(让默认的套接字由主动变为被动 listen)
    tcp_server_socket.listen(128)

    while True:

        # 4. 等待别人的电话到来(等待客户端的链接 accept)
        print("———waiting———")
        new_client_socket, client_addr = tcp_server_socket.accept()

        print(f"客户端的地址是{str(client_addr)}")

        while True:

            # 接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print(f"客户端的请求是{recv_data.decode()}")

            # 回送一部分数据给客户端

            if len(recv_data.decode()) == 0:
                break
            else:
                new_client_socket.send("hahahghai-----ok-----".encode("utf-8"))

        # 关闭套接字
        new_client_socket.close()
        print("-----end-----")

    tcp_server_socket.close()


if __name__ == "__main__":
    main()
