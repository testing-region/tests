# Notes for Depression Detection System

## Natural Language Processing (NLP)

- Ability to understand text and spoken words the way humans can.

### Sentiment Analysis

- Process of analysing digital text to determine if the emotional tone of
  the text is positive, negative or neutral.

## Traditional NLP Process

### Preprocessing

#### Tokenizing

- Work with smaller pieces of text that still are relatively coherent and
  meaningful outside of the context of the rest of the text.
- Tokenize by word or sentence.

#### Filtering Stop Words

- E.g. is, in, an.

## Exploratory Data Analysis

- Check for the existence of bias.
- Dataset1 was biased towards people who did not have depression.
  (79% difference)
- Dataset2 was fairly balanced with no bias towards those with depression
  and those with none. (0.89% difference)
- Dataset2 was already clean and have undergone preprocessing.

## Feature Engineering

All features.

## Vertex AI

- An ML platform that lets you train and deploy ML models and AI applications,
  and customize large language models.
- We used it to fine-tune PaLM2 text-bison model.

### Fine Tuning Workflow

1. Data preparation.
2. Model training.
3. Model evaluation and iteration.
4. Model deployment and serving.
5. Model Monitoring.

#### Dataset Preparation

- Format for training and evaluation: {"input_text": "", "output_text": ""}
- Format for testing: {"prompt": "", "ground_truth": ""}
- They all have to be text. 0 and 1 was encoded to "no" and "yes" respectively.
- Made sure target feature is evenly distributed. (stratify).
- 1000 rows for optimum results. (less will not perform well, and possible
  over-fitting if it is greater.)

#### Model Training

- Fine-tune text-bison model.

#### Model Evaluation

- Area under the Precision-Recall Curve (AuPRC): Higher value indicates higher
  quality model.
- Log Loss: Cross entropy between the model predictions and target values.
- Recall: True positive rate.
- Precision: Fraction of classification predictions produced by the model
  that were correct.
- F1 Score: Harmonic mean of precision and recall. (Balance)
- Confusion matrix: Shows how often a model correctly predicted a result.

## What is PaLM2?

- Pathway Language Model 2 (PaLM2) is an LLM developed by Google AI this year.
- Features:

  - Multilingual capabilities.
  - Improved reasoning and problem solving.
  - Responsible AI development: rigorously evaluates potential biases
    and harms before deployment.

- The same LLM that has been fine-tuned to power Google Bard, Google
  Assistant, Search and Translate.

### Text-Bison Model

- A model variation within PaLM2 architecture. (Others include code-bison,
  chat-bison, and more...)
- Falls within the mid-range size of PaLM2 and offers a balance between
  performance and efficiency.
- Capabilities (NLP tasks):

  - Text generation.
  - Information extraction.
  - Data extraction.
  - Problem solving.
  - Recommendations generation.
  - AI agents.
