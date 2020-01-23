![Control gallery](logo/control-gallery.png)

# Control Systems Gallery

The Control Systems Gallery is a Python module that documents a standard collection of systems for use in
the analysis and design of feedback control with a focus on state-space models.


# Features

- Continuous-time and discrete-time systems
- Easy integration with the [Python Control package](https://github.com/python-control/python-control)


# Links

- TBD


# Conventions
- Individual system definitions are stored in dictionaries as a [pickle](https://docs.python.org/3/library/pickle.html) file keyed to a unique 10-digit integer system ID
  - IDs 0000000000 thru 4999999999 are reserved for continuous-time systems
  - IDs 5000000000 thru 9999999999 are reserved for discrete-time systems
- At a minimum each system must have:
  - Time type, continuous ('c') or discrete ('d')
  - Dynamics representation, state-space ('ss') or transfer function ('tf')
  - Either A, B, C, and D matrices (state-space representation) or a transfer function G (transfer function representation)
    - If C and D matrices were not specified in source materials then C and D are NoneType
- Additional parameters are stored as needed
  - Consult the source material (listed in metadata) for detailed description
- Metadata (system description, source paper, authors, notes) is stored in the dictionary if available
- Column and row vectors are treated as single-dimensional NumPy arrays

# Dependencies

The Control Systems Gallery package requires the NumPy package.

Developed and tested with Python 3.7


# Installation

## Conda and conda-forge

TBD

## Pip

TBD


# Development

## Code

You can check out the latest version of the source code with the command:

  git clone https://github.com/BenGravell/control-gallery.git

## Testing

TBD

## License

This is free software released under the terms of the MIT License. There is no warranty; not even for merchantability or fitness for a particular purpose. Consult LICENSE for copying conditions.

When code is modified or re-distributed, the LICENSE file should accompany the code or any subset of it, however small. As an alternative, the LICENSE text can be copied within files, if so desired.

## Contributing

Your contributions are welcome!  Simply fork the GitHub repository and send a
[pull request](https://github.com/BenGravell/control-gallery/pulls).


Icons made by
<a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a>, 
<a href="https://www.flaticon.com/authors/eucalyp" title="Eucalyp">Eucalyp</a>,
<a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a>, 
<a href="https://www.flaticon.com/authors/smalllikeart" title="smalllikeart">smalllikeart</a>, and
<a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a>
from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>.
