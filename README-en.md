# PySchool - Python-based Escape Room

PySchool is an interactive web-based escape room game built with Python and Quarto. Players solve puzzles and challenges by writing and executing Python code directly in their browser.

[Live Demo](https://sebastiandres.github.io/pyschool_2025/)


## Features

- 🎮 Interactive Python coding challenges
- 🌐 Runs entirely in the browser using Pyodide
- 🎨 Beautiful sketch-style interface
- 🔍 Real-time code verification
- 📱 Responsive design for all devices

## Getting Started

### Design 

The design is based on the [sketchy theme](https://bootswatch.com/sketchy/), which relies on the google fonts Neucha and Cabin+Sketch.
Some of the color definitions are:


### Prerequisites

- Python 3.x
- Quarto
- Make (optional, for using Makefile commands)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sebastiandres/pyscape.git
   cd pyscape
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

1. Render the Quarto site:
   ```bash
   make render
   ```
   Or manually:
   ```bash
   cd quarto && quarto render .
   ```

> [!NOTE]
>
> Quarto runs using random port, to set a specific port use: `quarto preview --port [port]`.
> 
> More details `quarto preview --help`.

2. View the site:
   ```bash
   make view
   ```
   Or open `docs/index.html` in your browser.

## Project Structure

- `quarto/` - Contains the main Quarto site files
- `docs/` - Generated static site files
- `verification.py` - Python code for verifying solutions
- `Makefile` - Build automation commands

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Adding New Puzzles

To add a new puzzle:

1. Create a new Quarto document in the `quarto/` directory
2. Add your puzzle description and Python verification code
3. Update the navigation in `quarto/_quarto.yml`
4. Test your puzzle locally
5. Submit a pull request

## Technical Details

- Built with [Quarto](https://quarto.org/)
- Uses [Pyodide](https://pyodide.org/) for in-browser Python execution
- Custom theme based on the sketchy theme
- Fonts: Neucha and Cabin+Sketch

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Quarto and Pyodide teams for their amazing tools
- Inspired by the joy of escape rooms and Python programming