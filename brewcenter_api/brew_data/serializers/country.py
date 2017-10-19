from rest_framework import serializers
from brew_data.models import CountryCode


class CountryCodeSerializer(serializers.BaseSerializer):
    def to_representation(self, codes):
        return {'id'    : codes["id"],
                'code': codes["alpha_2"],
               }

