from classes import Metal, NonMetal, Acid, Salt, Beaker, Flask

def main():
    print("1. Элементы:")
    h = Metal("Водород", "H", 1)
    o = NonMetal("Кислород", "O", 8)
    print(f"{h} - {h.get_type()}")
    print(f"{o} - {o.get_type()}")
    print(f"Водород легкий? {h.is_light()}")

    print("\n2. Соединение:")
    water = Acid("Вода", "H2O", 18.0)
    salt = Salt("Поваренная соль", "NaCl", 58.5)
    print(f"{water}")
    print(f"{salt}")
    print(f"Масса 2 молей воды: {water.get_mass(2)} г")

    print("\n3. Посуда:")
    beaker = Beaker("Хим. стакан", 250.0)
    flask = Flask("Колба", 500.0)
    beaker.pour("дистиллированная вода", 200.0)
    flask.pour("раствор кислоты", 300.0)
    print(f"{beaker}")
    print(f"{flask}")

    flask.empty()
    print(f"После очистки: {flask}")

if __name__ == "__main__":
    main()