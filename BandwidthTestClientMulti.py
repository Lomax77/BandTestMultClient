import socket
import threading
import time

def stream_data(server_ip, port=5001, duration=5):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))
    chunk = b'0' * 4096

    start_time = time.time()
    total_sent = 0

    try:
        while time.time() - start_time < duration:
            client_socket.send(chunk)
            total_sent += len(chunk)
    finally:
        client_socket.close()

        print "Data sent: {} bytes".format(total_sent)
        print "Bandwidth: {:.2f} MB/s".format(total_sent / duration / (1024*1024))

def client(server_ip, port=5001, duration=5, streams=5):
    print "Sending data to {}:{} for {} seconds using {} streams...".format(server_ip, port, duration, streams)
    threads = []

    for _ in range(streams):
        t = threading.Thread(target=stream_data, args=(server_ip, port, duration))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    # Replace 'server_ip' with the IP address of the machine where the server script is running.
    client('server_ip')
