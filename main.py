import random

def build_markov_model(text_corpus):
    """
    Builds a simple Markov chain model from a text corpus.
    The model is a dictionary where keys are words and values are lists
    of words that follow the key word in the corpus.
    """
    model = {}
    # Clean and tokenize the corpus into words
    words = text_corpus.lower().replace('.', '').replace(',', '').split()
    
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i+1]
        if current_word not in model:
            model[current_word] = []
        model[current_word].append(next_word)
    
    return model

def generate_synthetic_text(model, start_word=None, length=20):
    """
    Generates synthetic text using the Markov model.
    """
    if not model:
        return "Model is empty. Cannot generate text."

    # Pick a random starting word if not provided or if the provided word is not in the model
    if start_word and start_word.lower() in model:
        current_word = start_word.lower()
    else:
        current_word = random.choice(list(model.keys()))
    
    generated_words = [current_word]

    for _ in range(length - 1):
        if current_word in model and model[current_word]:
            next_word = random.choice(model[current_word])
            generated_words.append(next_word)
            current_word = next_word
        else:
            # If no next word can be found for the current word, stop generation
            break
            
    # Capitalize the first word and add a period at the end for readability
    output = ' '.join(generated_words)
    return output.capitalize() + "."

# --- Main execution --- 
if __name__ == "__main__":
    # This corpus represents the "real" data from which we learn patterns.
    # The article discusses "synthetic representations" mimicking real-world phenomena.
    corpus = """
Yapay zeka günümüzde birçok alanda kullanılıyor. Sanal gerçeklik deneyimleri
gelişiyor. Sentetik veriler önemli bir rol oynuyor. Simülasyon teknolojileri
ilerliyor. Gerçek dünya verileriyle karşılaştırmak kritik. Etik kurallar
her zaman önemli. Yeni teknolojiler hayatımızı değiştiriyor.
    """

    print("--- Building Markov Model from Corpus ---")
    markov_model = build_markov_model(corpus)

    print("\n--- Generating Synthetic Text Examples ---")
    
    # Example 1: Generate a short synthetic sentence
    # This demonstrates creating a "synthetic representation" of language, 
    # mimicking natural text patterns without true understanding.
    synthetic_sentence_1 = generate_synthetic_text(markov_model, length=10)
    print(f"Synthetic Text 1: {synthetic_sentence_1}")

    # Example 2: Generate another synthetic sentence, perhaps starting with a specific word
    synthetic_sentence_2 = generate_synthetic_text(markov_model, start_word="sanal", length=12)
    print(f"Synthetic Text 2: {synthetic_sentence_2}")

    # Example 3: Generate a slightly longer one
    synthetic_sentence_3 = generate_synthetic_text(markov_model, length=15)
    print(f"Synthetic Text 3: {synthetic_sentence_3}")

    print("\n--- What this demonstrates ---")
    print("This script creates 'synthetic text' by learning simple word sequences from a given corpus.")
    print("It mimics the structure of natural language without understanding its meaning,")
    print("illustrating how artificial representations can be generated from real data patterns.")
