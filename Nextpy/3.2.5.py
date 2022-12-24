def read_file(file_name):
    try:
        content = "__CONTENT_START__\nr\n__CONTENT_END__"
        f = open(file_name, "r")
    except FileNotFoundError:
        cont = content.replace("r", "__NO_SUCH_FILE__")
    else:
        cont = content.replace("r", f.read())
        f.close()
    finally:
        return cont




print(read_file("name_length.txtt"))