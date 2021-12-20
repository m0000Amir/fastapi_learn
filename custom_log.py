def log(tag="", message=""):
    with open("log.text", "w+") as log:
        log.write(f"{tag}: {message}\n")