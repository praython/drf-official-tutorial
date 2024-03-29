from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    The HyperlinkedModelSerializer has the following differences from ModelSerializer:
        
        *It does not include the id field by default.
        *It includes a url field, using HyperlinkedIdentityField.
        *Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')
    
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 
                  'title', 'code','linenos', 'language', 'style']
        
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']