# Portfolio
Data Science Dojo portfolio available through Streamlit application

# Installation
python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

# Run
streamlit run Portfolio.py

# Add new subpage
create new .py file in *pages* catalog. New web page will appear automatically. \
every page must contain the following as the first lines: 
``` python
from render_project import render_project
from find_project import find_project
from initialize_page import initialize_page

initialize_page()
streamlit_project = find_project("ProjectName")
render_project(streamlit_project)
```


# Styling
### Streamlit
Streamlit allows for some basic styling. \
The config for it is `.streamlit/config.toml`. \
To apply that theme, select it in the top-right menu of the app.

### CSS
Additional styling can be done for example in `style/style.css` \

### Images
`/images` -> main images catalog \
