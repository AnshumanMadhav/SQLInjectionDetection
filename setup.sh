# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 10:29:52 2022

@author: anshu
"""

mkdir -p ~/.streamlit/

echo "\
[server]\n\
port= $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/comfig.toml