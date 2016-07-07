from CSS3.completions import types as t

# DESCRIPTOR NAMES
color_profile_descriptors = [
    ("name", "name: ${1:<identifier>};"),
    ("rendering-intent", "rendering-intent: ${1};"),
    ("src", "src: ${1};"),
]
counter_style_descriptors = [
    ("additive-symbols", "additive-symbols: ${1};"),
    ("fallback", "fallback: ${1:<counter-style-name>};"),
    ("negative", "negative: ${1};"),
    ("pad", "pad: ${1};"),
    ("prefix", "prefix: ${1:<symbol>};"),
    ("range", "range: ${1};"),
    ("speak-as", "speak-as: ${1};"),
    ("suffix", "suffix: ${1:<symbol>};"),
    ("symbols", "symbols: ${1};"),
    ("system", "system: ${1};"),
]
font_face_descriptors = [
    ("font-family", "font-family: ${1:<family-name>};"),
    ("font-feature-settings", "font-feature-settings: ${1};"),
    ("font-stretch", "font-stretch: ${1};"),
    ("font-style", "font-style: ${1};"),
    ("font-variant", "font-variant: ${1};"),
    ("font-weight", "font-weight: ${1};"),
    ("src", "src: ${1};"),
]
viewport_descriptors = [
    ("height", "height: ${1:<viewport-length>} ${2:<viewport-length>};"),
    ("max-height", "height: ${1:<viewport-length>};"),
    ("max-width", "width: ${1:<viewport-length>};"),
    ("max-zoom", "zoom: ${1};"),
    ("min-height", "height: ${1:<viewport-length>};"),
    ("min-width", "width: ${1:<viewport-length>};"),
    ("min-zoom", "zoom: ${1};"),
    ("orientation", "orientation: ${1};"),
    ("user-zoom", "user-zoom: ${1};"),
    ("width", "width: ${1:<viewport-length>} ${2:<viewport-length>};"),
    ("zoom", "zoom: ${1};"),
]

# DESCRIPTOR VALUES
color_profile_descriptor_to_completions = {
    "rendering-intent": [
        ("absolute-colorimetric",),
        ("auto",),
        ("perceptual",),
        ("relative-colorimetric",),
        ("saturation",),
    ],
    "src": [("sRGB",), t.local, t.url],
}
counter_style_descriptor_to_completions = {
    "additive-symbols": [t.integer] + t.symbol,
    "negative": t.symbol,
    "pad": [t.integer] + t.symbol,
    "prefix": t.symbol,
    "range": [("auto",), ("infinite",), t.integer],
    "speak-as": [
        ("<counter-style-name>", "$1"),
        ("auto",),
        ("bullets",),
        ("numbers",),
        ("spell-out",),
        ("words",),
    ],
    "suffix": t.symbol,
    "symbols": t.symbol,
    "system": [
        ("additive",),
        ("alphabetic",),
        ("cyclic",),
        ("extends",),
        ("fixed",),
        ("numeric",),
        ("symbolic",),
        t.counter_style_name,
        t.integer,
    ],
}
font_face_descriptor_to_completions = {
    "font-family": [
        ("cursive",),
        ("fantasy",),
        ("monospace",),
        ("sans-serif",),
        ("serif",),
        t.family_name,
    ],
    "font-feature-settings": [("normal",)] + t.feature_tag_value,
    "font-stretch": [
        ("condensed",),
        ("expanded",),
        ("extra-condensed",),
        ("extra-expanded",),
        ("normal",),
        ("semi-condensed",),
        ("semi-expanded",),
        ("ultra-condensed",),
        ("ultra-expanded",),
    ],
    "font-style": [("italic",), ("normal",), ("oblique",)],
    "font-variant": [
        ("all-petite-caps",),
        ("all-small-caps",),
        ("historical-forms",),
        ("none",),
        ("normal",),
        ("ordinal",),
        ("petite-caps",),
        ("ruby",),
        ("slashed-zero",),
        ("small-caps",),
        ("sub",),
        ("super",),
        ("titling-caps",),
        ("unicase",),
        t.annotation,
        t.character_variant,
        t.ornaments,
        t.styleset,
        t.stylistic,
        t.swash,
    ] + (
        t.common_lig_values + t.discretionary_lig_values + t.historical_lig_values +
        t.contextual_alt_values +
        t.numeric_figure_values + t.numeric_spacing_values + t.numeric_fraction_values +
        t.east_asian_variant_values + t.east_asian_width_values
    ),
    "font-weight": [
        ("100",),
        ("200",),
        ("300",),
        ("400",),
        ("500",),
        ("600",),
        ("700",),
        ("800",),
        ("900",),
        ("bold",),
        ("normal",),
    ],
    "src": [
        t.format_func,
        t.font_face_name,
        t.local,
        t.url,
    ],
    "unicode-range": [t.urange],
}
viewport_descriptor_to_completions = {
    "height": [("auto",), ("extend-to-zoom",), t.length, t.percentage],
    "max-height": [("auto",), ("extend-to-zoom",), t.length, t.percentage],
    "max-width": [("auto",), ("extend-to-zoom",), t.length, t.percentage],
    "max-zoom": [("auto",), t.number, t.percentage],
    "min-height": [("auto",), ("extend-to-zoom",), t.length, t.percentage],
    "min-width": [("auto",), ("extend-to-zoom",), t.length, t.percentage],
    "min-zoom": [("auto",), t.number, t.percentage],
    "orientation": [("auto",), ("landscape",), ("portrait",)],
    "user-zoom": [("fixed",), ("zoom",)],
    "width": [("auto",), ("extend-to-zoom",), t.length, t.percentage],
    "zoom": [("auto",), t.number, t.percentage],
}

at_rule_to_completions_dict = {
    "color-profile": color_profile_descriptor_to_completions,
    "counter-style": counter_style_descriptor_to_completions,
    "font-face": font_face_descriptor_to_completions,
    "viewport": viewport_descriptor_to_completions,
}


def sort_and_uniq_completions():
    completions_dicts = (
        color_profile_descriptor_to_completions,
        counter_style_descriptor_to_completions,
        font_face_descriptor_to_completions,
        viewport_descriptor_to_completions,
    )

    for completions_dict in completions_dicts:
        for name in completions_dict:
            completions_dict[name] = list(set(completions_dict[name]))
            completions_dict[name].sort()


sort_and_uniq_completions()
