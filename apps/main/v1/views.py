from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from ..models import Region, Catalog, UserFiles, Subscription, Notification, Story, PaymentType, Currency, \
    CarWeightType, CarType, CarBrand, CarMark, Color, TransportInformation
from . import serializers as main_serializers
from rest_framework import generics, status, response, permissions, authentication, viewsets


class RegionList(generics.ListAPIView):
    serializer_class = main_serializers.RegionSerializer
    queryset = Region.objects.all()
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'parent_id', 'region_type']


class CatalogList(generics.ListAPIView):
    serializer_class = main_serializers.CatalogSerializer
    queryset = Catalog.objects.all()
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'parent_id']


class UserFilesList(generics.ListAPIView):
    serializer_class = main_serializers.UserFilesSerializer
    queryset = UserFiles.objects.all()


class UserFilesCreate(generics.CreateAPIView):
    serializer_class = main_serializers.UserFilesSerializer
    queryset = UserFiles.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]


class UserFilesRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = main_serializers.UserFilesSerializer
    queryset = UserFiles.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = main_serializers.SubscriptionSerializer
    queryset = Subscription.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['watcher_id', 'user_id']


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = main_serializers.NotificationSerializer
    queryset = Notification.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id', 'is_read']


class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = main_serializers.StorySerializer
    queryset = Story.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']


class PaymentTypeList(generics.ListAPIView):
    serializer_class = main_serializers.PaymentTypeSerializer
    queryset = PaymentType.objects.all()


class CurrencyList(generics.ListAPIView):
    serializer_class = main_serializers.CurrencySerializer
    queryset = Currency.objects.all()


class CarWeightTypeList(generics.ListAPIView):
    serializer_class = main_serializers.CarWeightTypeSerializer
    queryset = CarWeightType.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'weight_max']


class CarTypeList(generics.ListAPIView):
    serializer_class = main_serializers.CarTypeSerializer
    queryset = CarType.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'car_weight_type_id']


class CarBrandList(generics.ListAPIView):
    serializer_class = main_serializers.CarBrandSerializer
    queryset = CarBrand.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['car_type_id', 'name']


class CarMarkList(generics.ListAPIView):
    serializer_class = main_serializers.CarMarkSerializer
    queryset = CarMark.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['car_brand_id', 'name']


class ColorList(generics.ListAPIView):
    serializer_class = main_serializers.ColorSerializer
    queryset = Color.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', ]


class TransportInformationList(generics.ListAPIView):
    serializer_class = main_serializers.TransportInformationSerializer
    queryset = TransportInformation.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return TransportInformation.objects.filter(user=self.request.user)


class TransportInformationCreate(generics.CreateAPIView):
    serializer_class = main_serializers.TransportInformationSerializer
    queryset = TransportInformation.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

