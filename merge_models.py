#验证SDK token
from modelscope.hub.api import HubApi
api = HubApi()
api.login('a685a6a2-3dc7-4266-bc7a-369789e29245')

#模型下载
from modelscope import snapshot_download
model_dir = snapshot_download('dtiosd/mymodels')

# python llm/llama.cpp/convert.py 刚才下载好的模型文件地址 --outtype f16 --outfile 保存的文件名.bin
 
# python ollama/llm/llama.cpp/convert_hf_to_gguf.py D:\ollama_models\mymodels --outtype f16 --outfile D:\ollama_models\mymodels.bin
# ollama create mymodels -f D:\ollama_models\test.Modelfile
