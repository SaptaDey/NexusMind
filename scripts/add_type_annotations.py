"""
This script adds Python type annotations to help with static type checking in the codebase.
"""
import re
from typing import Dict, List, Any

def add_type_annotations(file_path: str) -> None:
    """Add type annotations to a Python file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix list annotations
    content = re.sub(
        r'(dimension_labels|dimension_node_ids)\s*=\s*\[\]', 
        r'\1: List[str] = []', 
        content
    )
    
    # Fix dimensions_to_create
    content = re.sub(
        r'dimensions_to_create\s*=\s*(.*?)\n',
        r'dimensions_to_create: List[Dict[str, Any]] = \1\n',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Added type annotations to {file_path}")

if __name__ == "__main__":
    import os
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stage2_path = os.path.join(base_dir, "src", "asr_got_reimagined", "domain", "stages", "stage_2_decomposition.py")
    
    add_type_annotations(stage2_path)
