# mymodel
微调Qwen2:1.5B自我认知  
ollama模型存放  
https://ollama.com/dtiosd/study  
魔塔社区模型存放  
https://www.modelscope.cn/models/dtiosd/mymodels  





  ### 1.下载ollama源码  
https://github.com/ollama/ollama/tree/main

### 2.下载llama.cpp源码  
https://github.com/ggerganov/llama.cpp

### 3.下载环境  
pip install ./llm/llama.cpp/requirements.txt

### 4.在ollama项目下  
这是自己模型的路径  
D:\ollama_models\mymodels  
这是生成的模型的路径  
D:\ollama_models\mymodels.bin  
python ollama/llm/llama.cpp/convert_hf_to_gguf.py D:\ollama_models\mymodels --outtype f16 --outfile D:\ollama_models\mymodels.bin

### 5.配置文件，生成ollama文件  
创建配置文件test.Modelfile  
配置文件内容：  
```
FROM D:\ollama_models\mymodels.bin  
  
TEMPLATE """{{ if .System }}<|im_start|>system  
{{ .System }}<|im_end|>{{ end }}<|im_start|>user  
{{ .Prompt }}<|im_end|>  
<|im_start|>assistant  
"""  
   
PARAMETER stop "<|im_start|>"  
PARAMETER stop "<|im_end|>"  
```

生成ollama文件  
这是配置文件的路径  
D:\ollama_models\test.Modelfile    
ollama create mymodels -f D:\ollama_models\test.Modelfile  
  
  
  
  
参考文档  
https://blog.csdn.net/spiderwower/article/details/138506271  
https://blog.csdn.net/m0_73365120/article/details/141901776
