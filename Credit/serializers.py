from rest_framework import serializers
from Credit.models import Demande,agent_de_verification

class DemandeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Demande
        fields=('DemandeId',
                'ClientId',
                'Montant',
                'Status',
                'But'
                )

class agent_de_verificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = agent_de_verification
        fields = ('idAgent_de_verification', 'Nom', 'Prenom', 'Age')