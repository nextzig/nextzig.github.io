
project = 'nextzig docs'
copyright = '2026, nextzig'
author = 'nextzig'
release = '0.0.1'
html_meta = {
    'description': 'Dokumentasi resmi proyek nextzig',
    'keywords': 'nextzig, docs, sphinx, python',
    'author': 'nextzig',
}
extensions = [
    'sphinx.ext.autodoc',          
    'sphinx.ext.napoleon',         
    'sphinx.ext.viewcode',         
    'sphinx.ext.intersphinx',      
    'sphinx.ext.todo',             
    'sphinx.ext.coverage',         
    'sphinx.ext.mathjax',          
    'sphinx.ext.graphviz',         
    'sphinx.ext.inheritance_diagram', 
    'sphinx_copybutton',           
    'sphinx_design',               
    'myst_parser',                 
    'sphinx_autodoc_typehints',
]
autodoc_default_options = {
    'members': True,
    'undoc-members': True,       
    'private-members': False,    
    'special-members': '__init__',
    'inherited-members': True,
    'show-inheritance': True,
}
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'bizstyle'               
html_static_path = ['_static']
html_title = f"{project} {release}"
html_short_title = project
html_logo = ''                        
html_favicon = ''                     
html_sidebars = {
    '**': [
        'localtoc.html',    
        'relations.html',   
        'searchbox.html',
    ]
}
html_show_sphinx = True
html_show_copyright = True
html_show_sourcelink = True
todo_include_todos = True
typehints_fully_qualified = False    
always_document_param_types = True