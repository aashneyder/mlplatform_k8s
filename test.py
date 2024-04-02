# train.py
# import subprocess
# packages = ["mlflow", "mlserver", "boto3"]
# subprocess.check_call(["pip", "install"] + packages)

import mlflow
from mlserver.types import InferenceResponse, InferenceRequest
from mlserver.codecs.string import StringRequestCodec
from requests.models import Response
import json
import numpy as np

ip = "localhost"
mlflow.set_tracking_uri(f"http://{ip}:5000")
class MyModel(mlflow.pyfunc.PythonModel):
    def predict(self, context, request_input):
        print(f"Полученный predict запрос: {request_input}, тип: {type(request_input)}")
        model_input = self.decode_request(request_input)
        print(f"Результат decode_request для передачи в модель: {model_input}, тип: {type(model_input)}")
        model_output = self.my_custom_function(model_input)
        print(f"Результат работы модели (my_custom_function): {model_output}, тип: {type(model_output)}")
        inference_response = self.encode_response_model(model_output)
        print(f"Обработанный ответ модели для передачи mlserver: {request_input}, тип: {type(request_input)}")
        return inference_response
 
    def my_custom_function(self, model_input: dict) -> dict:
        model_output = {"result": model_input["a"] * 2}
        return model_output
 
    def decode_request(self, model_input: InferenceRequest) -> dict:
        raw_json = StringRequestCodec.decode_request(model_input)
        print(f"raw_json = {raw_json}, тип raw_json: {type(raw_json)}")
        print(f"raw_json[0] = {raw_json[0]}, тип raw_json[0] : {type(raw_json[0])}")
        _input = json.loads(raw_json[0])
        return _input
        
    def encode_response_model(self, model_output: dict) -> dict:
        _output = json.dumps(model_output)
        print(f"_output = {_output}, тип _output: {type(_output)}")
        _output_np = np.array(_output, dtype='object')
        print(f"_output_np = {_output_np}, тип _output_np: {type(_output_np)}")
        inference_response = {"output": _output_np}
        return inference_response

my_model = MyModel()
model_path = "work_model3"
reg_model_name = "work_model3"

with mlflow.start_run(run_name="run_work_model1_v3") as run:
    model_path = f"{model_path}"
    mlflow.pyfunc.save_model(path=model_path, python_model=my_model)
    mlflow.pyfunc.log_model(artifact_path=model_path, python_model=my_model, registered_model_name=reg_model_name)

