def outer_funtion():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function()


inner_function = outer_funtion()
inner_function()
