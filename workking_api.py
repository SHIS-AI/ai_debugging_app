import streamlit as st
from google import genai
from dotenv import load_dotenv
import os 
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)



def generate_hints(image):
    prompt = """
        Do NOT provide the full corrected code or direct answer.
        Give clear, step-by-step hints.
        Keep explanations simple, beginner-friendly, and practical.
        If something is unclear in the screenshot, ask specific questions.
        Focus more on guiding than solving."""
    response = client.models.generate_content(

        model = "gemini-3-flash-preview",
        contents=[image,prompt]
    )
    return response.text



def generate_solution(images):
    prompt ="""Analyze the problem and provide a clear explanation with a step-by-step solution and clean, optimized code."""
    response = client.models.generate_content(
        model= "gemini-3-flash-preview",
        contents= [images,prompt]
    )
    return response.text

