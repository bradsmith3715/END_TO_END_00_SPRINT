# 01-ai-engineering-bootcamp

Welcome to the first sprint of End-to-End AI Engineering bootcamp! This sprint is dedicated to setting up your development environment and making sure that all configuration works as intended.

We strongly recomend you coding along the video available on Maven rather than just cloning the repository and running the code.

If you do need to run the code, this is how:

- Clone the repository.
- Run:
```bash
cp env.example .env
```

Edit `.env` and add your API keys:

```
OPENAI_API_KEY=your_google_api_key
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
```

To build the project, run:

```bash
make build-docker-streamlit
```

To run the project:

```bash
make run-docker-streamlit
```



## This repository uses data provided by the authors of the following paper.
If you use this work, please cite:

```
@article{hou2024bridging,
  title={Bridging Language and Items for Retrieval and Recommendation},
  author={Hou, Yupeng and Li, Jiacheng and He, Zhankui and Yan, An and Chen, Xiusi and McAuley, Julian},
  journal={arXiv preprint arXiv:2403.03952},
  year={2024}
}
```
