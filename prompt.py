from langchain_core.prompts import PromptTemplate

RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an intelligent assistant answering questions from a PDF document.

Use ONLY the provided context to answer.
If the answer is not in the context, say:
"I could not find this information in the document."

Context:
{context}

Question:
{question}

Answer:
"""
)
