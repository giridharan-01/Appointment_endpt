from flask import Flask,request
from utils import init_llm
from prompts import get_prompt
from langchain_core.output_parsers import JsonOutputParser
import json
from waitress import serve
from datetime import date

app = Flask(__name__)

llm = init_llm()

@app.route("/ping",methods=['POST'])
def resp_ping():
    return "pong"

@app.route("/check",methods=['POST'])
def status():
    data = request.json

    question = data.get('question')

    prompt = get_prompt()

    chain = prompt | llm | JsonOutputParser()

    response = chain.invoke({"input_msg":question,"date":date.today()})
    print(date.today())

    print(question)

    return response


if __name__ == "__main__":
    # app.run(debug=True)
    serve(app, host = "0.0.0.0", port = 8000, threads =1)
    
