import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(object):
    user = graphene.Field(UserType, id=graphene.Int(), name=graphene.String())
    all_users = graphene.List(UserType)

    def resolve_all_users(self, context):
        return User.objects.all()

    def resolve_user(self, context, id=None, username=None):
        if id is not None:
            return User.objects.get(pk=id)
        if username is not None:
            return User.objects.get(username=username)
        return None


class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    username = graphene.String()
    password = graphene.String()
    last_name = graphene.String()
    first_name = graphene.String()


class CreateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, input=None):
        user = User(username=input.username)
        user.set_password(input.password)
        if input.last_name:
            user.last_name = input.last_name
        user.save()
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
