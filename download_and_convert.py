from huggingface_hub import snapshot_download
import argparse
import os
import subprocess

def download_model(model_id, download_path, revision):
    download_path = f"{download_path}/{model_id}" if download_path is not None else model_id
    if os.path.exists(download_path):
        user_input = input(f"Model '{model_id}' already exists at '{download_path}'. Do you want to re-download it? (y/n): ").strip().lower()
        if user_input == 'y':
            print(f"Re-downloading model '{model_id}'...")
            snapshot_download(repo_id=model_id, local_dir=download_path, revision=revision)
            print(f"Model '{model_id}' re-downloaded to '{download_path}'.")
        else:
            print(f"Skipping download. Using existing model at '{download_path}'.")
    else:
        snapshot_download(repo_id=model_id, local_dir=download_path, revision=revision)
        print(f"Model '{model_id}' downloaded to '{download_path}'.")
    return download_path

def convert_model_to_gguf(llama_cpp_path, model_path, quantize):
    model_name = os.path.basename(model_path)  # 모델 경로에서 모델 이름 추출
    convert_script = os.path.join(llama_cpp_path, "convert_hf_to_gguf.py")  # 변환 스크립트 경로 설정
    output_directory = os.path.join(llama_cpp_path, "models")  # 모델 저장 폴더 경로 설정
    output_file = os.path.join(output_directory, f"{model_name}.gguf")  # 출력 파일 경로 설정

    subprocess.run([
        "python", convert_script, model_path,
        "--outfile", output_file,
        "--outtype", quantize
    ], check=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_id', type=str, help='Huggingface Model ID', required=True)
    parser.add_argument('--download_path', type=str, default="./Download/downloaded_models", help='The folder name used to save model')
    parser.add_argument('--revision', type=str, default='main')
    parser.add_argument('--llama_cpp_path', type=str, default='llama.cpp/', help='The path to the llama.cpp directory')
    parser.add_argument('--quantize', type=str, default='f16', help='Quantization type for GGUF model (e.g., f16, q4_0)')
    args = parser.parse_args()
    
    # Step 1: Download the model
    model_path = download_model(args.model_id, args.download_path, args.revision)
    
    # Step 2: Convert the model to GGUF format
    convert_model_to_gguf(args.llama_cpp_path, model_path, args.quantize)