from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(data=request.data, instance=book)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return Response(status=204)
