
import re

import webbrowser

import pandas as pd
from jinja2 import Template

class View():
    
    def __init__(self, html_template = "template.txt"):
        
        with open(html_template, encoding = "utf8") as f:
            self.page = Template(f.read()) 

        self.div_tab = Template("""
                                <div id = "{{df_name}}" class = "tabcontent">
                                   {{html_table}}
                                </div>
                                """)
               
        
    def output(self, title, df_dict, output = None):
        
        divs = []
        
        for key, element in df_dict.items():

            if isinstance(element, pd.core.frame.DataFrame) == True:
                table = element.style.render().replace("\n", "")
            else:
                table = element.render().replace("\n", "")
                
            str_find = '<table id="\w*" >'
            str_replace = '<table id = "table_' + str(key) + '">'
            table = re.sub(str_find, str_replace, table)
            
            divs.append(self.div_tab.render(df_name = key, html_table = table))
                
        self.html_code = self.page.render(title = title,
                                          list_df = df_dict.keys(),
                                          list_divs = divs)
            
        if output is not None:
            with open(output, "w") as page:
                print(self.html_code, file = page)
                webbrowser.open(output)
        
        return None
            