from rest_framework import serializers
from rest_framework.validators import UniqueValidator, ValidationError
from django.contrib.auth.password_validation import validate_password
from utils.exceptions import ConflictError
from member.models import Members, ProofOfPayment


class UserSerializer(serializers.ModelSerializer):
    display_pic = serializers.ImageField(required=False)
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=Members.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Members
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
            "dob",
            "gender",
            "glug",
            "institute",
            "country_code",
            "contact",
            "blood_group",
            "address",
            "display_pic",
            "occupation",
            "edu_qualification",
            "stream",
            "profile_status",
            "is_accept_TC",
            "is_news_subscribed",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise ValidationError({"password": "Password fields didn't match."})
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class PaymentSerializer(serializers.ModelSerializer):
    document = serializers.ImageField(required=True)

    class Meta:
        model = ProofOfPayment
        fields = ["transaction_id", "document"]

    def validate(self, attrs):
        transaction_exists = ProofOfPayment.objects.filter(
            transaction_id=attrs["transaction_id"]
        ).exists()
        if transaction_exists:
            raise ConflictError(
                "Transaction ID already exists. Please contact the administrator."
            )
        return super().validate(attrs)
