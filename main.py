import argparse
import os
import subprocess
from typing import Sequence

from huggingface_hub import snapshot_download


def download_model(model_id: str, download_path: str | None, revision: str, force: bool = False) -> str:
    target_path = f"{download_path}/{model_id}" if download_path is not None else model_id

    if os.path.exists(target_path) and not force:
        choice = input(
            f"Model '{model_id}' already exists at '{target_path}'. Re-download? (y/n): "
        ).strip().lower()
        if choice != "y":
            print(f"Skipping download. Using existing model at '{target_path}'.")
            return target_path

    snapshot_download(repo_id=model_id, local_dir=target_path, revision=revision)
    print(f"Model '{model_id}' downloaded to '{target_path}'.")
    return target_path


def convert_model_to_gguf(llama_cpp_path: str, model_path: str, quantize: str) -> str:
    model_name = os.path.basename(model_path)
    convert_script = os.path.join(llama_cpp_path, "convert_hf_to_gguf.py")
    output_directory = os.path.join(llama_cpp_path, "models")
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, f"{model_name}.gguf")

    subprocess.run(
        [
            "python",
            convert_script,
            model_path,
            "--outfile",
            output_file,
            "--outtype",
            quantize,
        ],
        check=True,
    )
    print(f"Model '{model_name}' converted to GGUF at '{output_file}'.")
    return output_file


def parse_args(argv: Sequence[str] | None = None, default_convert: bool = False) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download a Hugging Face model, optionally convert to GGUF.")
    parser.add_argument("--model_id", required=True, help="Hugging Face model ID.")
    parser.add_argument(
        "--download_path",
        default="./Download/downloaded_models",
        help="Folder to store the model (defaults to ./Download/downloaded_models/<model_id>).",
    )
    parser.add_argument("--revision", default="main", help="Model revision to download.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-download even if the target path already exists.",
    )
    parser.add_argument(
        "--convert",
        action=argparse.BooleanOptionalAction,
        default=default_convert,
        help="Also convert the downloaded model to GGUF using llama.cpp.",
    )
    parser.add_argument(
        "--llama_cpp_path",
        default="./llama.cpp",
        help="Path to the llama.cpp directory (used when converting).",
    )
    parser.add_argument(
        "--quantize",
        default="f16",
        help="GGUF quantization type (e.g., f16, q4_0). Used when converting.",
    )
    return parser.parse_args(argv)


def run(argv: Sequence[str] | None = None, default_convert: bool = False) -> None:
    args = parse_args(argv, default_convert)
    model_path = download_model(
        model_id=args.model_id,
        download_path=args.download_path,
        revision=args.revision,
        force=args.force,
    )

    if args.convert:
        convert_model_to_gguf(args.llama_cpp_path, model_path, args.quantize)


def main() -> None:  # CLI entry point
    run()


if __name__ == "__main__":
    main()
