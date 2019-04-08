import decimal
import json
from decimal import Decimal

import boto3
from boto3.dynamodb.conditions import Key, Attr
import Settings


class DbConnection:
    def __enter__(self):
        try:
            self.dynamodbResource = boto3.resource(
                Settings.DATABASE_NAME_DYN,
                aws_access_key_id=Settings.AWS_ACCESS_KEY_ID_DYN,
                aws_secret_access_key=Settings.AWS_SECRET_ACCESS_KEY_DYN,
                region_name=Settings.REGION_NAME_DYN)

            self.dynamodbClient = boto3.client(
                Settings.DATABASE_NAME_DYN,
                aws_access_key_id=Settings.AWS_ACCESS_KEY_ID_DYN,
                aws_secret_access_key=Settings.AWS_SECRET_ACCESS_KEY_DYN,
                region_name=Settings.REGION_NAME_DYN)
            self.s3 = boto3.resource('s3')

        except ConnectionError:
            print("No se puede conectar a la base de datos")

        except:
            print("Error General")

    def scan(self, table_name, attr_name, value_name):
        try:
            table = self.dynamodbResource.Table(table_name)

            response = table.scan(FilterExpression=Attr(attr_name).eq(value_name))
            return response['Items']
        except:
            print("Error en consulta")

        return []


    def update(self, table_name, item):
        try:
            table = self.dynamodbResource.Table(table_name)
            table.put_item(Item=item)
        except Exception as e:
            print('Error Actualizando')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Conexion Terminada exit")




