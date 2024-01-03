#=====这个py把字典保存下来,用来观看.

import transformers
from transformers import AutoTokenizer, AutoModel
import transformers.audio_utils
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
#加上这行之后又恢复以前的速度了!
tokenizer = AutoTokenizer.from_pretrained("./", trust_remote_code=True)
open('aaa','w',encoding='utf-8').write(str(tokenizer.get_vocab())) #====保存vocab.

print(1)