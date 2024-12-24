from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = "D:/mymodels"
converted_path = "D:/converted_model"

# 加载 Qwen2 模型
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True)

# 保存为 Hugging Face 的 PyTorch 格式
model.save_pretrained(converted_path)
tokenizer.save_pretrained(converted_path)

print(f"模型已保存到 {converted_path}")