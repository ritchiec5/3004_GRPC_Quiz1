from __future__ import print_function

import logging
from re import template

import grpc
import template_pb2
import template_pb2_grpc

def run():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = template_pb2_grpc.templateStub(channel)
        
        """ Unary """
        response = stub.unary_rpc(template_pb2.HelloRequest(HelloRequest = "Hello Kenzo", name = "Kenzo"))
        print("Client received unary: " + response.Goodbye_reply)


        """ Server Streaming """
        responses = stub.server_streaming_rpc(template_pb2.HelloRequest(HelloRequest = "Hello Jing Hao", name = "Jing Hao"))
        goodbye_reponse = ''
        for response in responses:
            goodbye_reponse = goodbye_reponse + response.Goodbye_stream
        print("Client received server stream: " + goodbye_reponse)


        """ Client Streaming """
        response = stub.client_streaming_rpc(generate_hello_request('Hello Jia Jun', 'Jia Jun'))
        print("Client received server stream: " + response.Goodbye_reply)
        

        """ Bidirectional Streaming """
        responses = stub.bidirectional_streaming_rpc(generate_hello_request('Hello Pikachu \n', 'Pikachu'))
        goodbye_reponse = ''
        for response in responses: 
            goodbye_reponse += response.Goodbye_stream
        print("Client received server stream: " + goodbye_reponse)


        """ Repeated RPC """
        request = ['Hello', 'Charmander']
        response = stub.repeated_rpc(template_pb2.HelloRepeated(HelloRepeated=request))
        print("Client received repeated: " + response.Goodbye_reply)

def generate_hello_request(request, name):
    for i, char in enumerate(request):
        if i >= len(name):
            temp_name = "" 
        else:
            temp_name = name[i]
        yield template_pb2.HelloStream(HelloStream=char, name = temp_name)


if __name__ == '__main__':
    logging.basicConfig()
    run()
