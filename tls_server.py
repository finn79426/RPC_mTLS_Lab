# !/usr/bin/python
# -*-coding:utf-8 -*-

from concurrent import futures
import time
import grpc
import EchoService_pb2
import EchoService_pb2_grpc
from utils import getContent


# 實作 proto 文件中定義的 EchoerServicer


class Echoer(EchoService_pb2_grpc.EchoerServicer):
    # 實作 proto 文件中定義的 rpc 呼叫
    def SayHello(self, request, context):
        return EchoService_pb2.EchoReply(message='Hello {msg}'.format(msg=request.name))

    def SayHelloAgain(self, request, context):
        return EchoService_pb2.EchoReply(message='Hello {msg}'.format(msg=request.name))


def serve():
    # 加入 SSL 金鑰與證書
    # Server 會驗證 Client 的證書、Client 會驗證 Server 的證書 (mTLS)
    server_credentials = grpc.ssl_server_credentials(
        [(getContent.load('sk'), getContent.load('sc'))],
        root_certificates=getContent.load('cc'),
        require_client_auth=True
    )

    # 啓動 rpc 服務
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    EchoService_pb2_grpc.add_EchoerServicer_to_server(Echoer(), server)
    server.add_secure_port('[::]:50051', server_credentials)
    server.start()
    try:
        while True:
            time.sleep(60*60*24)  # 待機 1 day
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
