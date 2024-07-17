from pathlib import Path

import pandas as pd

# render it with jinja
from jinja2 import Environment, StrictUndefined

from rdagent.components.coder.factor_coder.config import FACTOR_IMPLEMENT_SETTINGS

TPL = """
{{file_name}}
```{{type_desc}}
{{content}}
````
"""
# Create a Jinja template from the string
JJ_TPL = Environment(undefined=StrictUndefined).from_string(TPL)


def get_data_folder_intro():
    """Directly get the info of the data folder.
    It is for preparing prompting message.
    """
    content_l = []
    for p in Path(FACTOR_IMPLEMENT_SETTINGS.data_folder_debug).iterdir():
        if p.name.endswith(".h5"):
            df = pd.read_hdf(p)
            # get  df.head() as string with full width
            pd.set_option("display.max_columns", None)  # or 1000
            pd.set_option("display.max_rows", None)  # or 1000
            pd.set_option("display.max_colwidth", None)  # or 199
            rendered = JJ_TPL.render(
                file_name=p.name,
                type_desc="generated by `pd.read_hdf(filename).head()`",
                content=df.head().to_string(),
            )
            content_l.append(rendered)
        elif p.name.endswith(".md"):
            with open(p) as f:
                content = f.read()
                rendered = JJ_TPL.render(
                    file_name=p.name,
                    type_desc="markdown",
                    content=content,
                )
                content_l.append(rendered)
        else:
            raise NotImplementedError(
                f"file type {p.name} is not supported. Please implement its description function.",
            )
    return "\n ----------------- file splitter -------------\n".join(content_l)
