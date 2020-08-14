MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$', '$']],
    displayMath: [['$$', '$$']],
    processEscapes: true,
    processEnvironments: true,
    skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
    TeX: {
      TagSide: "right",
      TagIndent: ".8em",
      MultLineWidth: "85%",
      equationNumbers: {
        autoNumber: "AMS",
      },
      unicode: {
        fonts: "STIXGeneral,'Arial Unicode MS'"
      },
      extensions: ["AMSmath.js", "AMSsymbols.js"]
    },
  },
  "HTML-CSS": {
    scale: 80,
    styles: {
      ".MathJax": { color: "rgb(191 149 249)", }
    },
  },
  displayAlign: "center",
  showProcessingMessages: false,
  messageStyle: "none"
});

$(document).ready(function () {
  let productImageGroups = []
  $('.img-fluid').each(function () {
    let productImageSource = $(this).attr('src')
    let productImageTag = $(this).attr('tag')
    let productImageTitle = $(this).attr('title')
    if (productImageTitle) {
      productImageTitle = 'title="' + productImageTitle + '" '
    }
    else {
      productImageTitle = ''
    }
    $(this).
        wrap('<a class="boxedThumb ' + productImageTag + '" ' +
            productImageTitle + 'href="' + productImageSource + '"></a>')
    productImageGroups.push('.' + productImageTag)
  })
  jQuery.unique(productImageGroups)
  productImageGroups.forEach(productImageGroupsSet)

  function productImageGroupsSet (value) {
    $(value).simpleLightbox()
  }
});