cd 1.hello_world
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. helloworld.proto