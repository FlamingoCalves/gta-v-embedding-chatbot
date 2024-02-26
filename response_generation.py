# response_generation.py
def get_response(query_text, vectorIndex, vstore, llm):
    print("QUESTION: \"%s\"" % query_text)
    answer = vectorIndex.query(query_text, llm=llm).strip()
    print("ANSWER: \"%s\"\n" % answer)
    
    # Display documents by relevance
    docs_by_relevance = vstore.similarity_search_with_score(query_text, k=4)
    return answer, docs_by_relevance
