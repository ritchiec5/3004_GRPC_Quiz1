from concurrent import futures
import logging

import grpc
import bookreview_pb2
import bookreview_pb2_grpc

bookreviews = []

class bookreview(bookreview_pb2_grpc.bookreviewServicer):

    
    def create_review(self, request, context):
        global bookreviews
        bookexist = False

        bookreview = {
            "bookname": "",
            "review":""
        }

        bookreview["bookname"] = request.bookname
        bookreview["review"] = request.review

        for book in bookreviews:
            if (book["bookname"] == request.bookname):
                book["review"] = book["review"] + ' ' + request.review
                bookexist = True
        
        if not bookexist:
            bookreviews.append(bookreview)

        print(bookreviews)
        return bookreview_pb2.review_reponse(review_reponse='Book Reviews added Successfully')


    def retrieve(self, request, context):
        global bookreviews

        list_of_books = []
        for book in bookreviews:
            list_of_books.append(book["bookname"])
        
        return bookreview_pb2.retrieve_reponse(booklist=list_of_books)

    def query(self, request, context):
        global bookreviews

        bookname = ""
        bookreview = ""
        for book in bookreviews:
            if (book["bookname"] == request.query):
                bookname = book["bookname"]
                bookreview = book["review"]

        return bookreview_pb2.review(bookname=bookname, review=bookreview)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bookreview_pb2_grpc.add_bookreviewServicer_to_server(bookreview(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
