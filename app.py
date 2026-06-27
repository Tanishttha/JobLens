from flask import Flask, request, render_template
import joblib
import os

app = Flask(__name__)
