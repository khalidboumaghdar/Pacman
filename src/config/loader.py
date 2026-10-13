from pathlib import Path
import json
from .shema import Config

DEFAULT_CONFIG = {
    "highscore_filename": "highscore.json",
    "width": 21,
    "height": 21,
    "lives": 3,
    "pacgum": 42,
    "points_per_pacgum": 10,
    "points_per_super_pacgum": 50,
    "points_per_ghost": 200,
    "seed": 42,
    "level_max_time": 90,
    "levels": [{"width": 21,  "height": 21, "pacgum": 12} for _ in range(10)],
}


class Parser:

    def check_data(self, path: str) -> str | None:
        try:
            if Path(path).suffix != ".json":
                print("! Warning suffix shold be .json")
                return None

            with open(path, "r") as p:
                data = []
                for line in p:
                    if line.strip().startswith("#") or not line.strip():
                        continue
                    if '#' in line:
                        line = line.split('#')[0].strip()

                    data.append(line)
                if len(data) == 0:
                    print("! config is empty")
                    return None
                return "".join(data)
        except FileNotFoundError as f:
            print(f)
            return None

    def read_data(self, raw: str) -> dict | None:
        try:
            return json.loads(raw)
        except json.JSONDecodeError as e:
            print("! json invalide ")
            print(e)
            return None

    def add_default_data(self, data: dict | None) -> dict:
        if data is None:
            print("! no valide config data")
            data = {}

        result = dict(DEFAULT_CONFIG)

        for key, default_value in DEFAULT_CONFIG.items():
            if key not in data:
                print(f"! missing key : {key}")
                continue

            value = data[key]
            if key == "highscore_filename":
                if not isinstance(value, str) or not Path(value).suffix:
                    print(
                        f"! Invalid highscore_filename: {value}"
                        f" -> using default: {default_value}"
                    )
                    continue
            if key == "lives":
                if value < 1:
                    print(
                        f"! must be lives than to  : {value}"
                        f" -> using default: {default_value}"
                    )
                    continue

            if key == "levels":
                try:
                    Config(levels=value)
                    if len(value) < 10:
                        ms = 10 - len(value)
                        print("\n =============== Error ⛔ ========"
                              "==================\n")
                        print(f"! Warning: you have {len(value)} levels")
                        print(f"\n================ ! Adding {ms} default"
                              "levels ✅ =============\n")
                        value = value + default_value[:ms]
                    for i, level in enumerate(value):
                        if level["width"] > 45:
                            print("⛔ !warning width is to long ")
                            value[i]["width"] = default_value[i]["width"]
                            print("\n================ ! Using default width "
                                  "data =============\n")
                        if level["height"] > 25:
                            print("⛔ !warning height is to long ")
                            print("\n================ ! Using default height "
                                  "data =============\n")
                            value[i]["height"] = default_value[i]["height"]
                        m_pucgam = level["width"] * level["height"] - 19
                        if level["pacgum"] > m_pucgam:
                            print("⛔ !warning pacgum is to long ")
                            print("\n================ ! Using default pacgame "
                                  "data =============\n")
                            value[i]["pacgum"] = default_value[i]["pacgum"]
                    result[key] = value
                    continue
                except Exception as e:
                    print("! Invalid levels")
                    erorrs = []
                    for err in e.errors():
                        erorrs.append(err["msg"])

                    print("\n =============== Error ⛔ =========="
                          "================\n")
                    for er in erorrs:
                        print(f"  Error: {er}")
                    print("\n================ Using Default Data ✅ ===="
                          "=========\n")
                    print(f"-> using default: {default_value}")
                    continue

            if not isinstance(value, type(default_value)):
                print(f"! invalide data in : {key}"
                      f"-> using default :{default_value}")
                continue

            if isinstance(value, int) and value < 0:
                print(f"Negative number in key :{key}"
                      f"-> using default: {default_value}")
                continue

            result[key] = value

        unknown_key = set(data) - set(DEFAULT_CONFIG)
        if unknown_key:
            print(f"! Ignoring unknown keys: {'- '.join(unknown_key)}")

        return result

    def parse(self, path: str) -> dict:
        try:
            ch = self.check_data(path)
            data = self.read_data(ch) if ch is not None else None
            return self.add_default_data(data)
        except Exception as e:
            print(e)
