"""
This script fixes indentation issues in the stage_4_evidence.py file.
It reads the original file, corrects indentation issues, and writes to a clean file.
"""

import os
import re

def fix_indentation(input_file, output_file=None):
    """Fix indentation issues in a Python file."""
    if output_file is None:
        output_file = input_file
    
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Fix common indentation issues
    fixed_lines = []
    for i, line in enumerate(lines):
        # Add space after statements if there's another statement right after
        cleaned_line = re.sub(r'([^\s])(\S+.*?)([^\s;])\s+([a-zA-Z_][a-zA-Z0-9_]*\s*=|def\s+|class\s+|if\s+|for\s+|while\s+|try\s*:|except\s+|finally\s*:|else\s*:|elif\s+|with\s+|@|return\s+)', r'\1\2\3\n\4', line)
        
        # Fix issues with indentation after parentheses
        if ')' in cleaned_line and ('):' in cleaned_line or ') :' in cleaned_line):
            next_line_indent = ' ' * (len(cleaned_line) - len(cleaned_line.lstrip()))
            if i+1 < len(lines) and lines[i+1].strip() and not lines[i+1].startswith(next_line_indent + '    '):
                cleaned_line = cleaned_line.rstrip() + '\n' + next_line_indent + '    '
        
        fixed_lines.append(cleaned_line)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(fixed_lines)
    
    print(f"Fixed indentation in {input_file} and saved to {output_file}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_dir = os.path.join(base_dir, 'src', 'asr_got_reimagined', 'domain', 'stages')
    
    # Fix stage_4_evidence.py
    evidence_file = os.path.join(src_dir, 'stage_4_evidence.py')
    fix_indentation(evidence_file)
