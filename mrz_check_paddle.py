from mrz.checker.td1 import TD1CodeChecker, get_country

from paddleocr import PaddleOCR
from time import perf_counter

card_path_front = '/home/varunsakunia/PycharmProjects/MRZ/EID  LICENCE/EID & LICENCE/SAM-B7I55M/EID Front.jpeg'
card_path_back = '/home/varunsakunia/PycharmProjects/MRZ/EID  LICENCE/EID & LICENCE/SAM-B7I55M/eid-back.jpeg'


def paddle_ocr(img_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=False)
    t1 = perf_counter()
    result = ocr.ocr(img_path, cls=True)
    t2 = perf_counter()
    txts = [line[1][0] for line in result]
    time_elapsed = t2 - t1
    return txts, time_elapsed

front_text = paddle_ocr(img_path=card_path_front)[0]
back_text = paddle_ocr(img_path=card_path_back)[0]

mrz_format = repr(back_text[-3] + "\n") + repr(back_text[-2] + "\n") + repr(back_text[-1])
print(mrz_format)
print(str(mrz_format))
# extracted_mrz = mrz_format


def MRZ_result(back_text):
    # mrz_format_1 = mrz_format.replace('/\\n/g', "\n")
    # print(mrz_format_1)
    td1_check = TD1CodeChecker(str(repr(back_text[-3] + "\n")) + str(repr(back_text[-2] + "\n")) + str(repr(back_text[-1])))
    fields = td1_check.fields()
    DOB = ("/".join(reversed([fields.birth_date[i:i + 2] for i in range(0, len(fields.birth_date), 2)])))
    DOE = ("/".join(reversed([fields.expiry_date[i:i + 2] for i in range(0, len(fields.expiry_date), 2)])))
    final_dict = {
        "First Name": fields.name,
        "Surname": fields.surname,
        "Name": fields.name + " " + fields.surname,
        "Country": get_country(fields.country),
        "Nationality": get_country(fields.nationality),
        "ID Number": fields.optional_data,
        "DOB": DOB,
        "DOE": DOE,
        "Sex": fields.sex
    }
    final_list = [fields.name, fields.surname, str(fields.name + " " + fields.surname), get_country(fields.country),
                  get_country(fields.nationality), fields.optional_data, DOB, DOE, fields.sex]
    return final_list, final_dict


print(front_text)
print(back_text)
print(MRZ_result(back_text=back_text))
