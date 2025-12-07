from retriever import DocumentRetriever

# Initialize retriever
retriever = DocumentRetriever()
retriever.k = 3  # get top 3 relevant documents

# Add documents from file
retriever.add_uploaded_docs([
    open("papers_file/hadoop.pdf", "rb"),
    open("papers_file/kafka.pdf", "rb")
])

# Check memory
print(f"Documents in memory: {len(retriever.documents)}")