# Trying 2 methods.
## Use algorithms that detect similarity of images
1. Crop the heading part of images 
2. Find a pretrained feature vector online on tfhub.dev or other sources.
3. Run these pretrained feature vectors on all the templates ( training data) , and store them.
4. Take any input from the input folder ( test set), get its feature vectors.
5. Using distance metric like Euclidean, Manhattan to find which image in template is nearest to the Input

## Use Doc2vec algorithm after extracting text using OCR API.
1. Two documents which have the most similar Doc2Vec embeddings are similar documents.

## TODO
1. Add tags while training, return tags during prediction
2. Predict multiple files at the same time, return a dictionary of outputs
3. Find if there is a function in gensim for prediction, instead of manually calcuating distances
