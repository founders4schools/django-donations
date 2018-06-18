from moneyed import Money
from rest_framework import serializers

from donations.models import Donation, Frequency


class DonationSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(
        label="amount", max_digits=10, decimal_places=2, source="amount.amount"
    )
    currency = serializers.CharField(label="amount", source="amount.currency")
    frequency = serializers.SlugRelatedField(
        queryset=Frequency.objects.all(), slug_field="name"
    )

    class Meta:  # pylint: disable=C1001
        model = Donation
        fields = ("id", "amount", "currency", "frequency")
        depth = 1

    def create(self, validated_data):
        kwargs = {
            "frequency": validated_data["frequency"],
            "amount": Money(**validated_data["amount"]),
        }
        return Donation.objects.create(**kwargs)
