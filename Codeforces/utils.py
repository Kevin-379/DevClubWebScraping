def getNumProblems(driver, url):
    driver.get(url)
    if driver.current_url != url:  # Invalid contest number, redirected to codeforces.com
        print("Invalid round number")
        exit()
    el = driver.find_element_by_class_name("problems")  # Table of problems
    probs = el.find_elements_by_tag_name("tr")  # All rows of table
    return len(probs)-1


def getExamples(driver, dir, prob):
    el = driver.find_element_by_class_name("sample-test")
    inputs = el.find_elements_by_class_name("input")  # All inputs
    outputs = el.find_elements_by_class_name("output")  # All outputs
    for i in range(len(inputs)):
        inp, out = inputs[i], outputs[i]
        with open(f"./{dir}/{prob}/input{i+1}.txt", "w") as f:
            f.write(inp.text[11:])  # Keep inputs only
        with open(f"./{dir}/{prob}/output{i+1}.txt", "w") as f:
            f.write(out.text[12:])
