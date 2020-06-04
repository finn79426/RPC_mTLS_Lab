# !/usr/bin/python3
# -*-coding:utf-8 -*-

import grpc
import EchoService_pb2
import EchoService_pb2_grpc
from utils import getContent


def run():
    # 加入 SSL 金鑰與證書
    # Server 會驗證 Client 的證書、Client 會驗證 Server 的證書 (mTLS)
    credentials = grpc.ssl_channel_credentials(
        root_certificates=getContent.load('sc'),
        private_key=getContent.load('ck'),
        certificate_chain=getContent.load('cc')
    )

    # 連接 rpc Server
    with grpc.secure_channel('localhost:50051', credentials) as channel:
        # 呼叫 rpc Service
        stub = EchoService_pb2_grpc.EchoerStub(channel)

        response = stub.SayHello(EchoService_pb2.EchoRequest(name='foobar'))
        print("Echo client received: " + response.message)

        response = stub.SayHelloAgain(
            EchoService_pb2.EchoRequest(name='TLS Activited!!!'))
        print("Echo client received: " + response.message)


if __name__ == '__main__':
    run()
