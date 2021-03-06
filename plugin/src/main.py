import glob

from .services import search_in_file, soft_scrape_from_file


def search_in_current_file(*, word, filename):
    return search_in_file(word=word, file=filename)


def hard_scraping(*, word, filename):
    for extension in ['js', 'jsx', 'ts', 'tsx']:
        for file in glob.glob('src/**/*.{}'.format(extension), recursive=True):
            result = search_in_file(file=file, word=word)

            if result:
                return


def soft_scraping(*, word, filename):
    return soft_scrape_from_file(
        wanted_definition=word,
        filename=filename,
        current_level=0
    )


def goto_definition(*, word, filename):
    found = soft_scraping(word=word, filename=filename)
    if found:
        return

    found = hard_scraping(word=word, filename=filename)
    if found:
        return
