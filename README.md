# Game of Life
Game of Life written in Python and Flask framework

## Usage
Install dependencies:
- with `pip`:
```bash
pip install -r requirements.txt
```
- with `poetry`:
```bash
poetry install
```

You could specify address and port with env variables: `GAME_OF_LIFE_ADDRESS` and `GAME_OF_LIFE_PORT`.

Run the app:
- with `make`:
```bash
make
```
- manual:
```bash
python game-of-life main.py
```
Or in the `debug` mode:
```bash
make debug
```
```bash
python game-of-life main.py --debug
```

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
