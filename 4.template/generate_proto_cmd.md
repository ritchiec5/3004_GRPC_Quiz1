cd 4.template
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. template.proto