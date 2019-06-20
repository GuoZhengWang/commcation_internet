import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ('10.12.45.209', 3736)
    udp_socket.bind(local_addr)

    while True:
        receive_data = udp_socket.recvfrom(1024)
        receive_msg = receive_data[0].decode('gbk')
        receive_adr = receive_data[1]
        print(f'你收到的数据是:{receive_msg}')

        if receive_msg == 'exit':
            break

    udp_socket.close()


if __name__ == '__main__':
    main()
