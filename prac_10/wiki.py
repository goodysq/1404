import wikipedia


def main():
    try:
        user_search = input("What do you want to search for? ")
        page = wikipedia.page(user_search)
        print(f"{page.title} \n{page.summary} \n{page.url}")
        while user_search != "":
            user_search = input("What do you want to search for? ")
            page = wikipedia.page(user_search)
            print(f"{page.title} \n{page.summary} \n{page.url}")
    except wikipedia.exceptions.WikipediaException:
        quit()


main()
