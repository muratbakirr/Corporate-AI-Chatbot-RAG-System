"""" Utility functions for document loading"""

import logging #tracking what your code is doing 
import pathlib
import tempfile
from typing import Any

from langchain_community.document_loaders.epub import UnstructuredEPubLoader
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders.word_document import UnstructuredWordDocumentLoader

from langchain_core.documents import Document
from streamlit.logger import get_logger

logging.basicConfig(encoding="utf-8", level=logging.INFO) # shows normal progress
LOGGER = get_logger(__name__)

class EpubReader(UnstructuredEPubLoader):
    def __init__(self, file_path: str | list[str], **unstructured_kwargs: Any):
        super().__init__(file_path,  mode = "elements", **unstructured_kwargs, strategy='fast')
        
class DocumentLoaderException(Exception):  # error type 
    pass

class DocumentLoader(object):
    """" Loads given document with supported extension"""
    
    sup_ext = {
        ".pdf": PyPDFLoader,
        ".txt": TextLoader,
        ".epub": EpubReader,
        ".docx": UnstructuredWordDocumentLoader,
        ".doc": UnstructuredWordDocumentLoader
        
    }
    
def load_document(file_path: str) -> list[Document]:
    """ Load a file and return Document objects. """
    
    
    doc_path_suffix = pathlib.Path(file_path).suffix
    doc_loader = DocumentLoader.sup_ext.get(doc_path_suffix)
    if not doc_loader:
        raise DocumentLoaderException(
            f"Invalid type of file, please upload appropriate types of files"
        )
    
    try:
        loader = doc_loader(file_path)
        loaded_doc = loader.load()
    except Exception as e:
        raise DocumentLoaderException(f"Failed to load {file_path}: {e}") from e
    
    return loaded_doc

        
    

        
        
  