# AI Semantic File Search

A simple semantic file search system built with transformer-based embeddings.
This project allows you to find the most relevant text file based on a natural language query instead of exact keyword matching.

---

## Features

* Semantic search (understands meaning, not just keywords)
* Transformer-based text embeddings
* Cosine similarity for relevance ranking
* Works with multiple `.txt` files
* Simple and easy-to-understand implementation

---

## Technologies Used

* Python
* SentenceTransformers
* scikit-learn

---

## Project Structure

```
.
├── main.py
├── data/
│   ├── historia.txt
│   ├── mate.txt
│   └── programacion.txt
```

---

## How It Works

1. The program reads all `.txt` files from the `data/` folder
2. Each file is converted into a vector (embedding) using a transformer model
3. The user inputs a query in natural language
4. The query is also converted into a vector
5. Cosine similarity is used to compare the query with all files
6. The most relevant files are returned

---

## Usage

Install dependencies:

```bash
pip install sentence-transformers scikit-learn
```

Run the program:

```bash
python main.py
```

Enter a query, for example:

```
machine learning algorithms
```

---

## Example Output

```
Top 2 results found:

1. programacion.txt
   Similarity: 0.87
   Content: Introduction to programming concepts...

2. mate.txt
   Similarity: 0.42
   Content: Basic algebra and equations...
```

---

## Learning Purpose

This project was built as a learning exercise to understand key concepts in modern Natural Language Processing (NLP), including:

* Transformer-based models
* Text embeddings (vectorization)
* Semantic similarity search
* Cosine similarity

AI tools were used to assist in the implementation, but the main goal was to understand how these systems work in practice.

---

## What I Learned

* How transformer models represent text as numerical vectors
* The difference between semantic search and keyword-based search
* How cosine similarity measures relevance between texts
* How to structure a basic NLP pipeline

---

## Limitations

* Recomputes embeddings every time the program runs
* Only supports `.txt` files
* Loads full file content into memory
* Not optimized for large datasets

---

## Future Improvements

* Store embeddings to avoid recomputation
* Add support for PDFs and other file formats
* Improve performance for larger datasets
* Build a simple API or user interface

---
