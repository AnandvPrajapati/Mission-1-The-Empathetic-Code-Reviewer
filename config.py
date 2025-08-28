# config.py - Configuration settings for Empathetic Code Reviewer

"""
Configuration file for customizing Empathetic Code Reviewer behavior
Modify these settings to adapt the tool for different programming languages and feedback styles
"""

# OpenAI Configuration
OPENAI_MODEL = "gpt-4"  # Can be changed to "gpt-3.5-turbo" for cost savings
MAX_TOKENS = 3000       # Allow comprehensive, detailed feedback
TEMPERATURE = 0.4       # Balance creativity with consistency for empathy
TOP_P = 0.9

# Empathetic Feedback Configuration
EMPATHY_LEVELS = {
    'critical': {
        'intro_phrases': [
            "I can see you put thought into this!",
            "Great start on tackling this problem!",
            "You're on the right track here!",
            "I appreciate the logic you've implemented!"
        ],
        'encouragement': [
            "This shows good problem-solving thinking.",
            "You've got the core concept right.",
            "I can see the reasoning behind your approach."
        ]
    },
    'major': {
        'intro_phrases': [
            "Nice work on this function!",
            "I like your approach here!",
            "Good job structuring this code!",
            "You've implemented this well!"
        ],
        'encouragement': [
            "With a small adjustment, this will be even better.",
            "This is close to being really polished.",
            "You're developing good coding instincts."
        ]
    },
    'minor': {
        'intro_phrases': [
            "This looks great!",
            "Excellent work on this!",
            "Really solid implementation!",
            "I love how you've structured this!"
        ],
        'encouragement': [
            "Just a tiny refinement to make it perfect.",
            "This small enhancement will add nice polish.",
            "You're demonstrating strong coding skills."
        ]
    },
    'style': {
        'intro_phrases': [
            "Your logic is spot-on!",
            "The functionality here is perfect!",
            "Great problem-solving approach!",
            "You've nailed the core implementation!"
        ],
        'encouragement': [
            "A quick style adjustment will make this shine.",
            "This formatting tweak follows best practices.",
            "Your attention to detail is impressive."
        ]
    }
}

# Programming Language Support
LANGUAGE_CONFIGS = {
    'python': {
        'style_guide_url': 'https://peps.python.org/pep-0008/',
        'best_practices_url': 'https://docs.python.org/3/tutorial/',
        'common_improvements': [
            'List comprehensions for efficiency',
            'Descriptive variable names',
            'Proper boolean usage',
            'Function documentation with docstrings',
            'Exception handling'
        ],
        'code_examples_prefix': 'python'
    },
    'javascript': {
        'style_guide_url': 'https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide/Code_style_guide/JavaScript',
        'best_practices_url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide',
        'common_improvements': [
            'const/let instead of var',
            'Arrow functions for conciseness',
            'Array methods like map/filter/reduce',
            'Proper error handling',
            'ES6+ modern syntax'
        ],
        'code_examples_prefix': 'javascript'
    },
    'java': {
        'style_guide_url': 'https://google.github.io/styleguide/javaguide.html',
        'best_practices_url': 'https://docs.oracle.com/javase/tutorial/',
        'common_improvements': [
            'Proper access modifiers',
            'Generic types for type safety',
            'Exception handling',
            'Javadoc documentation',
            'SOLID principles'
        ],
        'code_examples_prefix': 'java'
    },
    'cpp': {
        'style_guide_url': 'https://google.github.io/styleguide/cppguide.html',
        'best_practices_url': 'https://isocpp.org/get-started',
        'common_improvements': [
            'RAII and smart pointers',
            'const correctness',
            'STL container usage',
            'Proper memory management',
            'Modern C++ features'
        ],
        'code_examples_prefix': 'cpp'
    }
}

# Severity Classification Patterns (for contextual awareness)
SEVERITY_KEYWORDS = {
    'critical': [
        'terrible', 'awful', 'wrong', 'bad', 'broken', 'horrible', 'disaster',
        'completely wrong', 'totally broken', 'doesn\'t work', 'fails'
    ],
    'major': [
        'inefficient', 'slow', 'poor', 'unclear', 'confusing', 'problematic',
        'needs improvement', 'should be fixed', 'major issue'
    ],
    'minor': [
        'consider', 'could be', 'might', 'perhaps', 'small', 'minor',
        'suggestion', 'opportunity', 'enhancement'
    ],
    'style': [
        'format', 'style', 'convention', 'naming', 'whitespace', 'indentation',
        'formatting', 'consistent', 'clean up', 'polish'
    ]
}

# Documentation and Resource Links
RESOURCE_CATEGORIES = {
    'performance': {
        'python': [
            'https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions',
            'https://docs.python.org/3/library/itertools.html'
        ],
        'javascript': [
            'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array',
            'https://web.dev/fast/'
        ]
    },
    'readability': {
        'python': [
            'https://peps.python.org/pep-0008/#naming-conventions',
            'https://docs.python.org/3/tutorial/controlflow.html#defining-functions'
        ],
        'javascript': [
            'https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide/Code_style_guide/JavaScript#naming_conventions'
        ]
    },
    'best_practices': {
        'general': [
            'https://en.wikipedia.org/wiki/Software_engineering_best_practices',
            'https://www.oreilly.com/library/view/clean-code-a/9780136083238/'
        ]
    }
}

# Report Formatting
REPORT_TEMPLATES = {
    'header': """# Empathetic Code Review Report

**Generated:** {timestamp}
**Language Detected:** {language}
**Comments Analyzed:** {comment_count}
**Processing Time:** {processing_time} seconds

---
""",

    'footer': """
---

## Review Summary & Encouragement

{custom_encouragement}

Remember that every experienced developer has written code similar to your original version. The fact that you're seeking feedback shows professionalism and a growth mindset that will serve you well throughout your career. Keep experimenting, keep learning, and most importantly, keep coding!

## Technical Details
- **Analysis Model:** {model}
- **Contextual Features:** Severity classification, language detection, resource linking
- **Educational Focus:** Software engineering principles with practical examples
- **Empathy Framework:** Positive psychology and growth mindset principles

*This empathetic analysis was generated by the Empathetic Code Reviewer - Mission 1 Solution, designed to transform critical feedback into constructive growth opportunities.*
"""
}

# Advanced Features Configuration
ADVANCED_FEATURES = {
    'contextual_awareness': True,    # Adapt tone based on comment severity
    'resource_linking': True,        # Include relevant documentation links
    'holistic_summary': True,        # Generate encouraging conclusion
    'multi_language_support': True,  # Support multiple programming languages
    'code_examples': True,          # Provide concrete improvement examples
    'alternative_approaches': True,  # Show multiple solution methods
    'learning_path_suggestions': True # Suggest next learning steps
}

# Logging Configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file_logging': False,  # Set to True to enable file logging
    'log_file': 'empathetic_reviewer.log'
}
