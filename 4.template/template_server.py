from concurrent import futures
import logging

import grpc
import template_pb2
import template_pb2_grpc


class template(template_pb2_grpc.templateServicer):

    """ Unary """
    def unary_rpc(self, request, context):
        print("Server received unary: " + request.HelloRequest)
        return template_pb2.Goodbye_reply(Goodbye_reply='Goodbye, {}'.format(request.name))


    """ Server Streaming """
    def server_streaming_rpc(self, request, context):
        print("Server received server stream: " + request.HelloRequest)
        goodbye = "Goodbye, " + request.name
        for char in goodbye:
            yield template_pb2.Goodbye_stream(Goodbye_stream = char)


    """ Client Streaming """
    def client_streaming_rpc(self, request_iterator, context):
        Hello_stream = ''
        name = ''
        for request in request_iterator:
            Hello_stream += request.HelloStream
            name += request.name 
        print("Server received client stream: " + Hello_stream)
        return template_pb2.Goodbye_reply(Goodbye_reply='Goodbye, {}'.format(name))


    """ Bidirectional Streaming """
    def bidirectional_streaming_rpc(self, request_iterator, context):
        Hello_stream = ''
        name = ''
        for request in request_iterator:
            Hello_stream += request.HelloStream
            name += request.name
        print("Server received server stream: " + Hello_stream)

        goodbye = "Goodbye, " + name + "\n"
        for char in goodbye:
            yield template_pb2.Goodbye_stream(Goodbye_stream = char)
        
    """ Repeated RPC """
    def repeated_rpc(self, request, context):
        print("Server received server stream: " + str(request.HelloRepeated))
        return template_pb2.Goodbye_reply(Goodbye_reply='Goodbye, {}'.format(request.HelloRepeated[1]))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    template_pb2_grpc.add_templateServicer_to_server(template(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
