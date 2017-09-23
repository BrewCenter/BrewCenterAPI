from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.contrib import auth
from rest_framework import status
from rest_framework.decorators import api_view


