# Contributing to MiniMe-LLM 🤝

Thank you for your interest in contributing to MiniMe-LLM! We welcome contributions from developers of all skill levels who are interested in machine learning, LLMs, and educational projects.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Documentation](#documentation)
- [Community](#community)

## 🤝 Code of Conduct

This project follows a standard code of conduct. We expect all contributors to:

- Be respectful and inclusive
- Focus on constructive feedback
- Help create a welcoming environment for learners
- Maintain professionalism in all interactions

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- Basic understanding of Python and machine learning concepts
- Familiarity with transformers and LLM architecture (helpful but not required)

### Development Setup

1. **Fork the repository**
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/MiniMe-LLM.git
   cd MiniMe-LLM
   ```

2. **Set up the development environment**
   ```bash
   # Using uv (recommended)
   uv sync --dev
   
   # Or using pip
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

3. **Set up pre-commit hooks** (once implemented)
   ```bash
   pre-commit install
   ```

4. **Verify your setup**
   ```bash
   python main.py
   # Should run without errors (may show network error, that's expected)
   ```

## 🛠️ How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Code contributions**: Core LLM implementation, training pipeline, utilities
- **Documentation**: README improvements, tutorials, examples
- **Testing**: Unit tests, integration tests, performance benchmarks
- **Bug reports**: Issue identification and reproduction
- **Feature requests**: New functionality suggestions
- **Educational content**: Explanations, tutorials, learning materials

### Finding Something to Work On

1. Check the [Issues](https://github.com/thisguymartin/MiniMe-LLM/issues) page
2. Look for issues labeled `good-first-issue` or `help-wanted`
3. Check the development roadmap in the README
4. Propose new features or improvements

### Before You Start

1. **Create an issue** to discuss your planned contribution
2. **Get approval** from maintainers for significant changes
3. **Check existing work** to avoid duplication
4. **Start small** if you're new to the project

## 📝 Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

2. **Make your changes**
   - Write clean, readable code
   - Follow the coding standards
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**
   ```bash
   # Run tests (once implemented)
   python -m pytest
   
   # Verify basic functionality
   python main.py
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

5. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a Pull Request on GitHub.

### PR Requirements

- **Clear title** and description
- **Link to related issues**
- **Test coverage** for new code
- **Documentation updates** if applicable
- **Passing CI checks** (once implemented)

## 💻 Coding Standards

### Python Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use type hints for function signatures
- Write docstrings for classes and functions
- Maximum line length: 88 characters (Black formatter standard)

### Code Quality

- **Functions**: Keep functions small and focused
- **Classes**: Follow single responsibility principle
- **Variables**: Use descriptive names
- **Comments**: Explain complex logic, not obvious code

### Example Code Structure

```python
from typing import List, Optional

import numpy as np
import torch


class MiniMeLLM:
    """A minimal Large Language Model implementation.
    
    This class provides a simple interface for training and inference
    with a transformer-based language model.
    
    Args:
        vocab_size: Size of the vocabulary
        hidden_dim: Hidden dimension size
        num_layers: Number of transformer layers
    """
    
    def __init__(
        self, 
        vocab_size: int, 
        hidden_dim: int = 512, 
        num_layers: int = 6
    ) -> None:
        self.vocab_size = vocab_size
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
    
    def generate(self, prompt: str, max_length: int = 100) -> str:
        """Generate text from a given prompt.
        
        Args:
            prompt: Input text to continue
            max_length: Maximum length of generated text
            
        Returns:
            Generated text as string
        """
        # Implementation here
        pass
```

## 🧪 Testing

### Testing Philosophy

- Write tests for all new functionality
- Aim for high test coverage
- Include edge cases and error conditions
- Use descriptive test names

### Running Tests

```bash
# Run all tests (once implemented)
python -m pytest

# Run specific test file
python -m pytest tests/test_model.py

# Run with coverage
python -m pytest --cov=minime_llm
```

## 📚 Documentation

### Documentation Standards

- **README**: Keep the main README up to date
- **Docstrings**: Document all public functions and classes
- **Type hints**: Use for all function parameters and returns
- **Examples**: Include usage examples in docstrings
- **Comments**: Explain complex algorithms and design decisions

### Building Documentation (Future)

```bash
# Build documentation (once implemented)
mkdocs serve
```

## 🏗️ Project Structure

Understanding the codebase structure:

```
MiniMe-LLM/
├── minime_llm/          # Main package (to be created)
│   ├── __init__.py
│   ├── model.py         # Core LLM implementation
│   ├── training.py      # Training pipeline
│   ├── inference.py     # Inference engine
│   └── utils.py         # Utility functions
├── tests/               # Test suite (to be created)
│   ├── __init__.py
│   ├── test_model.py
│   └── test_training.py
├── examples/            # Usage examples (to be created)
├── docs/                # Documentation (to be created)
├── main.py              # Entry point
├── pyproject.toml       # Project configuration
└── README.md            # Project documentation
```

## 🌟 Community

### Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Code Reviews**: Learn from feedback on your PRs

### Recognition

Contributors will be:
- Listed in the README acknowledgments
- Mentioned in release notes for significant contributions
- Invited to be maintainers for sustained contributions

## 🎯 Development Priorities

Current focus areas (in order of priority):

1. **Core Architecture**: Basic transformer implementation
2. **Training Pipeline**: Data loading and model training
3. **Inference Engine**: Text generation functionality
4. **Testing Framework**: Comprehensive test suite
5. **Documentation**: Tutorials and examples
6. **Performance**: Optimization and benchmarking

---

Thank you for contributing to MiniMe-LLM! Your contributions help make machine learning more accessible and educational for everyone. 🚀