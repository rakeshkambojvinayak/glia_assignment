# Glia Assignment

# Model Training and Deployment

I have trained two versions of the classification model:
- One utilizing GloVe embeddings: [classification_assignment_glove.ipynb](link-to-notebook-glove)
- Another without using GloVe embeddings: [classification_assignment.ipynb](link-to-notebook-without-glove)

The version without GloVe embeddings achieved an impressive validation accuracy of 95% on the 7th epoch. 
The model with GloVe training is in progress, and I will share the updated file soon.

**Note**: The trained models are large in size. You can download them from the following link:
[Trained Models on Google Drive](https://drive.google.com/file/d/1Q7jAkE0NYCyQ-VriAHjUMh7PA5ZFo6Oz/view?usp=sharing)
[Trained Models on Google Drive](https://drive.google.com/file/d/16LeflvVh7c0pwbm7No-WSQ16DdrzbnG8/view?usp=sharing)

I did not use any pre-trained LLM models, as I achieved satisfactory accuracy by coding the models from scratch.

## Running the Notebooks

To run the notebooks:
1. Launch Jupyter Notebook.
2. Uncomment and install all required libraries mentioned in the respective notebook files.

## Deployment as API Service

For instructions on deploying as an API service, please refer to the [/app/README.md](https://github.com/rakeshkambojvinayak/glia_assignment/tree/main/app) file.

