from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.order.models import Order, OrderFiles, TransportDocument, OrderItem, Payment, Transaction, OrderApplicant, \
    OrderView, OrderStatus
from .serializers import OrderSerializer, OrderFilesSerializer, TransportDocumentSerializer, OrderItemSerializer, \
    PaymentSerializer, TransactionSerializer, OrderApplicantSerializer, OrderViewSerializer, OrderStatusSerializer, \
    OrderListSerializer, OrderApplicantListSerializer

from django_filters.rest_framework import DjangoFilterBackend


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.id)


class OrderDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.id)


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'name', 'catalog_id', 'order_type', 'from_region_id', 'to_region_id', 'transport_type_id', 'weight', 'brutto',
        'volume')


class OrderFilesCreateAPIView(generics.CreateAPIView):
    queryset = OrderFiles.objects.all()
    serializer_class = OrderFilesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class OrderFilesUpdateAPIView(generics.UpdateAPIView):
    queryset = OrderFiles.objects.all()
    serializer_class = OrderFilesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class OrderApplicantCreateAPIView(generics.CreateAPIView):
    queryset = OrderApplicant.objects.all()
    serializer_class = OrderApplicantSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class OrderApplicantListAPIView(generics.ListAPIView):
    queryset = OrderApplicant.objects.all()
    serializer_class = OrderApplicantListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('created_by', 'order_id', 'user_id')


class OrderApplicantRetrieveAPIView(generics.RetrieveAPIView):
    queryset = OrderApplicant.objects.all()
    serializer_class = OrderApplicantListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class OrderApplicantUpdateAPIView(generics.UpdateAPIView):
    queryset = OrderApplicant.objects.all()
    serializer_class = OrderApplicantSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
