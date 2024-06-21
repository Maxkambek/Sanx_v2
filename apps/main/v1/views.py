from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from ..models import Region, Catalog, UserFiles, Subscription, Notification, Story, PaymentType, Currency, \
    CarWeightType, CarType, CarBrand, CarMark, Color, TransportInformation, UserRating
from . import serializers as main_serializers
from rest_framework import generics, status, response, permissions, authentication, viewsets


class UserRatingCreate(generics.GenericAPIView):
    queryset = UserRating.objects.all()
    serializer_class = main_serializers.UserRatingCreateSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user_id = request.data['user_id']
        rate = request.data['rate']
        if user_id is None or rate is None:
            return response.Response({'error': 'Please provide both user_id and rate'},
                                     status=status.HTTP_400_BAD_REQUEST)
        try:
            user = UserRating.objects.get(pk=user_id)
        except:
            user = UserRating.objects.create(user_id=user_id, negative=0, positive=0)
        if rate:
            user.positive += 1
        if not rate:
            user.negative += 1
        return Response(data={'user_id': user_id, 'positive': user.positive, 'negative': user.negative},
                        status=status.HTTP_201_CREATED)


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


class NotificationListAPIView(generics.ListAPIView):
    serializer_class = main_serializers.NotificationSerializer
    queryset = Notification.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id', 'is_read']


class NotificationUpdate(generics.UpdateAPIView):
    serializer_class = main_serializers.NotificationSerializer
    queryset = Notification.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = main_serializers.SubscriptionSerializer
    queryset = Subscription.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['watcher_id', 'user_id']


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
        serializer.save(user_id=self.request.user.id)
