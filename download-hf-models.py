# huggingface download model repo
import os
import time
import traceback
import argparse
from loguru import logger
from hf_token import hf_token

parser = argparse.ArgumentParser()
parser.add_argument("--use-mirror", action="store_true")
args = parser.parse_args()
if args.use_mirror:
    os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from huggingface_hub import snapshot_download

model_repos = [
    "Qwen/Qwen2-72B-Instruct",
    "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "meta-llama/Meta-Llama-3.1-70B-Instruct",
    "deepseek-ai/deepseek-math-7b-instruct",
    "deepseek-ai/deepseek-math-7b-base",
    "deepseek-ai/deepseek-math-7b-rl",
    "deepseek-ai/DeepSeek-Prover-V1.5-Base",
    "deepseek-ai/DeepSeek-Prover-V1.5-SFT",
    "deepseek-ai/DeepSeek-Prover-V1.5-RL",
    "Qwen/Qwen2.5-72B-Instruct",
    "Qwen/Qwen2.5-72B-Instruct-GPTQ-Int4",
    "Qwen/Qwen2.5-72B-Instruct-GPTQ-Int8",
    "Qwen/Qwen2.5-Coder-7B-Instruct",
]
logger.add("download.log")

trial_num = 10
for model_repo in model_repos:
    model_local_path = "models/" + model_repo.split("/")[-1]
    while trial_num > 0:
        try:
            snapshot_download(
                repo_id=model_repo,
                local_dir=model_local_path,
                repo_type="model",
                token=hf_token,
            )
            logger.info(f"Downloaded {model_repo}")
            break
        except Exception as e:
            logger.error(f"Error: {e}")
            logger.error(traceback.format_exc())
            trial_num -= 1
            time.sleep(5)

