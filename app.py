from flask import Flask, request, render_template
import joblib
import os

app = Flask(__name__)

MODEL_PATH = "model/model.pkl"
VECTORIZER_PATH = "model/vectorizer.pkl"
