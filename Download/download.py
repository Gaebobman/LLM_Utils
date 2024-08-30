from huggingface_hub import snapshot_download
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_id', type=str, help='Huggingface Model ID', required=True)
    parser.add_argument('--download_path', type=str, default="downloaded_models", help='The folder name used to save model')
    parser.add_argument('--revision', type=str, default='main')
    args = parser.parse_args()
    
    model_id = args.model_id
    download_path = f"{args.download_path}/{model_id}" if args.download_path is not None else model_id
    
    snapshot_download(repo_id=model_id, local_dir=download_path, revision="main")