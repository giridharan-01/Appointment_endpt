from flask import Flask,request
from utils import init_llm
from prompts import get_prompt
from langchain_core.output_parsers import JsonOutputParser
import json
from waitress import serve


app = Flask(__name__)

llm = init_llm()

@app.route("/check",methods=['POST'])
def status():
    data = request.json

    question = data.get('question')

    prompt = get_prompt()

    chain = prompt | llm | JsonOutputParser()

    response = chain.invoke({"input_msg":question})

    print(question)

    return response


if __name__ == "__main__":
    # app.run(debug=True)
    serve(app, host = "0.0.0.0", port = 8000, threads =1)
    
