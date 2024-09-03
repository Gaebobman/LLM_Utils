# Model Download and Conversion Script

This script allows you to download a model from HuggingFace and convert it to GGUF format using a specified conversion script.

Requirements

Make sure to install the necessary Python packages before running the script. You can do this by running:

```bash
pip install -r requirements.txt
```
Usage

0.	Clone the llama.cpp Repository:
Before using the script, you need to clone the llama.cpp repository and install its dependencies. You can do this by running:

```bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
pip install -r requirements.txt
cd ..
```

1. Download the Model and Convert to GGUF Format

To download a model from HuggingFace and convert it to GGUF format, use the following command:

```bash
python download_and_convert.py --model_id <HuggingFace_Model_ID> --llama_cpp_path <path_to_llama_cpp_directory> --quantize <QUANTIZE_TYPE>
```
2. Optional Arguments:

	•	--model_id: (Required) The HuggingFace model ID that you want to download.
	•	--download_path: (Optional) The folder name where the model will be saved. The default is ./Download/downloaded_models.
	•	--revision: (Optional) The specific model version to download (default: main).
	•	--llama_cpp_path: (Optional) The path to the llama.cpp directory. This is where the conversion script is located and where the converted model will be saved. The default is llama.cpp/.
	•	--quantize: (Optional) The quantization type for the GGUF model (e.g., f16, q4_0). The default is f16.

Example Command

Here’s an example of how to use the script:

```bash
python script_name.py --model_id EleutherAI/gpt-neo-125M --llama_cpp_path /path/to/llama.cpp --quantize q4_0
```

In this example:

	•	The script downloads the gpt-neo-125M model from HuggingFace.
	•	The model is saved in the ./Download/downloaded_models/EleutherAI/gpt-neo-125M folder.
	•	The model is converted to GGUF format and saved as gpt-neo-125M.gguf in the /path/to/llama.cpp/models/ directory using q4_0 quantization.

Additional Feature:

	•	If the model is already downloaded: The script will prompt you to confirm whether you want to re-download the model. If you choose “n”, the existing model will be used for conversion.
<br>

---
References

For more information on the conversion script and GGUF format, check the  <a href ="https://github.com/ggerganov/llama.cpp/discussions/2948"> Llama.cpp discussions</a>.