for file in range(1,51):
    with open(str(file) + "주차.txt","w",encoding="utf8") as report_file:
        report_file.write("- {} 주차 주간보고 -".format(file))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")
         