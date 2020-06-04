# !/usr/bin/python
# -*-coding:utf-8 -*-

import grpc
import EchoService_pb2
import EchoService_pb2_grpc


def run():
    # 連接 rpc Server
    channel = grpc.insecure_channel('localhost:50051')
    # 呼叫 rpc Service
    stub = EchoService_pb2_grpc.EchoerStub(channel)

    response = stub.SayHello(EchoService_pb2.EchoRequest(name='foobar'))
    print("Echo client received: " + response.message)

    response = stub.SayHelloAgain(
        EchoService_pb2.EchoRequest(name='TLS Unactivited!!!'))
    print("Echo client received: " + response.message)


if __name__ == '__main__':
    run()
