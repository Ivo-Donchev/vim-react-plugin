IMPORT_REGEX = r"import(?:[\"'\s]*([\w*{}\n, ]+)from\s*)?[\"'\s]*([\.]?[@\w/_-]+)[\"'\s]*;?"
EXPORT_REGEX = r"export(?:[\"'\s]*([\w*{}\n, ]+)from\s*)[\"'\s]*([\.]?[@\w/_-]+)[\"'\s]*;?"

ROOT = 'src/'
MAX_LEVEL_OF_DEPTH = 20
