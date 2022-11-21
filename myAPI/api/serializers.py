from main.models import Alarm
from rest_framework import serializers
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_ssh_public_key
import json

class AlarmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm
        fields = "__all__"

class EncryptedAlarmsSerializer(AlarmsSerializer):
    #################### FIXME ########################
    # This class returns a bitearray object, which    #
    # isn't currently being rendered by the framework.#
    #################### FIXME ########################
    
    class Meta:
        model = Alarm
        fields = "__all__"

    @staticmethod
    def _encrypt(msg : dict, pubk : str) -> bytearray:
        # encrypts msg using pubk
        bytes = json.dumps(msg, indent=4).encode('utf-8')
        public_key = load_ssh_public_key(pubk.encode("utf-8"))
        cypher = public_key.encrypt(bytes,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        return cypher

    def to_representation(self, instance):
        # overwritting parent class method to add encryption
        serialized = dict(super().to_representation(instance))
        pubk = instance.mach.pubk
        encrypted = self._encrypt(serialized, pubk)
        return encrypted
        