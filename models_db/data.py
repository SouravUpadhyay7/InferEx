"""
models_db/data.py
-----------------
Single source of truth for all AI model entries in the ModelHub.
Add new models here — the rest of the app picks them up automatically.
"""

MODELS_DB = [
    {
        "id": "linear-regression-housing",
        "category": "ML Models",
        "subcategory": "Regression",
        "name": "Housing Price Predictor",
        "description": "A classic linear regression model trained on the Boston Housing dataset to predict real-estate values with high accuracy.",
        "dataset_description": "Boston Housing Dataset: Contains 506 samples with 14 features including crime rate, property tax, and pupil-teacher ratio. Used for predicting real estate values.",
        "model_explanation": "Linear regression models the relationship between a scalar response and one or more explanatory variables to predict the median value of owner-occupied homes.",
        "performance_metrics": {
            "Accuracy (R2)": "0.74",
            "RMSE": "4.8"
        },
        "model_file": "linear_regression.pkl",
        "notebook_file": "training_lr.ipynb",
        "visualization_url": "/static/images/regression.png"
    },
    {
        "id": "kmeans-customer-segmentation",
        "category": "ML Models",
        "subcategory": "Clustering",
        "name": "Customer Segmentation (K-Means)",
        "description": "Groups customers based on purchasing behavior using K-Means clustering — ideal for marketing and personalization strategies.",
        "dataset_description": "Mall Customer Segmentation Data: Features include Age, Annual Income, and Spending Score for 200 customers aiming to find distinct segments.",
        "model_explanation": "K-Means separates data into k mutually exclusive clusters to discover hidden patterns in customer spending habits, learning group representations.",
        "performance_metrics": {
            "Silhouette Score": "0.68",
            "Inertia": "2.44e4"
        },
        "model_file": "kmeans_clustering.pkl",
        "notebook_file": "segmentation_kmeans.ipynb",
        "visualization_url": "/static/images/clustering.png"
    },
    {
        "id": "random-forest-fraud",
        "category": "ML Models",
        "subcategory": "Classification",
        "name": "Fraud Detection (Random Forest)",
        "description": "An ensemble random forest classifier for detecting fraudulent credit card transactions in highly imbalanced datasets.",
        "dataset_description": "Kaggle Credit Card Fraud Dataset: 284,807 transactions of which 492 are frauds (0.17%). Features are PCA-transformed for privacy.",
        "model_explanation": "Random Forest builds multiple decision trees and merges them to get a more accurate and stable prediction, excelling at handling class imbalance with weighted voting.",
        "performance_metrics": {
            "F1 Score": "0.91",
            "ROC-AUC": "0.98"
        },
        "model_file": "random_forest_fraud.pkl",
        "notebook_file": "fraud_rf.ipynb",
        "visualization_url": "/static/images/regression.png"
    },
    {
        "id": "resnet50-image-classifier",
        "category": "Deep Learning",
        "subcategory": "Computer Vision",
        "name": "ResNet-50 Image Classifier",
        "description": "A deep convolutional neural network pre-trained on ImageNet for image classification across 1000 object categories.",
        "dataset_description": "ImageNet Data: Massive dataset containing 1.2 million high-resolution images across 1000 categories, providing robust visual features.",
        "model_explanation": "ResNet-50 uses residual blocks to avoid the vanishing gradient problem, enabling deep networks to learn complex image representations layer by layer.",
        "performance_metrics": {
            "Top-1 Accuracy": "76.1%",
            "Top-5 Accuracy": "92.8%"
        },
        "model_file": "resnet50.pth",
        "notebook_file": "vision_resnet.ipynb",
        "visualization_url": "/static/images/regression.png"
    },
    {
        "id": "yolov8-object-detection",
        "category": "Deep Learning",
        "subcategory": "Object Detection",
        "name": "YOLOv8 Object Detector",
        "description": "State-of-the-art real-time object detection model capable of identifying and localizing multiple objects in a single pass.",
        "dataset_description": "COCO Dataset: 330K images across 80 object categories, annotated with bounding boxes and segmentation masks for robust detection training.",
        "model_explanation": "YOLOv8 frames detection as a single regression problem, predicting bounding boxes and class probabilities directly from pixels in one evaluation.",
        "performance_metrics": {
            "mAP@50": "53.9%",
            "Inference Speed": "0.9ms"
        },
        "model_file": "yolov8n.pt",
        "notebook_file": "yolov8_detect.ipynb",
        "visualization_url": "/static/images/clustering.png"
    },
    {
        "id": "bert-sentiment-analysis",
        "category": "NLP Projects",
        "subcategory": "Text Classification",
        "name": "BERT Sentiment Analyzer",
        "description": "Fine-tuned BERT model to predict positive or negative sentiment from movie reviews with state-of-the-art accuracy.",
        "dataset_description": "IMDB Dataset: 50,000 highly polar movie reviews for binary sentiment classification, balanced carefully between positive and negative.",
        "model_explanation": "BERT is a transformer-based model that captures bidirectional context, allowing profound understanding of language nuance and semantic meaning.",
        "performance_metrics": {
            "F1 Score": "0.94",
            "Accuracy": "94.2%"
        },
        "model_file": "bert_sentiment.bin",
        "notebook_file": "nlp_bert_finetune.ipynb",
        "visualization_url": "/static/images/clustering.png"
    },
    {
        "id": "ner-spacy-biomedical",
        "category": "NLP Projects",
        "subcategory": "Named Entity Recognition",
        "name": "BioMedical NER (spaCy)",
        "description": "A spaCy-based Named Entity Recognition model fine-tuned on biomedical literature to extract diseases, drugs, and genes.",
        "dataset_description": "BC5CDR Corpus: 1500 PubMed articles annotated for chemical and disease entities — a standard benchmark in biomedical NLP.",
        "model_explanation": "spaCy's transformer pipeline uses a pre-trained BioBERT backbone, enabling rich contextual embeddings specialized for biomedical vocabulary and domain jargon.",
        "performance_metrics": {
            "Entity F1": "0.89",
            "Precision": "0.91"
        },
        "model_file": "bio_ner_spacy.zip",
        "notebook_file": "bio_ner_train.ipynb",
        "visualization_url": "/static/images/regression.png"
    },
    {
        "id": "gpt-mini-text-gen",
        "category": "Generative AI",
        "subcategory": "Text Generation",
        "name": "GPT-Mini Story Teller",
        "description": "A lightweight generative transformer model for creating short fantasy stories based on standard text generation loops.",
        "dataset_description": "Project Gutenberg Fantasy Corpus: Over 500 MB of classic fantasy literature cleaned and tokenized using BPE encoding.",
        "model_explanation": "Decodes tokens autoregressively using self-attention to generate coherent and creative text following a provided prompt, balancing brevity and creativity.",
        "performance_metrics": {
            "Perplexity": "18.5",
            "BLEU Score": "N/A"
        },
        "model_file": "gpt_mini.onnx",
        "notebook_file": "genai_transformer.ipynb",
        "visualization_url": "/static/images/regression.png"
    },
    {
        "id": "stable-diffusion-finetuned",
        "category": "Generative AI",
        "subcategory": "Image Generation",
        "name": "Stable Diffusion (Fine-tuned)",
        "description": "A diffusion model fine-tuned on anime-style artwork using DreamBooth, capable of high-fidelity stylized image generation.",
        "dataset_description": "Custom Anime Art Dataset: ~1200 curated high-resolution illustrations used for DreamBooth fine-tuning to teach unique artistic style.",
        "model_explanation": "Stable Diffusion iteratively denoises a latent representation guided by CLIP text embeddings, generating images that match textual descriptions with creative flair.",
        "performance_metrics": {
            "FID Score": "12.4",
            "CLIP Similarity": "0.83"
        },
        "model_file": "sd_anime_dreambooth.safetensors",
        "notebook_file": "sd_dreambooth.ipynb",
        "visualization_url": "/static/images/clustering.png"
    },
    {
        "id": "drl-agentic-robot",
        "category": "Agentic AI",
        "subcategory": "Reinforcement Learning",
        "name": "PPO Robot Navigator",
        "description": "An autonomous agent trained with Proximal Policy Optimization to navigate continuous physical mazes with near-perfect success rate.",
        "dataset_description": "Environment Simulation: Millions of interaction steps generated dynamically within a custom physics grid environment using Ray RLlib.",
        "model_explanation": "PPO strikes a delicate balance between ease of tuning and sample complexity while strictly avoiding large policy updates that historically hurt learning stability.",
        "performance_metrics": {
            "Average Reward": "98.5",
            "Success Rate": "99.2%"
        },
        "model_file": "ppo_agent.zip",
        "notebook_file": "agentic_ppo_train.ipynb",
        "visualization_url": "/static/images/clustering.png"
    }
]

# Category metadata for the landing page showcase
CATEGORIES = [
    {
        "id": "ml-models",
        "filter": "ML Models",
        "label": "ML Models",
        "icon": "🧠",
        "description": "Supervised & unsupervised classical machine learning algorithms — regression, classification, clustering and more.",
        "color": "#7c3aed"
    },
    {
        "id": "deep-learning",
        "filter": "Deep Learning",
        "label": "Deep Learning",
        "icon": "🔬",
        "description": "CNNs, ResNets, YOLO and other deep neural architectures for computer vision and complex pattern recognition.",
        "color": "#db2777"
    },
    {
        "id": "nlp-projects",
        "filter": "NLP Projects",
        "label": "NLP Projects",
        "icon": "💬",
        "description": "Transformer-based models for sentiment analysis, named entity recognition, text classification and more.",
        "color": "#0891b2"
    },
    {
        "id": "generative-ai",
        "filter": "Generative AI",
        "label": "Generative AI",
        "icon": "✨",
        "description": "GPT-style text generators, diffusion image models, and creative AI systems that produce novel content.",
        "color": "#ea580c"
    },
    {
        "id": "agentic-ai",
        "filter": "Agentic AI",
        "label": "Agentic AI",
        "icon": "🤖",
        "description": "Reinforcement learning agents and autonomous AI systems that learn to act in complex dynamic environments.",
        "color": "#16a34a"
    }
]
