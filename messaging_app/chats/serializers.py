from rest_framework import serializers, ValidationError
from .models import User, Conversation, Message
#from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    role = serializers.CharField()

    def validate_role(self, value):
        allowed_roles = ['guest', 'host', 'admin']
        if value not in allowed_roles:
            raise ValidationError("Role must be one of: guest, host, admin")
        return value

    class Meta:
        model = User
        fields = [
            'user_id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role',
            'created_at'
        ]
        read_only_fields = ['user_id', 'created_at']



class MessageSerializer(serializers.ModelSerializer):
    sender_full_name = serializers.SerializerMethodField()

    def get_sender_full_name(self, obj):
        return f"{obj.sender.first_name} {obj.sender.last_name}"

    class Meta:
        model = Message
        fields = [
            'message_id',
            'sender',
            'sender_full_name',
            'message_body',
            'sent_at'
        ]
        read_only_fields = ['message_id', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = [
            'conversation_id',
            'participants',
            'messages',
            'created_at'
        ]
        read_only_fields = ['conversation_id', 'created_at']
