#!/bin/bash

sleep 10
python ml_ops_labs/main.py &
streamlit run ml_ops_labs/web_view/index.py