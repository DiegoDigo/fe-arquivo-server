from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView
import logging

log = logging.getLogger(__name__)


class HealthCheckAPIView(APIView):
    def get(self, request, format=None):
        # Database
        database_healthy = True
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT 1;')
        except Exception as err:
            database_healthy = False
            log.exception(err)
        finally:
            if cursor is not None:
                cursor.close()

        data = {
            'database': database_healthy
        }
        return Response(data)
