from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
import requests
import subprocess
import json


app = Flask(__name__)
api = Api(app)

client = MongoClient("mongo://db:27017")
db = client.ImageRecognition
users = db["Users"]


class Register(Resource):
    def post(self):
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData["password"]

        # Not checking if exsists
        # Not encrypting te password either
        # I am skipping it all

        users.insert({
            "Username": username,
            "Password": password,
            "Tokens": 4
        })

        retJson = {
            "status": 200,
            "msg": "You are successfully registered"
        }
        return jsonify(retJson)
        