"""
CSS 1 definitions.
"""

from __future__ import absolute_import
import textwrap

CSS_PSEUDO_CLASS_NAMES = """first-letter first-line link active visited
        first-child focus hover lang before after left right first""".split()

CSS_ATTR_DICT = {
    'background': [
            'bottom',
            'center',
            'fixed',
            'inherit',
            'left',
            'none',
            'no-repeat',
            'repeat',
            'repeat-x',
            'repeat-y',
            'hsl(',
            'hsla(',
            'rgb(',
            'rgba(',
            'right',
            'scroll',
            'top',
            'transparent',
            'url(',
            'linear-gradient(',
            'repeating-linear-gradient(',
            'radial-gradient(',
            'repeating-radial-gradient(',
            '!important',
            '#',
        ],
    'background-attachment': [
            'fixed',
            'inherit',
            'scroll',
            '!important',
        ],
    'background-color': [
            'inherit',
            'hsl(',
            'hsla(',
            'rgb(',
            'rgba(',
            'transparent',
            '!important',
            '#',
        ],
    'background-image': [
            'inherit',
            'none',
            'url(',
            '!important',
        ],
    'background-position': [
            'bottom',
            'center',
            'inherit',
            'left',
            'right',
            'top',
            '!important',
        ],
    'background-repeat': [
            'inherit',
            'no-repeat',
            'repeat',
            'repeat-x',
            'repeat-y',
            '!important',
        ],
    'border'    : [
            'dashed',
            'dotted',
            'double',
            'groove',
            'hidden',
            'inherit',
            'inset',
            'medium',
            'none',
            'outset',
            'hsl(',
            'hsla(',
            'rgb(',
            'rgba(',
            'ridge',
            'solid',
            'thick',
            'thin',
            '!important',
            '#',
        ],
    'border-bottom': [
            'dashed',
            'dotted',
            'double',
            'groove',
            'hidden',
            'inherit',
            'inset',
            'medium',
            'none',
            'outset',
            'hsl(',
            'hsla(',
            'rgb(',
            'rgba(',
            'ridge',
            'solid',
            'thick',
            'thin',
            '!important',
            '#',
        ],
    'border-bottom-width': [
            'inherit',
            'medium',
            'thick',
            'thin',
            '!important',
        ],
    'border-color': [
            'inherit',
            'hsl(',
            'hsla(',
            'rgb(',
            'rgba(',
            'transparent',
            '!important',
            '#',
        ],
    'border-left': [
            'dashed',
            'dotted',
            'double',
            'groove',
            'hidden',
            'inherit',
            'inset',
            'medium',
            'none',
            'outset',
            'hsl(',
            'hsla(',
            'rgb(',
            'rgba(',
            'ridge',
            'solid',
            'thick',
            'thin',
            '!important',
            '#',
        ],
    'border-left-color': [
            'inherit',
            'hsl(',
            'hsla(',
            'rgb(',
            'rgba(',
            '!important',
            '#',
        ],
    'border-left-style': [
            'dashed',
            'dotted',
            'double',
            'groove',
            'hidden',
            'inherit',
            'inset',
            'none',
            'outset',
            'ridge',
            'solid',
            '!important',
        ],
    'border-left-width': [
            'inherit',
            'medium',
            'thick',
            'thin',
            '!important',
        ],
    'border-right': [
            'dashed',
            'dotted',
            'double',
            'groove',
            'hidden',
            'inherit',
            'inset',
            'medium',
            'none',
            'outset',
            'hsl(',
            'hsla(',
            'rgb(',
            'rgba(',
            'ridge',
            'solid',
            'thick',
            'thin',
            '!important',
            '#',
        ],
    'border-right-color': [
            'inherit',
            'hsl(',
            'hsla(',
            'rgb(',
            'rgba(',
            '!important',
            '#',
        ],
    'border-right-style': [
            'dashed',
            'dotted',
            'double',
            'groove',
            'hidden',
            'inherit',
            'inset',
            'none',
            'outset',
            'ridge',
            'solid',
            '!important',
        ],
    'border-right-width': [
            'inherit',
            'medium',
            'thick',
            'thin',
            '!important',
        ],
    'border-spacing': [
            'inherit',
            '!important',
        ],
    'border-style': [
            'dashed',
            'dotted',
            'double',
            'groove',
            'hidden',
            'inherit',
            'inset',
            'none',
            'outset',
            'ridge',
            'solid',
            '!important',
        ],
    'border-top': [
            'dashed',
            'dotted',
            'double',
            'groove',
            'hidden',
            'inherit',
            'inset',
            'medium',
            'none',
            'outset',
            'hsl(',
            'hsla(',
            'rgb(',
            'rgba(',
            'ridge',
            'solid',
            'thick',
            'thin',
            '!important',
            '#',
        ],
    'border-top-width': [
            'inherit',
            'medium',
            'thick',
            'thin',
            '!important',
        ],
    'border-width': [
            'inherit',
            'medium',
            'thick',
            'thin',
            '!important',
        ],
    'clear'     : [
            'both',
            'inherit',
            'left',
            'none',
            'right',
            '!important',
        ],
    'color'     : [
            'inherit',
            'hsl(',
            'hsla(',
            'rgb(',
            'rgba(',
            '!important',
            '#',
        ],
    'display'   : [
        'none',
        'inline',
        'block',
        'inline-block',
        'contents',
        'list-item',
        'inline-list-item',
        'table',
        'inline-table',
        'table-cell',
        'table-column',
        'table-column-group',
        'table-footer-group',
        'table-header-group',
        'table-row',
        'table-row-group',
        'table-caption',
        'flex',
        'inline-flex',
        'grid',
        'inline-grid',
        'ruby',
        'ruby-base',
        'ruby-text',
        'ruby-base-container',
        'ruby-text-container',
        'run-in',
        'inherit',
        'initial',
        'unset',
        '!important'
        ],
    'float'     : [
            'inherit',
            'left',
            'none',
            'right',
            '!important',
        ],
    'font'      : [
            '100',
            '200',
            '300',
            '400',
            '500',
            '600',
            '700',
            '800',
            '900',
            'bold',
            'bolder',
            'caption',
            'cursive',
            'fantasy',
            'icon',
            'inherit',
            'italic',
            'large',
            'larger',
            'lighter',
            'medium',
            'menu',
            'message-box',
            'monospace',
            'normal',
            'oblique',
            'sans-serif',
            'serif',
            'small',
            'smaller',
            'small-caps',
            'small-caption',
            'status-bar',
            'xx-large',
            'xx-small',
            'x-large',
            'x-small',
            '!important',
        ],
    'font-family': [
            'cursive',
            'fantasy',
            'inherit',
            'monospace',
            'sans-serif',
            'serif',
            '!important',
        ],
    'font-size' : [
            'inherit',
            'large',
            'larger',
            'medium',
            'small',
            'smaller',
            'xx-large',
            'xx-small',
            'x-large',
            'x-small',
            '!important',
        ],
    'font-size-adjust': [
            'inherit',
            'none',
            '!important',
        ],
    'font-stretch': [
            'condensed',
            'expanded',
            'extra-condensed',
            'extra-expanded',
            'inherit',
            'narrower',
            'normal',
            'semi-condensed',
            'semi-expanded',
            'ultra-condensed',
            'ultra-expanded',
            'wider',
            '!important',
        ],
    'font-style': [
            'inherit',
            'italic',
            'normal',
            'oblique',
            '!important',
        ],
    'font-variant': [
            'inherit',
            'normal',
            'small-caps',
            '!important',
        ],
    'font-weight': [
            '100',
            '200',
            '300',
            '400',
            '500',
            '600',
            '700',
            '800',
            '900',
            'bold',
            'bolder',
            'inherit',
            'lighter',
            'normal',
            '!important',
        ],
    'height'    : [
            'auto',
            'inherit',
            '!important',
        ],
    'letter-spacing': [
            'inherit',
            'normal',
            '!important',
        ],
    'line-height': [
            'inherit',
            'normal',
            '!important',
        ],
    'list-style': [
            'armenian',
            'circle',
            'cjk-ideographic',
            'decimal',
            'decimal-leading-zero',
            'disc',
            'georgian',
            'hebrew',
            'hiragana',
            'hiragana-iroha',
            'inherit',
            'inside',
            'katakana',
            'katakana-iroha',
            'lower-alpha',
            'lower-greek',
            'lower-latin',
            'lower-roman',
            'none',
            'outside',
            'square',
            'upper-alpha',
            'upper-latin',
            'upper-roman',
            'url(',
            '!important',
        ],
    'list-style-image': [
            'inherit',
            'none',
            'url(',
            '!important',
        ],
    'list-style-position': [
            'inherit',
            'inside',
            'outside',
            '!important',
        ],
    'list-style-type': [
            'armenian',
            'circle',
            'cjk-ideographic',
            'decimal',
            'decimal-leading-zero',
            'disc',
            'georgian',
            'hebrew',
            'hiragana',
            'hiragana-iroha',
            'inherit',
            'katakana',
            'katakana-iroha',
            'lower-alpha',
            'lower-greek',
            'lower-latin',
            'lower-roman',
            'none',
            'square',
            'upper-alpha',
            'upper-latin',
            'upper-roman',
            '!important',
        ],
    'margin'    : [
            'auto',
            'inherit',
            '!important',
        ],
    'margin-bottom': [
            'auto',
            'inherit',
            '!important',
        ],
    'margin-left': [
            'auto',
            'inherit',
            '!important',
        ],
    'margin-right': [
            'auto',
            'inherit',
            '!important',
        ],
    'margin-top': [
            'auto',
            'inherit',
            '!important',
        ],
    'padding'   : [
            'inherit',
            '!important',
        ],
    'padding-bottom': [
            'inherit',
            '!important',
        ],
    'padding-left': [
            'inherit',
            '!important',
        ],
    'padding-right': [
            'inherit',
            '!important',
        ],
    'padding-top': [
            'inherit',
            '!important',
        ],
    'text-align': [
            'center',
            'inherit',
            'justify',
            'left',
            'right',
            '!important',
        ],
    'text-decoration': [
            'blink',
            'inherit',
            'line-through',
            'none',
            'overline',
            'underline',
            '!important',
        ],
    'text-indent': [
            'inherit',
            '!important',
        ],
    'text-transform': [
            'capitalize',
            'inherit',
            'lowercase',
            'none',
            'uppercase',
            '!important',
        ],
    'vertical-align': [
            'baseline',
            'bottom',
            'inherit',
            'middle',
            'sub',
            'super',
            'text-bottom',
            'text-top',
            'top',
            '!important',
        ],
    'white-space': [
            'inherit',
            'normal',
            'nowrap',
            'pre',
            'pre-wrap',
            'pre-line',
            '!important',
        ],
    'width'     : [
            'auto',
            'inherit',
            '!important',
        ],
    'word-spacing': [
            'inherit',
            'normal',
            '!important',
        ],
}

CSS_PROPERTY_ATTRIBUTE_CALLTIPS_DICT = {
    'background'            : """Shorthand for setting the individual background properties""",
    'background-attachment' : """If background image is specified, this specifies whether it is fixed with regard to the viewport ('fixed') or scrolls along with the document ('scroll').""",
    'background-color'      : """Sets the background color of an element, either a <color> value or the keyword 'transparent', to make the underlying colors shine through""",
    'background-image'      : """Sets the background image of an element. When setting a background image, authors should also specify a background color that will be used when the image is unavailable. When the image is available, it is rendered on top of the background color""",
    'background-position'   : """If a background image has been specified, this property specifies its initial position""",
    'background-repeat'     : """If a background image is specified, this property specifies whether the image is repeated (tiled), and how""",
    'border'                : """Shorthand for border-width, border-style and border-color affecting all 4 borders""",
    'border-bottom'         : """Shorthand for border-width, border-style and border-color affecting the bottom border""",
    'border-bottom-width'   : """Sets the width of the bottom border of a box""",
    'border-color'          : """Sets the color of the four borders""",
    'border-left'           : """Shorthand for border-width, border-style and border-color affecting the left border""",
    'border-left-width'     : """Sets the width of the left border of a box""",
    'border-right'          : """Shorthand for border-width, border-style and border-color affecting the right border""",
    'border-right-width'    : """Sets the width of the right border of a box""",
    'border-style'          : """Specifies the line style of a box's four borders (solid, double, dashed, hidden, etc.)""",
    'border-top'            : """Shorthand for border-width, border-style and border-color affecting the top border""",
    'border-top-width'      : """Sets the width of the top border of a box""",
    'border-width'          : """Shorthand for setting 'border-top-width', 'border-right-width', 'border-bottom-width', and 'border-left-width' at the same place in the style sheet. If there is only one value, it applies to all sides. If there are two values, the top and bottom borders are set to the first value and the right and left are set to the second. If there are three values, the top is set to the first value, the left and right are set to the second, and the bottom is set to the third. If there are four values, they apply to the top, right, bottom, and left, respectively.""",
    'clear'                 : """Indicates which sides of an element's box(es) may not be adjacent to an earlier floating box""",
    'color'                 : """This property describes the foreground color of an element's text content""",
    'display'               : """How the element is to be displayed, denotes the box type format""",
    'float'                 : """Specifies whether a box should float to the left, right, or not at all""",
    'font'                  : """Shorthand for setting 'font-style', 'font-variant', 'font-weight', 'font-size', 'line-height', and 'font-family', at the same place in the style sheet""",
    'font-family'           : """Specifies a prioritized list of font family names and/or generic family names""",
    'font-size'             : """Describes the size of the font when set solid""",
    'font-size-adjust'      : """Specifies an aspect value for an element that will preserve the x-height of the first choice font in the substitute font""",
    'font-stretch'          : """Selects a normal, condensed, or extended face from a font family""",
    'font-style'            : """Sets normal (sometimes referred to as "roman" or "upright"), italic, and oblique faces within a font family""",
    'font-variant'          : """Can be used to select font casing 'normal' or 'small-caps'""",
    'font-weight'           : """Specifies the weight of the font""",
    'height'                : """Specifies the content height of boxes generated by block-level and replaced elements""",
    'letter-spacing'        : """Specifies spacing behavior between text characters""",
    'line-height'           : """Specifies the minimal height of each generated inline box""",
    'list-style'            : """Shorthand notation for setting the three properties 'list-style-type', 'list-style-image', and 'list-style-position' at the same place in the style sheet""",
    'list-style-image'      : """Sets the image that will be used as the list item marker""",
    'list-style-position'   : """Specifies the position of the marker box in the principal block box""",
    'list-style-type'       : """Specifies appearance of the list item marker if 'list-style-image' has the value 'none' or if the image pointed to by the URI cannot be displayed""",
    'margin'                : """Shorthand for setting 'margin-top', 'margin-right', 'margin-bottom', and 'margin-left' at the same place in the style sheet""",
    'margin-bottom'         : """Specifies the width of the bottom margin area of a box""",
    'margin-left'           : """Specifies the width of the left margin area of a box""",
    'margin-right'          : """Specifies the width of the right margin area of a box""",
    'margin-top'            : """Specifies the width of the top margin area of a box""",
    'padding'               : """Shorthand for setting 'padding-top', 'padding-right', 'padding-bottom', and 'padding-left' at the same place in the style sheet""",
    'padding-bottom'        : """Sets the bottom width of the containing box""",
    'padding-left'          : """Sets the left width of the containing box""",
    'padding-right'         : """Sets the right width of the containing box""",
    'padding-top'           : """Sets the top width of the containing box""",
    'table-layout'          : """Specifies the algorithm used to lay out the table cells, rows, and columns""",
    'text-align'            : """Specifies how inline content of a block is aligned""",
    'text-decoration'       : """Specifies decorations that are added to the text of an element""",
    'text-indent'           : """Specifies the indentation of the first line of text in a block""",
    'text-transform'        : """Specifies capitalization effects of an element's text""",
    'uri'                   : """An internet reference string.""",
    'vertical-align'        : """Affects the vertical positioning inside a line box of the boxes generated by an inline-level element""",
    'white-space'           : """Specifies how whitespace inside the element is handled""",
    'width'                 : """Specifies the content width of boxes generated by block-level and replaced elements""",
    'word-spacing'          : """Specifies spacing behavior between words""",
}
for property, calltip in CSS_PROPERTY_ATTRIBUTE_CALLTIPS_DICT.items():
    CSS_PROPERTY_ATTRIBUTE_CALLTIPS_DICT[property] = "\n".join(textwrap.wrap(calltip, 40))
