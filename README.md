# 🔍 Prompt Diff

A lightweight Python CLI tool for comparing two versions of a prompt and identifying added or removed words.

## Features

- Compare two prompts
- Detect added words
- Detect removed words
- Count words in both versions
- No external dependencies

## Run

```bash
python main.py
```

## Example

```text
Old prompt:
> Create a Python chatbot for students

New prompt:
> Create an AI Python chatbot for college students

📊 Changes
========================================

Added words   : ['AI', 'college']
Removed words : ['for']
Old words     : 6
New words     : 8
```

## Built With

- Python
- Sets
- String processing
