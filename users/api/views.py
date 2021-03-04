# from rest_framework import status
# from rest_framework.response import response
# from rest_framework.decorators import api_view

# from user.models import user
# from user.api.serializers import UserSerializer

# @api_view(['GET', ])
# def api_detail_user_view(request):
#     try:
#        user = User.objects.get() 
#     except User.DoesNotExist: 
#         return Response(status=status.HTTP_404_NOT_FOUND)