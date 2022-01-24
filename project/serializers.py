from rest_framework import serializers
from .models import Project, Contributor, Issue, Comment
from custom_user.serializers import UserSerializer



class ProjectListSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'type',
                  'author_user_id',
                  
                  ]
        

    def create(self, validated_data):
        
        
        project = Project.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            type=validated_data["type"]
        )
        

        return project
class ProjectDetailSerializer(serializers.ModelSerializer):

    contributors = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user_id', 'contributors']

    def get_contributors(self, instance):
        queryset = instance.contributors.filter(project_id=instance.id)
        return ContributorSerializer(queryset, many=True).data
class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project','permission','role']

class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'title', 'descripition', 'tag', 'priority', 'status', 'project_id', 'author_user_id', 'assignee_user', 'created_time']


    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description', 'author_user', 'issue_id', 'created_time']