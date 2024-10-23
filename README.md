# skia-gradient-array

Simple wrapper around Skia to generate a gradient image in numpy.
It uses a skia.Surface with alphaType of skia.kUnpremul_AlphaType, so that it plays
nicely with matplotib. Packages like cairo only supports alpha-premultiplied canvas,
and things are not idea as Matplotlib does not support alpha-multiplied images.
                                    )

## Installation

You can install using `pip`:

```bash
pip install skia_gradient_array
```

## Development Installation


```bash
pip install -e ".[dev]"
```

