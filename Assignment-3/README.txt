Description of All Files:
1) indic_trans.ipynb, nllb.ipynb and chat_gpt.ipynb:
Above files are translating dataset into respected target languages and then saving the required translated text

2) indic_trans_eval.ipynb, nllb_eval.ipynb and chat_gpt_eval.ipynb
Above files import the translated text and reference text and compute BLEU and ROUGE scores

Result based on BLEU score for corpus is fairly high but for many sentences BLEU score is very low. Still it doesn't reflect that the translation is incorrect but because BLEU relies on n-gram matching. So even if translation is perfectly fine it may recieve less BLEU score. BLEU score is not so suitable for free order language like indic languages.

ROUGE has more variants and different scores. BLEU only relied on precision for n-grams. Where ROUGE has 1-gram, 2-gram, L-gram(longest common subsequence) and even in that it captures Precision, Recall and F-score.

But it is also kind of order-restrictive score so It might not capture whether translation are perfect or not. But you can see ROUGE unigram score... It can tell us a lot about it.