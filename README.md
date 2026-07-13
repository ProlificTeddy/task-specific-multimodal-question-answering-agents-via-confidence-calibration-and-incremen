# Task-Specific Multimodal Question Answering Agents for QANTA 2026

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/ArXiv-2607.09623v1-b31b1b.svg)](https://arxiv.org/pdf/2607.09623v1)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](https://github.com/yourusername/qanta-2026/issues)

---

## Overview

This repository contains the official implementation of the research paper **[Task-Specific Multimodal Question Answering Agents via Confidence Calibration and Incremental Reasoning for QANTA 2026](https://arxiv.org/pdf/2607.09623v1)** by Nirjhar Das and Md. Al-Mamun Provath. The paper introduces a novel approach to solving the **QANTA 2026 shared challenge** on multimodal quizbowl systems, which involves answering pyramid-style questions incrementally revealed through text and images.

The system is built around a **task-specific two-agent architecture**:
1. **Tossup Agent**: Focused on confidence-calibrated answering and numeric reasoning for early and accurate responses.
2. **Bonus Agent**: Designed for lead-in-aware reasoning, structured relational reasoning, and multimodal evidence integration to improve exact answer selection.

With this lightweight and efficient architecture, the system achieved the **highest leaderboard score of 0.402**, demonstrating the effectiveness of task-specific reasoning strategies under resource constraints.

---

## How It Works

The implementation is based on two core agents, each tailored to handle distinct tasks in the QANTA 2026 challenge:

### 1. Tossup Agent
- **Objective**: Decide when to answer under uncertainty.
- **Key Features**:
  - **Confidence Calibration**: The agent uses a confidence threshold to determine when it has enough certainty to answer the question.
  - **Numeric Reasoning Policy**: Reduces overconfident predictions by identifying and correctly interpreting isolated numeric clues in the question.
  - **Model**: Built on the lightweight `GPT-4o-mini-class` (GPT-4.1-mini) architecture for efficient inference.

### 2. Bonus Agent
- **Objective**: Focus on accurate answer selection and human adoption.
- **Key Features**:
  - **Leadin-Aware Reasoning**: Incorporates context from the question's lead-in to improve answer relevance.
  - **Structured Relational Reasoning**: Leverages structured relationships between entities for better comprehension.
  - **Multimodal Evidence Integration**: Combines textual and visual information to make informed decisions.
  - **Model**: Utilizes the more powerful `GPT-4o-class` (GPT-4.1) architecture for enhanced reasoning capabilities.

### Efficiency and Performance
- The system avoids reliance on retrieval pipelines or model ensembles, focusing instead on **lightweight reasoning policies** and **confidence calibration**.
- The architecture is designed to operate in a **hosted-only environment**, ensuring compliance with the competition's efficiency constraints.
- Achieved state-of-the-art performance on the QANTA 2026 leaderboard with a **Tossup score of 0.238** and a **Bonus Effect score of 0.164**.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/qanta-2026.git
   cd qanta-2026
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have Python 3.10 or higher installed.

---

## Usage

The main implementation is provided in the `implementation.py` script. Below are the instructions to run the Tossup and Bonus agents:

### Running the Tossup Agent
To run the Tossup agent on a sample dataset:
```bash
python implementation.py --task tossup --input data/tossup_sample.json --output results/tossup_predictions.json
```

- `--task`: Specifies the task (`tossup` or `bonus`).
- `--input`: Path to the input JSON file containing the questions.
- `--output`: Path to save the predictions.

### Running the Bonus Agent
To run the Bonus agent on a sample dataset:
```bash
python implementation.py --task bonus --input data/bonus_sample.json --output results/bonus_predictions.json
```

### Input Format
The input file should be a JSON file containing a list of questions. Each question should have the following structure:
```json
[
  {
    "id": "question_1",
    "text": "This is the text of the question...",
    "image": "path/to/image.jpg"
  },
  ...
]
```

### Output Format
The output file will be a JSON file containing the predictions for each question:
```json
[
  {
    "id": "question_1",
    "answer": "Predicted Answer",
    "confidence": 0.85
  },
  ...
]
```

---

## Example

To test the implementation with the provided sample data:
```bash
python implementation.py --task tossup --input data/tossup_sample.json --output results/tossup_predictions.json
python implementation.py --task bonus --input data/bonus_sample.json --output results/bonus_predictions.json
```

---

## Repository Structure

```
qanta-2026/
├── data/                     # Sample input data
│   ├── tossup_sample.json
│   ├── bonus_sample.json
├── results/                  # Output predictions
├── models/                   # Pre-trained model weights
├── implementation.py         # Main implementation script
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── LICENSE                   # License file
```

---

## Contributing

We welcome contributions to improve this project! Feel free to open an issue or submit a pull request. Please ensure that your code follows the repository's coding guidelines.

---

## Citation

If you use this code or find it helpful, please cite our paper:

```
@article{das2026qanta,
  title={Task-Specific Multimodal Question Answering Agents via Confidence Calibration and Incremental Reasoning for QANTA 2026},
  author={Nirjhar Das and Md. Al-Mamun Provath},
  journal={arXiv preprint arXiv:2607.09623v1},
  year={2026}
}
```

---

## License

This project is licensed under the [MIT License](LICENSE).