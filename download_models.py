from modelscope.hub.snapshot_download import snapshot_download
import os

# 或者使用相对路径（相对于项目根目录）
base_dir = "./engines/InsightEngine/models"

print("=" * 50)
print("开始下载模型...")
print("=" * 50)

# ========== 1. 下载聚类模型 ==========
print("\n[1/2] 正在下载聚类模型: paraphrase-multilingual-MiniLM-L12-v2")
try:
    # 聚类模型单独一个目录
    cluster_dir = os.path.join(base_dir, "paraphrase-multilingual-MiniLM-L12-v2")
    os.makedirs(cluster_dir, exist_ok=True)

    model_dir_1 = snapshot_download(
        model_id="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        cache_dir=cluster_dir,
        revision="master"
    )
    print(f"✓ 聚类模型已下载到：{model_dir_1}")
except Exception as e:
    print(f"✗ 聚类模型下载失败：{e}")

# ========== 2. 下载情感分析模型 ==========
print("\n[2/2] 正在下载情感分析模型: tabularisai/multilingual-sentiment-analysis")
try:
    # 情感分析模型单独一个目录
    sentiment_dir = os.path.join(base_dir, "multilingual-sentiment-analysis")
    os.makedirs(sentiment_dir, exist_ok=True)

    model_dir_2 = snapshot_download(
        model_id="tabularisai/multilingual-sentiment-analysis",
        cache_dir=sentiment_dir,
        revision="master"
    )
    print(f"✓ 情感分析模型已下载到：{model_dir_2}")
except Exception as e:
    print(f"✗ 情感分析模型下载失败：{e}")

print("\n" + "=" * 50)
print("下载完成！")
print("=" * 50)
print(f"模型目录：{base_dir}")