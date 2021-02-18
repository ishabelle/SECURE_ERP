import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

                generated_id = ""
                elements_of_id = []


                for _ in range(number_of_small_letters):
                    elements_of_id.append(random.choice(string.ascii_lowercase))
                for _ in range(number_of_capital_letters):
                    elements_of_id.append(random.choice(string.ascii_uppercase))
                for _ in range(number_of_digits):
                    elements_of_id.append(random.choice(range(0, 10)))
                for _ in range(number_of_special_chars):
                    elements_of_id.append(random.choice(allowed_special_chars))

                random.shuffle(elements_of_id)

                for element in elements_of_id:
                    element = str(element)
                    generated_id += element

                return generated_id
