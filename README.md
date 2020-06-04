1. 編譯 proto file

```
pip3 install grpcio
python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. EchoService.proto
```

2. 建立 server 的 private key 跟 certificate

```
openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout ./secrets/server.key -subj '/CN=localhost' -out ./secrets/server.crt
```

3. 建立 client 的 private key 跟 certificate

openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout ./secrets/client.key -subj '/CN=localhost' -out ./secrets/client.crt

4. 先啓動 server

```
pythod3 ./server.py
or
python3 ./tls_server.py
```

5. 再啓動 client 來建立連線

```
pythod3 ./client.py
or
python3 ./tls_client.py
```