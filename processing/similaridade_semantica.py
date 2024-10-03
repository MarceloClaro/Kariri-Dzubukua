# processing/similaridade_semantica.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def calcular_similaridade_semantica(model, sentences_dzubukua, sentences_arcaico, sentences_moderno):
    """
    Função para calcular a similaridade semântica entre as frases de três idiomas diferentes.
    """
    all_sentences = sentences_dzubukua + sentences_arcaico + sentences_moderno
    embeddings = model.encode(all_sentences, batch_size=32, normalize_embeddings=True)

    # Separar os embeddings de cada idioma
    embeddings_dzubukua = embeddings[:len(sentences_dzubukua)]
    embeddings_arcaico = embeddings[len(sentences_dzubukua):len(sentences_dzubukua) + len(sentences_arcaico)]
    embeddings_moderno = embeddings[len(sentences_dzubukua) + len(sentences_arcaico):]

    # Calcular similaridade de cosseno
    similarity_arcaico_dzubukua = cosine_similarity(embeddings_dzubukua, embeddings_arcaico).diagonal()
    similarity_moderno_dzubukua = cosine_similarity(embeddings_dzubukua, embeddings_moderno).diagonal()
    similarity_arcaico_moderno = cosine_similarity(embeddings_arcaico, embeddings_moderno).diagonal()

    return similarity_arcaico_dzubukua, similarity_moderno_dzubukua, similarity_arcaico_moderno
