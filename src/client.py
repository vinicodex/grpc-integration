import grpc
from common import greet_pb2, greet_pb2_grpc
from common import greeting_response_pb2_grpc, greeting_response_pb2

with grpc.insecure_channel('localhost:50051') as greet_channel:
    greet_stub = greet_pb2_grpc.GreeterStub(greet_channel)
    greet_response = greet_stub.SayHello(greet_pb2.HelloRequest(name='Marcos Vinicius'))
    print("Greeter client received:", greet_response.message)

with grpc.insecure_channel('localhost:50052') as response_channel:
    response_stub = greeting_response_pb2_grpc.ResponderStub(response_channel)
    response = response_stub.RespondToGreeting(greeting_response_pb2.Greeting(message=greet_response.message))
    print("Responder client received:", response.message)