from rest_framework import serializers
from .models import Project
from rest_framework.permissions import IsAuthenticated
#from .permissions import IsAdminAuthenticated



class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'type',
                  'author_user_id',
                  ]
        

    def create(self, validated_data):
        
        permission_classes = [IsAuthenticated]
        #permission_classes = [IsAdminAuthenticated]
        project = Project.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            type=validated_data["type"],
            author_user_id=validated_data['author_user_id']
        )
        

        return project