from rest_framework.response import Response

def success(message, data=None, status=200):
    return Response({
        "success": True,
        "message": message,
        "data": data
    }, status=status)

def error(message, status=400):
    return Response({
        "success": False,
        "message": message,
        "data": None
    }, status=status)