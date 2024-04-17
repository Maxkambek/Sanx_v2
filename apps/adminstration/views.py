from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from apps.my_auth.models import Account, VerifyCode
from .serializers import AccountSerializer, VerifyCodeSerializer, AdminLoginSerializer
from rest_framework import generics, status, viewsets
from apps.main.models import Region, Catalog, UserFiles, Story, PaymentType, Currency, CarWeightType, CarType, CarBrand, \
    CarMark, Color, TransportInformation
from apps.main.v1.serializers import RegionSerializer, CatalogSerializer, StorySerializer, PaymentTypeSerializer, \
    CurrencySerializer, UserFilesSerializer, CarWeightTypeSerializer, CarMarkSerializer, CarTypeSerializer, \
    CarBrandSerializer, ColorSerializer, TransportInformationSerializer
from apps.order.models import Order, TransportDocument, OrderItem, Payment, Transaction, OrderApplicant, OrderStatus, \
    OrderView, Chat, Message
from apps.order.v1.serializers import OrderSerializer, TransportDocumentSerializer, OrderItemSerializer, \
    PaymentSerializer, TransactionSerializer, OrderApplicantSerializer, OrderStatusSerializer, OrderViewSerializer, \
    ChatSerializer, MessageSerializer


class AdminLoginView(APIView):
    serializer_class = AdminLoginSerializer

    def post(self, request, *args, **kwargs):
        phone = request.data['phone']
        password = request.data['password']
        user = Account.objects.filter(phone=phone).first()
        if not user or not user.check_password(password) or not user.is_active or not user.is_superuser:
            return Response({'message': 'User is not found'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return Response({'token': str(token), 'user_id': user.id, 'role': user.user_type}, status=status.HTTP_200_OK)


class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class AccountViewSet(MyViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'user_type', 'is_staff', 'is_active', 'is_superuser']


class VerifyCodeViewSet(MyViewSet):
    queryset = VerifyCode.objects.all()
    serializer_class = VerifyCodeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class RegionViewSet(MyViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'region_type', 'parent_id']


class CatalogViewSet(MyViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'type_catalog', 'parent_id']


class UserFilesViewSet(MyViewSet):
    queryset = UserFiles.objects.all()
    serializer_class = UserFilesSerializer


class StoryViewSet(MyViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class PaymentTypeViewSet(MyViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class CurrencyViewSet(MyViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CarWeightViewSet(MyViewSet):
    queryset = CarWeightType.objects.all()
    serializer_class = CarWeightTypeSerializer


class CarTypeViewSet(MyViewSet):
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer


class CarBrandViewSet(MyViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarMarkViewSet(MyViewSet):
    queryset = CarMark.objects.all()
    serializer_class = CarMarkSerializer


class ColorViewSet(MyViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class TransportInformationViewSet(MyViewSet):
    queryset = TransportInformation.objects.all()
    serializer_class = TransportInformationSerializer


class OrderViewSet(MyViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TransportDocumentViewSet(MyViewSet):
    queryset = TransportDocument.objects.all()
    serializer_class = TransportDocumentSerializer


class OrderItemViewSet(MyViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class PaymentViewSet(MyViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class TransactionViewSet(MyViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class OrderApplicantViewSet(MyViewSet):
    queryset = OrderApplicant.objects.all()
    serializer_class = OrderApplicantSerializer


class OrderStatusViewSet(MyViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer


class OrderViewViewSet(MyViewSet):
    queryset = OrderView.objects.all()
    serializer_class = OrderViewSerializer


class ChatViewSet(MyViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageViewSet(MyViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
