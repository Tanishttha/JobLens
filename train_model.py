import pandas as pd
df = pd.read_csv("fake_job_postings.csv")
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

print("Loading dataset...")
data = pd.read_csv("fake_job_postings.csv")  

print("Cleaning dataset...")
data = data[["title", "description", "fraudulent"]]
data = data.dropna()

