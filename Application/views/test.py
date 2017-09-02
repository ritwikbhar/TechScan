from flask import Blueprint, render_template, redirect, url_for, request, jsonify

import flask
import time
import os

#creating Blueprint
test_bp = Blueprint('test',__name__)

@test_bp.route("/")
@test_bp.route("/home")
def home():
    return "Hello";
