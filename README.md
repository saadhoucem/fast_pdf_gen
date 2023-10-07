# Fast PDF Generator

Fast PDF Generator is a Python package that allows you to generate PDF files using Handlebars templates quickly. It provides a simple and efficient way to compile Handlebars templates and convert them into PDF documents.

## Features

- **Handlebars Template Compilation:** Compile Handlebars templates to HTML strings.
- **PDF Generation:** Generate PDF files from compiled HTML content.
- **Path Handling:** Support for both absolute and relative file paths on Linux, macOS, and Windows.

## Installation

You can install the `fast_pdf_gen` package using `pip`:

`pip install fast_pdf_gen`



## Usage

```python
from fast_pdf_gen import compile_handlebars_template, generate_pdf

# Handlebars Template Compilation
template_key = 'template1'
template_path_or_string = 'path/to/template.html'  # Or a template string
context = {'variable': 'value'}
compiled_template = compile_handlebars_template(template_key, template_path_or_string, context=context)

# PDF Generation
output_path = 'output.pdf'
generate_pdf(template_key, compiled_template, output_path, context=context)
```

### Options

* `template_key` (str): Unique identifier for the template.
* `template_path_or_string` (str): Path to the HTML template file or a template string.
* `compiled_template` (str): Compiled HTML content obtained from `compile_handlebars_template`.
* `output_path` (str): Path where the generated PDF will be saved.
* `context` (optional, dict): Dictionary containing variables to be substituted in the Handlebars template.

### Contributing

1. Fork the repository and clone it locally.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Create a pull request on GitHub.

### License

This project is licensed under the MIT License.
