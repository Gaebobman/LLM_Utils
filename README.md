# Model Download and Conversion Script

Download a Hugging Face model and convert it to GGUF with the llama.cpp tooling.

## Setup (uv)

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if you do not have it yet.
- Install project dependencies (Python 3.12+):

```bash
uv sync
```

## Authentication (Hugging Face)

Private/gated model downloads require a Hugging Face token to be available in the shell environment.

Recommended:

```bash
# ~/.zshrc
export HF_TOKEN=hf_xxx_your_token
```

Apply it to the current shell (or open a new terminal):

```bash
source ~/.zshrc
```

Quick verification:

```bash
uv run python -c "from huggingface_hub import whoami; print(whoami())"
```

If this prints your account info, `uv run python main.py ...` will use the same token.

- Prepare llama.cpp (use the same environment so `huggingface-hub` is available):

```bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
uv run python -m pip install -r requirements.txt
cd ..
```

## Usage

### Download (optional convert to GGUF)

```bash
uv run python main.py --model_id <huggingface_model_id> [--download_path <path>] [--revision <rev>] [--force] [--convert] [--llama_cpp_path <path_to_llama.cpp>] [--quantize <type>]
```

Important flags:
- `--convert` / `--no-convert`: toggle GGUF conversion (default: no conversion).
- `--llama_cpp_path`: path to your `llama.cpp` checkout (default: `./llama.cpp`); used when converting.
- `--quantize`: GGUF quantization type, e.g. `f16` (default) or `q4_0`.
- `--force`: re-download even if the target path already exists.

Example (download + convert):

```bash
uv run python main.py --model_id EleutherAI/gpt-neo-125M --llama_cpp_path ./llama.cpp --quantize q4_0 --convert
```

Behavior:
- If the model already exists locally, the script asks whether to re-download; answering `n` reuses the existing files.

### Compatibility entrypoint

`download_and_convert.py` remains available; it behaves the same as `main.py --convert` by default:

```bash
uv run python download_and_convert.py --model_id <huggingface_model_id> --llama_cpp_path <path_to_llama.cpp> --quantize q4_0
```

## References

- [llama.cpp GGUF discussion](https://github.com/ggerganov/llama.cpp/discussions/2948)
