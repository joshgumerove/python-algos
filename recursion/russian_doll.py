def open_russian_doll(doll):
    if doll == 1:
        print(doll)
        print("all dolls are opened")

    else:
        print(doll)
        open_russian_doll(doll - 1)
        

print(open_russian_doll(7))