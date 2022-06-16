from __future__ import print_function

import logging
from re import template

import grpc
import bookreview_pb2
import bookreview_pb2_grpc

def run():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = bookreview_pb2_grpc.bookreviewStub(channel)
        
        # Create Review
        response = stub.create_review(bookreview_pb2.review(bookname = "Book", review = "Good book"))
        print(response.review_reponse)

        # Create Review
        response = stub.create_review(bookreview_pb2.review(bookname = "Beyond good and evil", review = "Beyond me"))
        book_list = ""

        # Retrieve History
        response = stub.retrieve(bookreview_pb2.retrieval(retrieve = "retrieve"))
        for response in response.booklist:
            book_list = book_list + response + " ," 
        print(book_list)

        # Query books
        reponse = stub.query(bookreview_pb2.queries(query = "Book"))
        print("Bookname: ", reponse.bookname, "\n Book Review:", reponse.review)



if __name__ == '__main__':
    logging.basicConfig()
    run()
