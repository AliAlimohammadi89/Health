from rest_framework import serializers
from .models import PersonInfo, PersonExercise
from .models import Exercise


class ValidData(serializers.Serializer):
    Username = serializers.CharField(required=True)
    Password = serializers.IntegerField(required=True)


class ValidToken(serializers.Serializer):
    Token = serializers.CharField(required=True)


class ValidTokenAndDate(serializers.Serializer):
    Token = serializers.CharField(required=True)
    DateW = serializers.CharField(required=True)


class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInfo
        fields = '__all__'
        depth = 1


class PersonExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonExercise
        fields = ['ZamanEsterahat',
                  'TedadSet',
                  'TedadTekrar',
                  'ShomareHarkat',
                  'Exercise',
                  ]
        depth = 1

        # fields = (
        #     'FirstName',
        #     'LastName',
        #     'FatherName',
        #     'Sex',
        #     'Tahsilat',
        #     'Compo_date',
        #     'Sex',
        # )


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

    # fields = (
    #     'title',
    #     'description',
    #     'video',
    #     'ExerciseGroups',
    # )
