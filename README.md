<h3> Usage </h3>

Install requirements

```bash
pip install -r requirements.txt
```
Download model from HuggingFace
```bash
python Download/Download.py --python download.py --model_id <HuggingFace_Model_ID> 
```

Convert model to GGUF format
```bash
python llama.cpp/convert_hf_to_gguf.py <MODEL_PATH> --outfile <llama.cpp/models/{MODEL_NAME}.gguf> --outtype <QUANTIZE>
```


---
References
- https://github.com/ggerganov/llama.cpp/discussions/2948