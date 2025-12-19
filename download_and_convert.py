from main import run

if __name__ == "__main__":
    # Backward-compatible entrypoint: always convert unless explicitly disabled with --no-convert.
    run(default_convert=True)
