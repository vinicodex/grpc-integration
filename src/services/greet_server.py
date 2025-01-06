from concurrent import futures
import grpc
from common import greet_pb2_grpc, greet_pb2

class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greet_pb2.HelloReply(message=f"Hello, {request.name}!")
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server Running")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()