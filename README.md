
# Tetris by Ayush

## Features
- Classic Tetris gameplay with smooth controls
- Colorful tetrominoes and grid
- Sound effects for game start, bonus, and game over
- Pause, restart, and mute functionality
- Responsive window and custom icon

## Folder Structure
```
├── main.py                # Entry point for the game
├── pyproject.toml         # Project metadata and dependencies
├── uv.lock                # Lock file for dependencies
├── icon.png               # Game window icon
├── assets/                # Game sound assets
│   ├── game-bonus.mp3
│   ├── game-over.mp3
│   └── game-start.mp3
├── tetris/                # Game package
│   ├── __init__.py
│   ├── audio.py           # Audio loading and management
│   ├── constants.py       # Game constants and settings
│   ├── game.py            # Main game logic
│   └── tetromino.py       # Tetromino shapes and logic
└── README.md
```

## How to Run
1. Install dependencies (see `pyproject.toml`).
2. Run the game:
	```bash
	python main.py
	```

## Controls
- **Arrow keys**: Move and rotate tetrominoes
- **Space**: Start game
- **R**: Restart after game over
- **P**: Pause
- **M**: Mute/unmute sound

## License
BSD 3-Clause License  
Copyright (c) 2025 All rights reserved.

## Credits for Assets
- Game over Sound Effect by [FoxBoyTails](https://pixabay.com/users/foxboytails-49447089/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=317318) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=317318)
- Game start Sound Effect by [freesound_community](https://pixabay.com/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=38511) from [Pixabay](https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=38511)
- Game bonus Sound Effect by [Universfield](https://pixabay.com/users/universfield-28281460/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=294436) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=294436)
- Game logo made with Gemini and Pillow library (free to use)
