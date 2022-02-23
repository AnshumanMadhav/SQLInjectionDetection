# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 10:29:52 2022

@author: AnshumanMadhav
"""

mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml