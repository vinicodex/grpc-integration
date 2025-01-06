import grpc
import response_pb2
import response_pb2_grpc
from concurrent import futures

class ResponderServicer(response_pb2_grpc.ResponderServicer):
    def RespondToGreeting(self, request, context):
        return response_pb2.Response(message=f"How are you, {request.message.split(',')[1].strip()}?")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    response_pb2_grpc.add_ResponderServicer_to_server(ResponderServicer(), server)
    server.add_insecure_port('[::]:50052')  # Use a different port
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()