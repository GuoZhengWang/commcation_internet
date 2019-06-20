import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ('10.12.45.209', 3736)
    udp_socket.bind(local_addr)
    while True:
        send_data = input('这是一个数据发生程序\n要退出请输入:exit\n请输入你要发生的数据:')
        udp_socket.sendto(send_data.encode("utf-8"), ("10.12.45.209", 8080))
        if send_data == 'exit':
            break

    udp_socket.close()


if __name__ == '__main__':
    main()


