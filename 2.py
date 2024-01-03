# 这个py用来debug 模型的结构. 压缩了模型, 让普通电脑都可以运行了.
from modeling_chatglm import ChatGLMForConditionalGeneration
import torch
 
from configuration_chatglm import ChatGLMConfig

llamamodel = ChatGLMForConditionalGeneration(ChatGLMConfig(num_layers=2,original_rope=True,use_cache=True))
inputs_ids  = torch.randint(low=0,high=65024, size=(4,30))
res = llamamodel(inputs_ids)
print(res)
