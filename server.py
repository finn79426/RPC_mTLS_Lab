# !/usr/bin/python
# -*-coding:utf-8 -*-

from concurrent import futures
import time
import grpc
import EchoService_pb2
import EchoService_pb2_grpc

# 實作 proto 文件中定義的 EchoerServicer


class Echoer(EchoService_pb2_grpc.EchoerServicer):
    # 實作 proto 文件中定義的 rpc 呼叫
    def SayHello(self, request, context):
        return EchoService_pb2.EchoReply(message='Hello {msg}'.format(msg=request.name))

    def SayHelloAgain(self, request, context):
        return EchoService_pb2.EchoReply(message='Hello {msg}'.format(msg=request.name))


def serve():
    # 啓動 rpc 服務
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    EchoService_pb2_grpc.add_EchoerServicer_to_server(Echoer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)  # 待機 1 day
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
