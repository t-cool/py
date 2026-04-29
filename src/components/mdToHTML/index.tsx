import MarkdownIt from "markdown-it";
import mk from "markdown-it-katex";

export default function mdToHTML(mdCode: string) {
  const md = new MarkdownIt({
    html: true,
    linkify: true,
    typographer: true,
    highlight: function (str, lang) {
      const language = lang || 'python';
      return `<pre class="language-${language}"><code class="language-${language}">${md.utils.escapeHtml(str)}</code></pre>`;
    }
  });
  md.use(mk);

  const htmlContent = md.render(mdCode);

  const template = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.5.1/katex.min.css"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-okaidia.min.css"/>
  <style>
    body {
      background-color: transparent !important;
      margin: 0;
      padding: 10px;
      color: #333;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    }

    /* コードブロックの背景を黒に固定 */
    pre[class*="language-"] {
      background: #000000 !important;
      padding: 1em;
      margin: 0.5em 0;
      overflow: auto;
      border-radius: 8px;
      border: 1px solid #333;
    }

    /* コード内の基本文字色を明るいグレーに固定 */
    code[class*="language-"], 
    pre[class*="language-"] {
      color: #f8f8f2 !important;
      text-shadow: none !important;
      font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
      font-size: 14px;
      line-height: 1.5;
    }

    /* ハイライトが効かない場合やコメントなどが黒くなるのを防ぐための強制カラー */
    .token.comment, .token.prolog, .token.doctype, .token.cdata { color: #8292a2 !important; }
    .token.punctuation { color: #f8f8f2 !important; }
    .token.namespace { opacity: .7; }
    .token.property, .token.tag, .token.constant, .token.symbol, .token.deleted { color: #f92672 !important; }
    .token.boolean, .token.number { color: #ae81ff !important; }
    .token.selector, .token.attr-name, .token.string, .token.char, .token.builtin, .token.inserted { color: #a6e22e !important; }
    .token.operator, .token.entity, .token.url, .language-css .token.string, .style .token.string { color: #f8f8f2 !important; }
    .token.atrule, .token.attr-value, .token.keyword { color: #66d9ef !important; }
    .token.function, .token.class-name { color: #e6db74 !important; }
    .token.regex, .token.important, .token.variable { color: #fd971f !important; }
    
    /* Mermaidなどの特殊なブロックもPython風に色付けするためのフォールバック */
    .language-mermaid .token { color: #f8f8f2; }
  </style>
</head>
<body>
  ${htmlContent}
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-mermaid.min.js"></script>
  <script>
    (function() {
      function highlight() {
        if (typeof Prism !== 'undefined') {
          Prism.highlightAll();
        }
      }
      if (document.readyState === 'complete') {
        highlight();
      } else {
        window.addEventListener('load', highlight);
      }
      // バックアップ：動的読み込みに対応
      setTimeout(highlight, 100);
      setTimeout(highlight, 500);
    })();
  </script>
</body>
</html>
`;
  return template;
}
