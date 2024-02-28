import pandas as pd

file_path1 = "./EIS/PANA 2.5/PANA 2.5.xlsx"
output_path1 = "./eis PANA2.5A.txt"

file_path2 = "./EIS/PANA 3.0/PANA 3.0.xlsx"
output_path2 = "./eis PANA3.0A.txt"

file_path3 = "./EIS/SANYO 2.5/SANYO 2.5.xlsx"
output_path3 = "./eis SANYO2.5A.txt"

file_path4 = "./EIS/SANYO 3.0/SANYO 3.0.xlsx"
output_path4 = "./eis SANYO3.0A.txt"


def EIS(file_path, output_path):
    sheets_data = {}

    with pd.ExcelFile(file_path) as xls:
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            columns_data = df.iloc[0:, [3, 4]]
            sheets_data[sheet_name] = columns_data

    dic = {}

    for key in sheets_data:
        # if key == '20':
        #     break

        df = sheets_data[key]
        col1 = df["Re(Z)/Ohm"]
        col2 = df["-Im(Z)/Ohm"]

        print(f"key: {key}, col1.size: {col1.size}, col2.size: {col2.size}")

        if col1.size == 0:
            break

        l = []

        if col1.size >= 60:
            cnt = 0
            for item in col1:
                l.append(str(item))
                cnt += 1
                if cnt == 60:
                    break
            cnt = 0
            for item in col2:
                l.append(str(item))
                cnt += 1
                if cnt == 60:
                    break
        else:
            for item in col1:
                l.append(str(item))
            for i in range(60 - col1.size):
                l.append(str(col1[col1.size - 1]))

            for item in col2:
                l.append(str(item))
            for i in range(60 - col2.size):
                l.append(str(col2[col2.size - 1]))

        dic[key] = l

    print("-" * 50)

    result = ""
    for key in dic:
        print(f"key: {key}, len: {len(dic[key])}")
        for item in dic[key]:
            result += item + " "
        result = result[:-1] + "\n"

    with open(output_path, "w") as f:
        f.write(result)


print("-" * 50)
EIS(file_path1, output_path1)
print("-" * 50)
EIS(file_path2, output_path2)
print("-" * 50)
EIS(file_path3, output_path3)
print("-" * 50)
EIS(file_path4, output_path4)
print("-" * 50)
