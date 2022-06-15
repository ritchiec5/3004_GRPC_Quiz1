cd 3.stream
https://grpc.io/docs/languages/python/basics/
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. route_guide.proto