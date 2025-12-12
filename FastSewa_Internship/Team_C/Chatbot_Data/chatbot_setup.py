import json
import nltk

# Download necessary NLTK data (only need to run this once)
nltk.download('punkt')
nltk.download('punkt_tab') 

# 1. Load the intents.json file
try:
    with open('intents.json', 'r') as file:
        data = json.load(file)
    print("✅ Success: intents.json loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: Could not find 'intents.json'. Make sure it's in the same folder.")
    exit()

# 2. Process the data
words = []          
classes = []        
documents = []      

print("--- Processing Data ---")
for intent in data['intents']:
    for pattern in intent['patterns']:
        # Tokenize (split sentence into words)
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# 3. Output the results
print(f"-> Found {len(documents)} sentences.")
print(f"-> Found {len(classes)} categories: {classes}")
print(f"-> Found {len(words)} unique words.")
print("\n✅ Setup Complete. Your data is ready for the AI model.")