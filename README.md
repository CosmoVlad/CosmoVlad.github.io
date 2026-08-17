# cosmovlad.github.io

Personal academic website of Vladimir Strokov, served by GitHub Pages.

## Editing the text content

The About paragraphs and the paper summaries on "My latest papers" live as Markdown in `content/`:

- `content/about.md`
- `content/paper-glow.md`
- `content/paper-hankel.md`

After editing them, splice the text back into the pages with

```
python build.py
```

(run in a Python environment with the `markdown` package)

(the script replaces the regions between `<!-- content:... -->` markers in `index.html` and `latest-papers.html`). TeX is supported in these files: `$...$` inline and `$$...$$` display, rendered by MathJax on the papers page. Escape literal asterisks in plain prose (`M87\*`) so Markdown does not read them as emphasis.

## Blogs

`blog/` and `reproduce-a-paper/` are Pelican sites (posts in `content/`, themes in `theme/`). After any change, regenerate:

```
cd blog && pelican content -s pelicanconf.py
cd reproduce-a-paper && pelican content -s pelicanconf.py
```

(run in a Python environment with `pelican` installed)

The generated pages in each `output/` are committed and served as-is. The two themes are identical except for the accent-color block at the top of `theme/static/css/main.css` (coral for Blog, azure for Reproduce-a-Paper).

## CV and publications

LaTeX sources in `materials/` (`CV.tex`, `publications.tex`, shared `refs.bib`). Build with `pdflatex` (publications also needs `biber`). The site links `materials/CV.pdf` and `materials/publications.pdf`.

## Template

Based on [Editorial](https://html5up.net) by HTML5 UP (@ajlkn), free for personal and commercial use under the [CCA 3.0 license](https://html5up.net/license) (see `LICENSE.txt`). Icons by Font Awesome; jQuery and Responsive Tools under the hood.
