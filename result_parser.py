def parse_vina_result(result_file):
    with open(result_file, "r") as r:
        lines = r.readlines()
        vina_result = ""
        for line in lines:
            if line.startswith("REMARK VINA RESULT:"):
                vina_result = line.split(":")[1].strip()
                break
        return vina_result
