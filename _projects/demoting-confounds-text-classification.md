---
title: Demoting Spurious Confounds in Text Classification

description: |
  We develop methods of discovering and demoting latent confounds in text classifcation which correspond to superficial patterns specific to the training set but don't generalize well.

people:
  - sachin
  - anjalie

layout: project
image: /img/project/deconfound.png
code: 
  - https://github.com/Sachin19/adversarial-classify
paper:
  - title: "Topics to Avoid: Demoting Latent Confounds in Text Classification"
    url: https://arxiv.org/abs/1909.00453
  - title: "Demoting Racial Bias in Hate Speech Detection"
    url: https://www.aclweb.org/anthology/2020.socialnlp-1.2/
last-updated: 2020-01-11
---

Despite impressive performance on many text classification tasks, deep neural networks tend to learn frequent superficial patterns that are specific to the training data and do not always generalize well. In this work, we observe this limitation with respect to the task of native language identification. We find that standard text classifiers which perform well on the test set end up learning topical features which are confounds of the prediction task (e.g., if the input text mentions Sweden, the classifier predicts that the author’s native language is Swedish). We propose a method that represents the latent topical confounds and a model which “unlearns” confounding features by predicting both the label of the input text and the confound; but we train the two predictors adversarially in an alternating fashion to learn a text representation  that predicts the correct label but is less prone to using information about the confound. We show that this model  generalizes better and learns features that are indicative of the writing style rather than the content.

## Demoting Racial Bias in Hate Speech Detection